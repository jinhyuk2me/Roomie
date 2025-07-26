# Vision Service Interface Specification

## 1. Service Interfaces

### 1.1 인식 모드 전환 요청
- **From**: RC → VS
- **Protocol**: ROS2 Service
- **Topic**: `/vs/command/set_vs_mode`

```srv
# SetVSMode.srv
# Request
int32 robot_id
int32 mode_id
---
# Response
int32 robot_id
bool success
```

**mode_id 값:**
- **후방 카메라 모드**
  - `0`: 대기모드
  - `1`: 등록모드
  - `2`: 추적모드
- **전방 카메라 모드**
  - `3`: 엘리베이터 외부 모드
  - `4`: 엘리베이터 내부 모드
  - `5`: 일반모드

---

### 1.2 엘리베이터 입구 너비 감지 요청
- **From**: RC → VS
- **Protocol**: ROS2 Service
- **Topic**: `/vs/command/elevator_width`

```srv
# ElevatorWidth.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool success
float32 left_boundary
float32 right_boundary
```

---

### 1.3 버튼 상태 감지 요청
- **From**: RC → VS
- **Protocol**: ROS2 Service
- **Topic**: `/vs/command/button_status`

```srv
# ButtonStatus.srv
# Request
int32 robot_id
int32[] button_ids
---
# Response
int32 robot_id
bool success
float32[] xs
float32[] ys
float32[] depths
bool[] is_pressed
builtin_interfaces/Time[] timestamp
```

**button_id 값:**
- `1`: 1층
- `2`: 2층
- `3`: 3층
- `4`: 4층
- `5`: 5층
- `6`: 6층
- `7`: 7층
- `8`: 8층
- `9`: 9층
- `10`: 10층
- `11`: 11층
- `12`: 12층
- `100`: 하행버튼
- `101`: 상행버튼
- `102`: 열기버튼
- `103`: 닫기버튼

---

### 1.4 엘리베이터 위치 및 방향 감지 요청
- **From**: RC → VS
- **Protocol**: ROS2 Service
- **Topic**: `/vs/command/elevator_status`

```srv
# ElevatorStatus.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool success
int32 direction
int32 position
```

**direction 값:**
- `0`: upward
- `1`: downward

**position 값:**
- 현재 층 번호

---

### 1.5 문 열림 감지 요청
- **From**: RC → VS
- **Protocol**: ROS2 Service
- **Topic**: `/vs/command/door_status`

```srv
# DoorStatus.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool success
bool door_opened
```

**door_opened 값:**
- `false (0)`: closed
- `true (1)`: opened

---

### 1.6 엘리베이터 탑승/하차시 공간 확보 여부 감지
- **From**: RC → VS
- **Protocol**: ROS2 Service
- **Topic**: `/vs/command/space_availability`

```srv
# SpaceAvailability.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool success
bool space_availability
```

---

### 1.7 현재 위치 감지 결과
- **From**: RC → VS
- **Protocol**: ROS2 Service
- **Topic**: `/vs/command/location`

```srv
# Location.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool success
int32 location_id
```

**location_id 값:**
- `0`: LOB_WAITING
- `1`: LOB_CALL
- `2`: RES_PICKUP
- `3`: RES_CALL
- `4`: SUP_PICKUP
- `5`: ELE_1
- `6`: ELE_2
- `101`: ROOM_101
- `102`: ROOM_102
- `201`: ROOM_201
- `202`: ROOM_202

---

## 2. Topic Interfaces

### 2.1 추적 이벤트
- **From**: VS → RC
- **Protocol**: ROS2 Topic
- **Topic**: `/vs/tracking_event`

```msg
# TrackingEvent.msg
int32 robot_id
int32 tracking_event_id
int32 task_id
builtin_interfaces/Time timestamp
```

**tracking_event_id 값:**
- `0`: slow_down
- `1`: maintain
- `2`: lost
- `3`: resume

---

### 2.2 추적 대상 등록됨
- **From**: VS → RC
- **Protocol**: ROS2 Topic
- **Topic**: `/vs/registered`

```msg
# Registered.msg
int32 robot_id
builtin_interfaces/Time timestamp
```

---

## 3. 메시지 파일 위치

모든 서비스 및 메시지 정의는 `roomie_msgs` 패키지에 정의되어 있습니다:

- **Services**: `roomie_msgs/srv/`
- **Messages**: `roomie_msgs/msg/`
- **Actions**: `roomie_msgs/action/`
 

