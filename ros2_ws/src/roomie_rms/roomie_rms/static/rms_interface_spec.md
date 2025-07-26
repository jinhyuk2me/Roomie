# Roomie RMS Interface Specification

## 1. RMS ↔ RC (Robot Controller)

### 1.1 Service

#### 길안내 작업 생성 요청 (`/roomie/command/create_task`)
```srv
# CreateTask.srv

# Request
int32 robot_id
int32 target_location_id
---
# Response
int32 robot_id
int32 task_id
bool success
string message
```

#### 좌표 데이터 요청 (`/roomie/command/get_locations`)
```srv
# GetLocations.srv

# Request
int32 robot_id

---
# Response
int32 robot_id
bool success
int32[] location_ids
int32[] floor_ids
float32[] location_xs
float32[] location_ys
```

### 1.2 Topic

#### 로봇 상태 (`/roomie/status/robot_state`)
```msg
# RobotState.msg

int32 robot_id
int32 robot_state_id
```

#### 작업 상태 (`/roomie/status/task_state`)
```msg
# TaskState.msg

int32 task_id
int32 task_state_id
```

#### 장소 도착 (`/roomie/event/arrival`)
```msg
# Arrival.msg

int32 robot_id
int32 task_id
int32 location_id
```

#### 배터리 잔량 (`/roomie/status/battery_status`)
```msg
# BatteryStatus.msg

int32 robot_id
float32 charge_percentage
bool is_charging
```

#### 현재 로봇 위치와 방향 (`/roomie/status/roomie_pose`)
```msg
# RoomiePose.msg

int32 robot_id
int32 floor_id
geometry_msgs/Pose pose
```

#### 픽업 완료 (`/roomie/event/pickup_completed`)
```msg
#PickupCompleted.msg

int32 robot_id
int32 task_id
builtin_interfaces/Time timestamp
```

#### 수령 완료 (`/roomie/event/delivery_completed`)
```msg
#DeliveryCompleted.msg

int32 robot_id
int32 task_id
builtin_interfaces/Time timestamp
```

### 1.3 Action

#### 작업 할당 (`/roomie/action/perform_task`)
```action
# PerformTask.action

# Goal
int32 robot_id
int32 task_id
int32 task_type_id
int32 task_status_id
int32 target_location_id
int32 pickup_location_id
string order_info        # 주문 정보 (JSON)

---

# Result (RCS -> RMS 최종 결과)
int32 robot_id
int32 task_id
bool success
string message

---
# Feedback (RCS(수행중) -> RMS 진행 상황)
int32 robot_id
int32 task_id
int32 task_status_id
```

#### 복귀 (`/roomie/action/perform_return`)
```action
# PerformReturn.action

# Goal
int32 robot_id

---
# Result
int32 robot_id
string message

---

# Feedback
(없음)
```

---

## 2. RMS ↔ SGUI (Staff GUI)

### 2.1 공통 용어 정의

#### 음식 항목 (food)
- 0: 스파게티
- 1: 피자
- 2: 스테이크
- 3: 버거

#### 비품 항목 (supply)
- 0: 칫솔
- 1: 타월
- 2: 생수
- 3: 수저

### 2.2 WebSocket 이벤트 메시지

#### 음식 주문 발생 알림 (food_order_creation)
```json
{
  "type": "event",
  "action": "food_order_creation",
  "payload": {
    "task_id": "TASK_001",
    "location": "ROOM_307",
    "order_details": [
      {
        "name": "스파게티",
        "quantity": 2,
        "price": 15000
      },
      {
        "name": "피자",
        "quantity": 1,
        "price": 15000
      }
    ]
  }
}
```

#### 음식 주문 작업 상태 전환 요청 (food_order_status_change)

**요청**
```json
{
  "type": "request",
  "action": "food_order_status_change",
  "payload": {
    "task_id": "TASK_001"
  }
}
```

**응답**
```json
{
  "type": "response",
  "action": "food_order_status_change",
  "payload": {
    "task_id": "TASK_001",
    "status_changed": "food_ready"
  }
}
```

#### 음식 픽업 장소 도착 알림 (food_pickup_arrival)
```json
{
  "type": "event",
  "action": "food_pickup_arrival",
  "payload": {
    "task_id": "TASK_001",
    "robot_id": "ROBOT_01"
  }
}
```

#### 비품 요청 발생 알림 (supply_order_creation)
```json
{
  "type": "event",
  "action": "supply_order_creation",
  "payload": {
    "task_id": "TASK_002",
    "location": "ROOM_307",
    "order_details": [
      {
        "name": "타월",
        "quantity": 3
      },
      {
        "name": "생수",
        "quantity": 2
      }
    ]
  }
}
```

#### 비품 픽업 장소 도착 알림 (supply_pickup_arrival)
```json
{
  "type": "event",
  "action": "supply_pickup_arrival",
  "payload": {
    "task_id": "TASK_002",
    "robot_id": "ROBOT_01"
  }
}
```

