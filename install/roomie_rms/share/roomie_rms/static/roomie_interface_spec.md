# Roomie RMS Interface Specification

## 1. RMS ↔ RC

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
int32 

---
# Result
int32 robot_id
string message

---

# Feedback
(없음)
```

---

## 2. RMS ↔ SGUI

### WebSocket

#### 음식 주문 발생 이벤트
```json
{
  "type": "event",
  "action": "food_order_creation",
  "payload": {
    "task_id": "TASK_001",
    "request_location": "ROOM_307",
    "order_details": {
      "items": [
        {"name": "스파게티", "quantity": 2, "price": 15000},
        {"name": "피자", "quantity": 1, "price": 15000}
      ]
    }
  }
}
```

#### 음식 주문 상태 전환 요청/응답
```json
// 요청
{
  "type": "request",
  "action": "food_order_status_change",
  "payload": {"task_id": "TASK_001"}
}
// 응답
{
  "type": "response",
  "action": "food_order_status_change",
  "payload": {"task_id": "TASK_001", "status_changed": "food_ready"}
}
```

#### 음식 픽업 도착 이벤트
```json
{
  "type": "event",
  "action": "food_pickup_arrival",
  "payload": {"task_id": "TASK_001", "robot_id": "ROBOT_01"}
}
```

#### 비품 요청 이벤트
```json
{
  "type": "event",
  "action": "supply_order_creation",
  "payload": {
    "task_id": "TASK_002",
    "request_location": "ROOM_307",
    "request_details": {
      "items": [
        {"name": "타월", "quantity": 3},
        {"name": "생수", "quantity": 2}
      ]
    }
  }
}
```

#### 비품 픽업 도착 이벤트
```json
{
  "type": "event",
  "action": "supply_pickup_arrival",
  "payload": {"task_id": "TASK_002", "robot_id": "ROBOT_01"}
}
```

---

## 3. RMS ↔ AGUI

### HTTP

#### 작업 목록 요청/응답
```json
// 요청
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
// 응답
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
      }
    ]
  }
}
```

#### 작업 상세 요청/응답
```json
// 요청
{
  "type": "request",
  "action": "task_detail",
  "payload": {"task_id": "TASK_001"}
}
// 응답
{
  "type": "response",
  "action": "task_detail",
  "payload": {
    "robot_assignment_time": "2024-03-15T10:32:00Z",
    "pickup_completion_time": "2024-03-15T10:45:00Z"
  }
}
```

#### 로봇 목록 요청/응답
```json
// 요청
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
// 응답
{
  "type": "response",
  "action": "robot_list",
  "payload": {
    "robots": [
      {
        "robot_id": "ROBOT_01",
        "model_name": "ServiceBot_V2",
        "current_location": "LOB_1",
        "battery_level": 85,
        "task_status": "배송 중",
        "has_error": "N",
        "error_code": null
      }
    ]
  }
}
```

### WebSocket

#### 작업 상태 업데이트 이벤트
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

#### 로봇 상태 업데이트 이벤트
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

---

## 4. RMS ↔ GGUI

### WebSocket 이벤트

#### 호출 수락
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

#### 로봇 도착
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

#### 시간초과 복귀 알림
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
