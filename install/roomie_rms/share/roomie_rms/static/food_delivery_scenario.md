# 음식 주문 및 배송 시나리오

## 1. 개요

이 문서는 Roomie Main Server(RMS)의 음식 주문 및 배송 기능에 대한 상세 프로세스를 정의합니다. 모든 프로세스는 현재 구현된 데이터베이스 스키마와 코드 로직을 기준으로 작성되었습니다.

**핵심 원칙**:
- **상태 정보 기준**: `task_status`, `robot_status` 등 상태 정보의 기준은 항상 데이터베이스입니다. 코드에서는 이 값들을 동적으로 로드하여 사용하며, 이 문서에서는 이해를 돕기 위해 '이름'을 기준으로 서술합니다.
- **상태 관리**: 로봇의 실시간 상태(위치, 배터리, 현재 상태 등)는 `robot_current_state` 테이블을 통해 관리됩니다.

## 2. 프로세스 단계별 상세 명세

### 단계 1: 음식 메뉴 조회

- **요청자**: Guest GUI (GGUI)
- **수신자**: RMS (Roomie Main Server)
- **API**: `POST /api/gui/get_food_menu`
- **처리 과정**:
    1. GGUI가 RMS에 음식 메뉴를 요청합니다.
    2. RMS는 `food` 테이블에서 모든 메뉴 정보를 조회하여 GGUI에 반환합니다.
        ```sql
        -- 실제 실행되는 쿼리 예시
        SELECT name, price, image FROM food;
        ```

### 단계 2: 배송 작업 생성

- **요청자**: GGUI
- **수신자**: RMS
- **API**: `POST /api/gui/create_delivery_task`
- **처리 과정**:
    1. GGUI가 주문 정보(배송지, 주문 음식 등)를 담아 RMS에 배송 작업을 요청합니다.
    2. RMS는 트랜잭션 내에서 다음 테이블들에 데이터를 생성합니다.
        - **`task` 테이블**:
            - `type_id`: '음식배송'에 해당하는 ID를 `task_type` 테이블에서 조회하여 설정합니다.
            - `task_status_id`: 초기 상태인 **'접수됨'**에 해당하는 ID를 `task_status` 테이블에서 조회하여 설정합니다.
            - `location_id`: 목적지에 해당하는 ID를 `location` 테이블에서 조회하여 설정합니다.
            ```sql
            -- 실제 실행되는 쿼리 예시
            INSERT INTO task (type_id, task_status_id, location_id, task_creation_time)
            VALUES (%s, %s, %s, %s);
            ```
        - **`order` 테이블**:
            - 계산된 총 주문 금액과 함께 `task_id`를 참조하여 주문 정보를 생성합니다.
        - **`food_order_item` 테이블**:
            - `order_id`를 참조하여 주문된 각 음식 항목을 생성합니다.
    3. 모든 DB 작업이 성공하면 트랜잭션을 커밋합니다. 실패 시 롤백합니다.

### 단계 3: 음식 주문 발생 알림 (WebSocket)

- **발신자**: RMS
- **수신자**: 모든 Staff GUI (SGUI) 클라이언트
- **처리 과정**:
    1. `task` 생성이 성공적으로 완료되면, RMS는 'staff' 그룹의 모든 SGUI 클라이언트에게 WebSocket을 통해 `food_order_creation` 이벤트를 브로드캐스트합니다.
- **메시지 형식 (예시)**:
    ```json
    {
      "event_type": "food_order_creation",
      "payload": {
        "task_id": 123,
        "request_location": "ROOM_101",
        "order_details": {
          "items": [
            {"name": "스파게티", "quantity": 1, "price": 15000}
          ]
        },
        "created_at": "2024-07-26T10:00:00Z"
      }
    }
    ```

### 단계 4: 예상 도착 시간 응답

- **발신자**: RMS
- **수신자**: GGUI
- **처리 과정**:
    - RMS는 작업 생성 요청(단계 2)에 대한 HTTP 응답으로, 생성된 작업 정보와 예상 도착 시간을 GGUI에 반환합니다.

### 단계 5: 음식 준비 완료

- **요청자**: SGUI
- **수신자**: RMS
- **API**: `POST /api/gui/change_task_status` (가칭, 구현 필요)
- **처리 과정**:
    1. 주방 직원이 음식 준비를 마치고 SGUI에서 '준비 완료' 버튼을 클릭합니다.
    2. SGUI는 해당 `task_id`와 함께 상태 변경을 RMS에 요청합니다.
    3. RMS는 해당 `task`의 `task_status_id`를 **'준비 완료'** 상태로 업데이트합니다.
        ```sql
        -- 실제 실행되는 쿼리 예시
        UPDATE task SET task_status_id = %s WHERE id = %s;
        -- %s에 '준비 완료' 상태의 ID가 바인딩됩니다.
        ```

