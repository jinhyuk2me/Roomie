# 비품 주문 및 배송 프로세스 명세서

## 1. 개요

이 문서는 Roomie Main Server(RMS)의 비품 주문 및 배송 기능에 대한 상세 프로세스를 정의합니다. 이 문서는 `food_delivery_scenario.md`와 시스템의 현재 데이터베이스 스키마를 기반으로 작성되었습니다.

**핵심 원칙**:
- **재사용성**: 가능한 한 음식 배송 프로세스와 동일한 API 엔드포인트, ROS2 토픽, 상태(status) 흐름을 재사용하여 시스템의 복잡도를 낮춥니다.
- **확장성**: `task` 테이블의 `type_id`를 통해 비품 배송과 음식 배송 로직을 명확히 구분하여 처리합니다.

## 2. 프로세스 단계별 상세 명세

### 단계 1: 비품 목록 조회

- **요청자**: Guest GUI (GGUI)
- **수신자**: RMS (Roomie Main Server)
- **API**: `POST /api/gui/get_supply_menu`
- **처리 과정**:
    1. GGUI가 RMS에 비품 목록을 요청합니다.
    2. RMS는 `supply` 테이블에서 모든 비품 정보를 조회하여 GGUI에 반환합니다.
        ```sql
        -- 실제 실행되는 쿼리 예시
        SELECT id, name, image FROM supply;
        ```

### 단계 2: 배송 작업 생성

- **요청자**: GGUI
- **수신자**: RMS
- **API**: `POST /api/gui/create_delivery_task`
- **처리 과정**:
    1. GGUI가 주문 정보(배송지, 주문 비품 등)를 담아 RMS에 배송 작업을 요청합니다.
        - **`task_type_name`**: **'비품배송'** 으로 설정하여 전송합니다.
    2. RMS는 트랜잭션 내에서 다음 테이블들에 데이터를 생성합니다.
        - **`task` 테이블**:
            - `type_id`: **'비품배송'**에 해당하는 ID를 `task_type` 테이블에서 조회하여 설정합니다.
            - `task_status_id`: 초기 상태인 **'접수됨'** ID를 사용합니다.
            - `location_id`: 목적지 ID를 사용합니다.
        - **`order` 테이블**:
            - `total_price`는 0으로 설정합니다 (비품은 가격이 없음).
        - **`supply_order_item` 테이블**:
            - `order_id`를 참조하여 주문된 각 비품 항목을 생성합니다. (음식 배송의 `food_order_item` 테이블과 구분됩니다.)
            ```sql
            -- 실제 실행되는 쿼리 예시
            INSERT INTO supply_order_item (order_id, supply_id, quantity)
            VALUES (%s, %s, %s);
            ```
    3. 모든 DB 작업이 성공하면 트랜잭션을 커밋합니다.

### 단계 3: 비품 주문 발생 알림 (WebSocket)

- **발신자**: RMS
- **수신자**: 모든 Staff GUI (SGUI) 클라이언트
- **처리 과정**:
    - `task` 생성이 성공적으로 완료되면, RMS는 'staff' 그룹에 `supply_order_creation` 이벤트를 브로드캐스트합니다.
- **메시지 형식 (예시)**:
    ```json
    {
      "event_type": "supply_order_creation",
      "payload": {
        "task_id": 124,
        "request_location": "ROOM_102",
        "order_details": {
          "items": [
            {"name": "타월", "quantity": 2},
            {"name": "생수", "quantity": 4}
          ]
        },
        "created_at": "2024-07-26T11:00:00Z"
      }
    }
    ```

### 단계 4: 예상 도착 시간 응답

- **발신자**: RMS
- **수신자**: GGUI
- **처리 과정**:
    - 음식 배송과 동일하게, 작업 생성 요청에 대한 HTTP 응답으로 생성된 작업 정보와 예상 도착 시간을 반환합니다.

### 단계 5: 비품 준비 완료

- **요청자**: SGUI
- **수신자**: RMS
- **API**: `POST /api/gui/change_task_status` (기존 API 재사용)
- **처리 과정**:
    1. 직원이 비품을 준비하고 SGUI에서 '준비 완료' 버튼을 클릭합니다.
    2. RMS는 해당 `task`의 `task_status_id`를 **'준비 완료'** 상태로 업데이트합니다.

### 단계 6: 로봇 할당

- **트리거**: 로봇이 **'작업 가능'** 상태가 됨.
- **처리 주체**: RMS (`rms_node`)
- **처리 과정**:
    - 음식 배송 시나리오와 완벽히 동일합니다. '준비 완료' 상태인 가장 오래된 작업(음식/비품 무관)을 '작업 가능' 로봇에게 할당합니다.

### 단계 7: 작업 할당 지시 (Action)

- **발신자**: RMS
- **수신자**: RC
- **처리 과정**:
    - `'/roomie/action/perform_task'` 액션을 호출하여 작업을 지시합니다.
- **액션 목표(Goal) 데이터 (예시)**:
    ```
    robot_id: 2
    task_id: 124
    task_status_id: 2 # '로봇 할당됨'
    target_location_id: 102 # 'ROOM_102'
    pickup_location_id: 4  # 'SUP_PICKUP' (비품 픽업 장소 ID)
    order_info: '{"items": [{"name": "타월", "quantity": 2}, ...]}'
    ```
    - **주요 차이점**: `pickup_location_id`가 DB에 정의된 비품 픽업 장소(`SUP_PICKUP`)의 ID로 설정됩니다.

### 단계 8 ~ 12: 이후 과정

- **픽업 장소 도착**: 로봇이 `SUP_PICKUP` 위치에 도착하면 `pickup_arrival` 이벤트가 발생합니다. (음식과 비품을 구분하는 이벤트 이름 제안)
- **픽업 완료**: 직원이 비품을 로봇에 실으면 `pickup_completed` 이벤트가 발생합니다.
- **배송 및 완료**: 이후의 모든 과정(배송, 목적지 도착, 수령 완료)은 음식 배송 시나리오와 동일한 토픽과 상태 흐름을 따릅니다. 