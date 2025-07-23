# RMS-RGUI Interface Specification

## 1. Service Interfaces

### 1.1 도어 잠금 해제 요청
- **From**: Robot GUI → RC
- **Protocol**: ROS2 Service
- **Topic**: `/robot_gui/unlock_door`

```srv
# UnlockDoor.srv
# Request
int32 robot_id
int32 task_id
---
# Response
int32 robot_id
bool success
int32 reason
```

---

### 1.2 출발 카운트다운
- **From**: RC → Robot GUI
- **Protocol**: ROS2 Service
- **Topic**: `/robot_gui/start_countdown`

```srv
# StartCountdown.srv
# Request
int32 robot_id
int32 task_id
int32 task_type_id
---
# Response
int32 robot_id
bool success
int32 reason
```

**task_type_id 값:**
- `0`: 음식배송
- `1`: 비품배송
- `2`: 호출
- `3`: 길안내

---

### 1.3 복귀 카운트다운
- **From**: RC → Robot GUI
- **Protocol**: ROS2 Service
- **Topic**: `/robot_gui/start_return_countdown`

```srv
# ReturnCountdown.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool success
int32 reason
```

---

## 2. Topic Interfaces

### 2.1 로봇 GUI 이벤트 전송 (RC → Robot GUI)
- **From**: RC → Robot GUI
- **Protocol**: ROS2 Topic
- **Topic**: `/robot_gui/event`

```msg
# RobotGuiEvent.msg
int32 robot_id
int32 rgui_event_id
int32 task_id
builtin_interfaces/Time timestamp
string detail
```

**rgui_event_id 값 (RC → Robot GUI):**

**엘리베이터 관련:**
- `1`: 엘리베이터 버튼 조작 시작
- `2`: 엘리베이터 버튼 조작 종료
- `3`: 엘리베이터 탑승 시작
- `4`: 엘리베이터 탑승 종료
- `5`: 엘리베이터 하차 시작
- `6`: 엘리베이터 하차 종료

**이동 관련:**
- `7`: 호출 이동 시작
- `8`: 호출 이동 종료
- `10`: 길안내 이동 시작
- `11`: 길안내 이동 종료
- `12`: 픽업장소 이동 시작
- `13`: 픽업장소 이동 종료
- `14`: 배송장소 이동 시작
- `15`: 배송장소 도착 완료

**인식 및 상태:**
- `9`: 호실 번호 인식 완료
  - **detail**: 호실 번호 (예: `"101"`)

**서랍 관련:**
- `16`: 서랍 열림
- `17`: 서랍 닫힘
- `18`: 서랍 잠금

**충전 관련:**
- `19`: 충전 시작
- `20`: 충전 종료

**사용자 관련:**
- `21`: 투숙객 이탈
- `22`: 투숙객 이탈 후 재등록
- `23`: 투숙객 등록

**배송 관련:**
- `24`: 배송 수령 완료
- `25`: 배송 수령 미완료

**detail 예시 (픽업장소 이동 종료 시):**
```json
{
    "items": [
      {
        "name": "스파게티",
        "quantity": 2
      },
      {
        "name": "피자",
        "quantity": 1
      }
    ]
}
```

---

### 2.2 로봇 GUI 이벤트 전송 (Robot GUI → RC)
- **From**: Robot GUI → RC
- **Protocol**: ROS2 Topic
- **Topic**: `/robot_gui/event`

```msg
# RobotGuiEvent.msg
int32 robot_id
int32 rgui_event_id
int32 task_id
builtin_interfaces/Time timestamp
string detail
```

**rgui_event_id 값 (Robot GUI → RC):**

**사용자 입력:**
- `100`: [수령 완료] 클릭
- `101`: 목적지 입력 완료
  - **detail**: 목적지 정보 (예: `"LOCATION_NAME"`)
- `103`: [카드키로 입력] 선택
- `104`: [서랍 열기] 클릭
- `105`: [적재 완료] 클릭

**상태 관련:**
- `102`: 사용자 점유 상태
  - **detail**: `"OCCUPIED"` 또는 `"VACANT"`

**모드 제어:**
- `106`: 인식모드 전환 요청
  - **detail**: 모드 값
    - `"0"`: 대기모드
    - `"1"`: 등록모드
    - `"2"`: 추적모드
    - `"3"`: 엘리베이터모드

---

## 3. 메시지 파일 위치

모든 서비스 및 메시지 정의는 `roomie_msgs` 패키지에 정의되어 있습니다:

- **Services**: 
  - `roomie_msgs/srv/task_management/StartCountdown.srv`
  - `roomie_msgs/srv/task_management/ReturnCountdown.srv`
  - `roomie_msgs/srv/security/ControlLock.srv` (UnlockDoor)
- **Messages**: 
  - `roomie_msgs/msg/user_interface/RobotGuiEvent.msg`
