# 음식 주문 및 배송 프로세스 명세서

## 개요

현재는 MySQL DB가 구현되지 않은 상태이며, 로봇은 1대만 운용 중이라고 가정합니다.
인터페이스 명세서와 ER 다이어그램의 테이블 구조를 참고하여 작성되었습니다.

## 프로세스 단계별 상세 명세

### 1. 음식 메뉴 조회

**요청자**: Guest GUI (GGUI)  
**수신자**: Roomie Main Server (RMS)

**처리 과정**:
- GGUI가 RMS에 음식 메뉴 요청 (`get_food_menu`)을 전송
- RMS는 `food` 테이블에서 모든 메뉴 정보 조회
  ```sql
  SELECT id, name, price, image FROM food;
  ```
- 현재는 하드코딩된 더미 데이터 사용 (DB 미구현 상태)
- RMS가 GGUI에 음식 메뉴 목록 응답 (`get_food_menu`)

**참고 데이터**:
- `food` 테이블: id(0-3), name(스파게티, 피자, 스테이크, 버거), price, image

### 2. 배송 작업 생성

**요청자**: Guest GUI (GGUI)  
**수신자**: Roomie Main Server (RMS)

**처리 과정**:
- GGUI가 RMS에 배송 작업 생성 요청 (`create_delivery_task`)을 전송
- RMS는 다음 테이블에 데이터를 생성:

  **`task` 테이블 생성**:
  ```sql
  INSERT INTO task (id, type_id, task_status_id, location_id, robot_id, task_creation_time, 
                   robot_assignment_time, pickup_completion_time, delivery_arrival_time, 
                   task_completion_time, task_cancellation_time)
  VALUES (새로운_task_id, 0, 0, 목적지_location_id, NULL, NOW(), NULL, NULL, NULL, NULL, NULL);
  ```
  
  **`order` 테이블 생성**:
  ```sql
  INSERT INTO `order` (id, task_id, location_id, total_price)
  VALUES (새로운_order_id, task_id, 목적지_location_id, 총_주문금액);
  ```
  
  **`food_order_item` 테이블 생성**:
  ```sql
  INSERT INTO food_order_item (id, order_id, food_id, quantity)
  VALUES (새로운_item_id, order_id, 음식_id, 수량);
  ```

**설정 값**:
- `type_id`: 0 (음식배송)
- `task_status_id`: 0 (접수됨)
- `location_id`: 배송 목적지 (예: 201 for ROOM_201)

### 3. 음식 주문 발생 알림

**발신자**: Roomie Main Server (RMS)  
**수신자**: Staff GUI (SGUI)

**처리 과정**:
- RMS는 SGUI에 WebSocket을 통해 음식 주문 발생 이벤트 전송

**메시지 형식**:
```json
{
  "type": "event",
  "action": "food_order_creation",
  "payload": {
    "task_id": "생성된_task_id",
    "request_location": "목적지_location_name",
    "order_details": {
      "items": [
        {"name": "음식명", "quantity": 수량, "price": 가격}
      ]
    }
  }
}
```

### 4. 예상 도착 시간 응답

**발신자**: Roomie Main Server (RMS)  
**수신자**: Guest GUI (GGUI)

**처리 과정**:
- RMS는 예상 도착 시간을 산출 (현재: 임의로 30분 설정)
- GGUI에 배송 작업 생성 응답 (`create_delivery_task`) 전송

**응답 데이터**:
- `task_id`: 생성된 작업 ID
- `estimated_time`: 30분 (하드코딩)
- `success`: true
- `message`: "배송 작업이 생성되었습니다"

### 5. 음식 준비 완료 처리

**요청자**: Staff GUI (SGUI)  
**수신자**: Roomie Main Server (RMS)

**처리 과정**:
- SGUI가 RMS에 음식 주문 작업상태 전환 요청 (`food_order_status_change`)
- RMS는 `task` 테이블의 `task_status_id`를 1 (준비 완료)로 변경
  ```sql
  UPDATE task SET task_status_id = 1 WHERE id = task_id;
  ```
- RMS가 SGUI에 작업상태 전환 응답 (`food_order_status_change`)

### 6. 로봇 할당

**처리 조건**: Robot Controller (RC)의 로봇 상태 토픽에서 `robot_state_id = 1` (작업 가능) 확인

**처리 과정**:
- RMS는 `/roomie/status/robot_state` 토픽을 구독하여 로봇 상태 모니터링
- `robot_state_id = 1` (작업 가능) 상태인 로봇 감지 시:
  ```sql
  UPDATE task SET robot_id = 할당할_robot_id, task_status_id = 2, robot_assignment_time = NOW() 
  WHERE id = task_id;
  ```
- `task_status_id`: 2 (로봇 할당됨)

**참고 데이터**:
- `robot_status` 테이블: id=1은 "작업 가능" 상태

### 7. 작업 할당 지시

**발신자**: Roomie Main Server (RMS)  
**수신자**: Robot Controller (RC)

**처리 과정**:
- RMS가 RC에 `/roomie/action/perform_task` 액션 호출

**액션 Goal 데이터**:
```
robot_id: 할당된_로봇_id
task_id: 작업_id
task_type_id: 0 (음식배송)
task_status_id: 2 (로봇 할당됨)
target_location_id: 목적지_location_id
pickup_location_id: 2 (RES_PICKUP)
order_info: JSON 형태의 주문 정보
```

### 8. 로봇 상태 동기화