---

## 3. RMS ↔ GGUI (Guest GUI)

### 3.1 기본 정보

메시지 공통 구조:
```json
{
  "type": "request" | "response" | "event",
  "action": "string",
  "payload": "object"
}
```

### 3.2 HTTP 동기 인터페이스

#### 호출 작업 생성 요청/응답
```json
// 요청
{
  "type": "request",
  "action": "create_call_task",
  "payload": {
    "location": "ROOM_201",
    "task_type": 2
  }
}

// 응답
{
  "type": "response",
  "action": "create_call_task",
  "payload": {
    "location_name": "ROOM_201",
    "task_name": "TASK_006",
    "success": true,
    "error_code": null,
    "error_message": null,
    "task_creation_time": "2025-07-22T16:42:16+09:00"
  }
}
```

#### 음식 메뉴 요청/응답
```json
// 요청
{
  "type": "request",
  "action": "get_food_menu",
  "payload": {
    "location_name": "ROOM_201"
  }
}

// 응답
{
  "type": "response",
  "action": "get_food_menu",
  "payload": {
    "food_items": [
      {
        "food_name": "스파게티",
        "price": 15000,
        "image": "/images/spaghetti.jpg"
      },
      {
        "food_name": "피자",
        "price": 25000,
        "image": "/images/pizza.jpg"
      }
    ]
  }
}
```

#### 비품 메뉴 요청/응답
```json
// 요청
{
  "type": "request",
  "action": "get_supply_menu",
  "payload": {
    "location_name": "ROOM_201"
  }
}

// 응답
{
  "type": "response",
  "action": "get_supply_menu",
  "payload": {
    "supply_items": [
      {
        "supply_name": "타월",
        "image": "/images/towel.jpg"
      },
      {
        "supply_name": "생수",
        "image": "/images/water.jpg"
      }
    ]
  }
}
```

#### 배송 작업 생성 요청/응답
```json
// 요청
{
  "type": "request",
  "action": "create_delivery_task",
  "payload": {
    "location_name": "ROOM_201",
    "task_type_name": "음식배송",
    "order_details": {
      "items": [
        {
          "name": "스파게티",
          "quantity": 2,
          "price": 15000
        },
        {
          "name": "피자",
          "quantity": 1,
          "price": 15000
        }
      ]
    }
  }
}

// 응답
{
  "type": "response",
  "action": "create_delivery_task",
  "payload": {
    "location_name": "ROOM_201",
    "task_name": "TASK_005",
    "success": true,
    "error_code": null,
    "error_message": null,
    "estimated_time": 55,
    "task_creation_time": "2025-07-22T16:42:16+09:00"
  }
}
```

#### 호출 내역 조회 요청/응답
```json
// 요청
{
  "type": "request",
  "action": "get_call_history",
  "payload": {
    "location_name": "ROOM_102",
    "task_name": "TASK_006"
  }
}

// 응답
{
  "type": "response",
  "action": "get_call_history",
  "payload": {
    "location_name": "ROOM_102",
    "task_name": "TASK_006",
    "task_type_name": "TASK_006",
    "estimated_time": 5,
    "robot_status": {
      "x": "float",
      "y": "float",
      "floor_id": "int"
    }
  }
}
```

#### 주문 내역 조회 요청/응답
```json
// 요청
{
  "type": "request",
  "action": "get_order_history",
  "payload": {
    "request_location": "ROOM_201",
    "task_name": "TASK_001",
    "task_type_name": "음식배송"
  }
}

// 응답
{
  "type": "response",
  "action": "get_order_history",
  "payload": {
    "request_location": "ROOM_201",
    "task_name": "TASK_001",
    "task_type_name": "음식배송",
    "estimated_time": 55,
    "task_creation_time": "2025-07-22T16:42:16+09:00",
    "robot_assignment_time": "2025-07-22T16:42:16+09:00",
    "pickup_completion_time": "2025-07-22T16:42:16+09:00",
    "delivery_arrival_time": null
  }
}
```

### 3.3 WebSocket 비동기 이벤트

#### 호출 수락 알림
```json
{
  "type": "event",
  "action": "call_request_acceptance",
  "payload": {
    "task_name": "TASK_006",
    "estimated_wait_time": 15
  }
}
```

#### 로봇 도착 완료 알림
```json
{
  "type": "event",
  "action": "robot_arrival_completion",
  "payload": {
    "task_name": "TASK_006",
    "location_name": "ROOM_102"
  }
}
```

#### 배송 완료 알림
```json
{
  "type": "event",
  "action": "delivery_completion",
  "payload": {
    "task_name": "TASK_001",
    "request_location": "ROOM_102"
  }
}
```

#### 시간 초과 복귀 알림
```json
{
  "type": "event",
  "action": "task_timeout_return",
  "payload": {
    "task_name": "TASK_006",
    "location_name": "ROOM_102"
  }
}
```