### 단계 6: 로봇 할당

- **트리거**: RC(Robot Controller)로부터 특정 로봇의 상태가 **'작업 가능'**이라는 `robot_state` 토픽 메시지 수신
- **처리 주체**: RMS (`rms_node`)
- **처리 과정**:
    1. RMS의 `rms_node`는 항상 `/roomie/status/robot_state` 토픽을 구독하며 로봇들의 상태를 모니터링합니다.
    2. '작업 가능' 상태의 로봇이 감지되면, RMS는 **가장 오래된 '준비 완료' 상태의 `task`**를 찾습니다. (선입선출)
    3. 해당 `task`에 로봇을 할당하고(`robot_id` 업데이트), `task_status_id`를 **'로봇 할당됨'** 상태로 변경하며 `robot_assignment_time`을 기록합니다.

### 단계 7: 작업 할당 지시 (Action)

- **발신자**: RMS
- **수신자**: RC
- **처리 과정**:
    1. 로봇 할당(단계 6)이 완료되면, RMS는 RC에게 `'/roomie/action/perform_task'` 액션을 호출하여 실제 작업을 지시합니다.
- **액션 목표(Goal) 데이터 (예시)**:
    ```
    robot_id: 1
    task_id: 123
    task_status_id: 2 # '로봇 할당됨'
    target_location_id: 101 # 'ROOM_101'
    pickup_location_id: 2  # 'RES_PICKUP'
    order_info: '{"items": [{"name": "스파게티", "quantity": 1}]}'
    ```

### 단계 8: 로봇 상태 동기화

- **트리거**: RC로부터 `robot_state` 토픽 메시지 수신
- **처리 주체**: RMS
- **처리 과정**:
    - RMS는 RC로부터 받은 로봇의 최신 상태(`robot_state_id`, `battery_level` 등)를 **`robot_current_state`** 테이블에 즉시 업데이트합니다.
    - 이를 통해 AGUI(Admin GUI) 등에서 로봇의 최신 상태를 항상 조회할 수 있습니다.
        ```sql
        -- 실제 실행되는 쿼리 예시 (UPSERT 로직)
        -- robot_id가 존재하면 UPDATE, 없으면 INSERT
        INSERT INTO robot_current_state (robot_id, robot_status_id, last_updated_time)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE robot_status_id = VALUES(robot_status_id), last_updated_time = VALUES(last_updated_time);
        ```

### 단계 9: 픽업 장소 도착 및 알림

- **트리거**: RC로부터 'RES_PICKUP' 위치에 도착했다는 `/roomie/event/arrival` 토픽 메시지 수신
- **처리 주체**: RMS
- **처리 과정**:
    1. RMS는 해당 `task`의 `task_status_id`를 **'픽업 대기 중'**으로 업데이트합니다.
    2. RMS는 RC에게도 동일한 작업 상태를 `/roomie/status/task_state` 토픽으로 전파합니다.
    3. RMS는 모든 SGUI 클라이언트에게 `food_pickup_arrival` 이벤트를 WebSocket으로 브로드캐스트하여 로봇이 픽업을 기다리고 있음을 알립니다.

### 단계 10: 픽업 완료

- **트리거**: RC로부터 `/roomie/event/pickup_completed` 토픽 메시지 수신
- **처리 주체**: RMS
- **처리 과정**:
    1. RMS는 해당 `task`의 `task_status_id`를 **'배송 중'**으로 업데이트하고, `pickup_completion_time`을 기록합니다.
    2. RMS는 RC에게도 변경된 작업 상태를 전파합니다.

### 단계 11: 배송 목적지 도착 및 알림

- **트리거**: RC로부터 최종 목적지(예: 'ROOM_101')에 도착했다는 `/roomie/event/arrival` 토픽 메시지 수신
- **처리 주체**: RMS
- **처리 과정**:
    1. RMS는 해당 `task`의 `task_status_id`를 **'배송 도착'**으로 업데이트하고, `delivery_arrival_time`을 기록합니다.
    2. RMS는 RC에게도 변경된 작업 상태를 전파합니다.
    3. RMS는 **해당 목적지(location_name)의 GGUI 클라이언트에게만** `delivery_completion` 이벤트를 WebSocket으로 전송하여 배송 도착을 알립니다.

### 단계 12: 작업 최종 완료

- **트리거**: RC로부터 `/roomie/event/delivery_completed` 토픽 메시지 수신 (손님이 물건을 수령 완료)
- **처리 주체**: RMS
- **처리 과정**:
    1. RMS는 해당 `task`의 `task_status_id`를 **'수령 완료'**로 업데이트하고, `task_completion_time`을 기록합니다.
    2. RMS는 RC에게도 최종 작업 상태를 전파합니다.
    3. 로봇은 다음 작업을 수행하거나 대기 장소로 복귀합니다. 