**처리 조건**: RC의 로봇 상태 토픽에서 `robot_state_id = 3` (작업 수행중) 확인

**처리 과정**:
- RMS는 `/roomie/status/robot_state` 토픽 구독
- `robot_state_id = 3` (작업 수행중) 상태 감지 시:
  ```sql
  UPDATE robot SET robot_status_id = 3 WHERE id = robot_id;
  ```

### 9. 픽업 장소로 이동 상태 변경

**처리 과정**:
- RMS는 현재 task의 `task_status_id`를 3 (픽업 장소로 이동)으로 변경
  ```sql
  UPDATE task SET task_status_id = 3 WHERE id = task_id;
  ```
- RMS가 RC에 `/roomie/status/task_state` 토픽으로 작업 상태 전송

**토픽 메시지**:
```
task_id: 작업_id
task_state_id: 3
```

### 10. 픽업 장소 도착 처리

**처리 조건**: RC의 장소 도착 토픽에서 `location_id = 2` (RES_PICKUP) 도착 확인

**처리 과정**:
- RMS는 `/roomie/event/arrival` 토픽 구독
- `location_id = 2` (픽업장소) 도착 시:
  ```sql
  UPDATE task SET task_status_id = 4 WHERE id = task_id;
  ```
- RMS가 RC에 작업 상태 (`task_state_id = 4`) 전송

**참고 데이터**:
- `location` 테이블: id=2는 "RES_PICKUP" (음식 픽업 장소)
- `task_status` 테이블: id=4는 "픽업 대기 중"

### 11. 음식 픽업 도착 알림

**발신자**: Roomie Main Server (RMS)  
**수신자**: Staff GUI (SGUI)

**처리 과정**:
- RMS가 SGUI에 WebSocket을 통해 픽업 도착 이벤트 전송

**메시지 형식**:
```json
{
  "type": "event",
  "action": "food_pickup_arrival",
  "payload": {
    "task_id": "작업_id",
    "robot_id": "로봇_id"
  }
}
```

### 12. 픽업 완료 처리

**처리 조건**: RC의 픽업 완료 토픽 수신

**처리 과정**:
- RMS는 `/roomie/event/pickup_completed` 토픽 구독
- 픽업 완료 이벤트 수신 시:
  ```sql
  UPDATE task SET task_status_id = 5, pickup_completion_time = NOW() WHERE id = task_id;
  ```
- RMS가 RC에 작업 상태 (`task_state_id = 5`) 전송

**참고 데이터**:
- `task_status` 테이블: id=5는 "배송 중"

### 13. 배송 목적지 도착 처리

**처리 조건**: RC의 장소 도착 토픽에서 목적지 `location_id` 도착 확인

**처리 과정**:
- RMS는 `/roomie/event/arrival` 토픽 구독
- task의 목적지 `location_id`와 일치하는 도착 이벤트 수신 시:
  ```sql
  UPDATE task SET task_status_id = 6, delivery_arrival_time = NOW() WHERE id = task_id;
  ```
- RMS가 RC에 작업 상태 (`task_state_id = 6`) 전송

**참고 데이터**:
- `task_status` 테이블: id=6은 "배송 도착"

### 14. 배송 완료 알림

**발신자**: Roomie Main Server (RMS)  
**수신자**: Guest GUI (GGUI)

**처리 과정**:
- RMS가 GGUI에 WebSocket을 통해 배송 완료 이벤트 전송

**메시지 형식**:
```json
{
  "type": "event",
  "action": "delivery_completion",
  "payload": {
    "task_name": "작업_id",
    "request_location": "목적지_location_name"
  }
}
```

## 데이터베이스 테이블 참조

### 주요 테이블 구조

**`task` 테이블**:
- `id`: 작업 고유 ID
- `type_id`: 작업 유형 (0: 음식배송)
- `task_status_id`: 작업 상태 (0: 접수됨, 1: 준비완료, 2: 로봇할당됨, ...)
- `location_id`: 목적지 위치
- `robot_id`: 할당된 로봇 ID

**`task_status` 테이블**:
- 0: 접수됨
- 1: 준비 완료
- 2: 로봇 할당됨
- 3: 픽업 장소로 이동
- 4: 픽업 대기 중
- 5: 배송 중
- 6: 배송 도착
- 7: 수령 완료

**`location` 테이블**:
- 2: RES_PICKUP (음식 픽업 장소)
- 101-302: 각 객실 (ROOM_101, ROOM_102, ...)

## 구현 고려사항

1. **에러 처리**: 각 단계에서 실패 시 적절한 롤백 처리 필요
2. **동시성**: 여러 주문이 동시에 들어올 경우의 처리
3. **타임아웃**: 각 단계별 타임아웃 설정 및 처리
4. **로봇 상태 관리**: 로봇의 실시간 상태 동기화
5. **데이터 일관성**: DB 트랜잭션 처리로 데이터 일관성 보장

## 메시지 인터페이스

### ROS2 토픽/서비스/액션
- **토픽**: `/roomie/status/robot_state`, `/roomie/status/task_state`, `/roomie/event/arrival`, `/roomie/event/pickup_completed`
- **액션**: `/roomie/action/perform_task`

### WebSocket 이벤트
- **SGUI**: `food_order_creation`, `food_pickup_arrival`
- **GGUI**: `delivery_completion`

### HTTP API
- **GGUI**: `get_food_menu`, `create_delivery_task`
- **SGUI**: `food_order_status_change` 