---

## 4. RMS ↔ AGUI (Admin GUI)

### 4.1 공통 용어 정의

#### Task Type (`task_type`)
- 0: 음식배송
- 1: 비품배송
- 2: 호출
- 3: 길안내

#### Task Status (`task_status`)
- 0: 접수됨
- 1: 준비 완료
- 2: 로봇 할당됨
- 3: 픽업 장소로 이동
- 4: 픽업 대기중
- 5: 배송 중
- 6: 배송 도착
- 7: 수령 완료
- 10: 호출 접수됨
- 11: 호출 로봇 할당됨
- 12: 호출 이동 중
- 13: 호출 도착
- 20: 길안내 접수됨
- 21: 길안내 중
- 22: 길안내 도착

#### Robot Status (`robot_status`)
- 0: 작업 불가능
- 1: 작업 가능
- 2: 작업 입력중
- 3: 작업 수행중
- 4: 복귀 대기중
- 5: 복귀 중
- 6: 작업 실패
- 7: 시스템 오류

#### Location
- 0: LOB_WAITING
- 1: LOB_CALL
- 2: RES_PICKUP
- 3: RES_CALL
- 4: SUP_PICKUP
- 5: ELE_1
- 6: ELE_2
- 101: ROOM_101
- 102: ROOM_102
- 201: ROOM_201
- 202: ROOM_202

### 4.2 HTTP 통신 인터페이스

#### 작업 목록 요청 (task_list)

**요청 메시지 (전체 조회)**
```json
{
  "type": "request",
  "action": "task_list",
  "payload": {
    "filters": {}
  }
}
```

**요청 메시지 (필터 적용)**
```json
{
  "type": "request",
  "action": "task_list",
  "payload": {
    "filters": {
      "start_date": "2024-01-01",
      "end_date": "2024-01-02",
      "task_type": "음식배송",
      "task_status": "수령 완료",
      "destination": "ROOM_102"
    }
  }
}
```

**응답 메시지 예시**
```json
{
  "type": "response",
  "action": "task_list",
  "payload": {
    "tasks": [
      {
        "task_id": "TASK_001",
        "task_type": "음식배송",
        "task_status": "수령 완료",
        "destination": "ROOM_202",
        "robot_id": "ROBOT_01",
        "task_creation_time": "2024-03-15T10:30:00Z",
        "task_completion_time": "2024-03-15T10:52:10Z"
      },
      {
        "task_id": "TASK_002",
        "task_type": "음식배송",
        "task_status": "픽업 대기중",
        "destination": "ROOM_102",
        "robot_id": "ROBOT_01",
        "task_creation_time": "2024-03-15T10:30:00Z",
        "task_completion_time": null
      }
    ]
  }
}
```

#### 작업 상세 요청 (task_detail)

**요청 메시지**
```json
{
  "type": "request",
  "action": "task_detail",
  "payload": {
    "task_id": "TASK_001"
  }
}
```

**응답 메시지**
```json
{
  "type": "response",
  "action": "task_detail",
  "payload": {
    "robot_assignment_time": "2024-03-15T10:32:00Z",
    "pickup_completion_time": "2024-03-15T10:45:00Z",
    "delivery_arrival_time": null,
    "task_completion_time": null
  }
}
```

#### 로봇 목록 요청 (robot_list)

**요청 메시지 (전체 조회)**
```json
{
  "type": "request",
  "action": "robot_list",
  "payload": {
    "filters": {}
  }
}
```

**요청 메시지 (필터 적용)**
```json
{
  "type": "request",
  "action": "robot_list",
  "payload": {
    "filters": {
      "robot_id": "ROBOT_001",
      "model_name": "ServiceBot_V2",
      "robot_status": "복귀 중"
    }
  }
}
```

**응답 메시지**
```json
{
  "type": "response",
  "action": "robot_list",
  "payload": {
    "robots": [
      {
        "robot_id": "ROBOT_01",
        "model_name": "ServiceBot_V2",
        "current_location": "LOB_WAITING",
        "battery_level": 85,
        "task_status": "배송 중",
        "has_error": "N",
        "error_code": null
      },
      {
        "robot_id": "ROBOT_02",
        "model_name": "ServiceBot_V1",
        "current_location": "LOB_CALL",
        "battery_level": 45,
        "task_status": "failed",
        "has_error": "Y",
        "error_code": "..."
      }
    ]
  }
}
```

### 4.3 WebSocket 이벤트

#### 작업 상태 업데이트 (task_status_update)
```json
{
  "type": "event",
  "action": "task_status_update",
  "payload": {
    "total_task_count": 25,
    "waiting_task_count": 3
  }
}
```

#### 로봇 상태 업데이트 (robot_status_update)
```json
{
  "type": "event",
  "action": "robot_status_update",
  "payload": {
    "total_robot_count": 5,
    "waiting_robot_count": 2
  }
}
```
