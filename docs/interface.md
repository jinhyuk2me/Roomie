
From

To

프로토콜

인터페이스 항목

메시지 형식

 

Service
 

RC

RMS

Service 

길안내 작업 생성 요청

/roomie/command/create_task



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
location_id
0: LOB_WAITING

1: LOB_CALL

2: RES_PICKUP

3: RES_CALL

4: SUP_PICKUP

5: ELE_1

6: ELE_2

101: ROOM_101

Topic
 

RC

RMS

Topic

로봇 상태

/roomie/status/robot_state



# RobotState.msg
int32 robot_id
int32 task_id
int32 robot_state_id
robot_state_id (ERD 하고 일치해야 할 듯)
0: 작업 불가능

1: 작업 가능

2: 작업 입력 중

3: 작업 수행 중

4: 복귀 대기 중

5: 복귀 중

6: 작업 실패

7: 시스템 오류

RMS

RC

Topic

작업 상태

/roomie/status/task_state



# TaskState.msg
int32 task_id
int32 task_state_id
task_state_id (ERD 하고 일치해야 할 듯)
0: 접수됨

1: 준비 완료

2: 로봇 할당됨

3: 픽업 장소로 이동

4: 픽업 대기 중

5: 배송 중

6: 픽업 도착

7: 수령 완료

10: 호출 접수됨

11 : 호출 로봇 할당됨

12: 호출 이동 중

13: 호출 도착

20: 길안내 접수됨

21: 길안내 중

21: 길안내 도착

RC

RMS

Topic

장소 도착

/roomie/event/arrival



# Arrival.msg
int32 robot_id
int32 task_id
int32 location_id
 

RC

RMS

Topic

배터리 잔량

/roomie/status/battery_status



# BatteryStatus.msg
int32 robot_id
float32 charge_percentage
bool is_charging
 

RC

RMS

Topic

현재 로봇 위치와 방향

/roomie/status/roomie_pose



# RoomiePose.msg
int32 robot_id
int32 floor
geometry_msgs/Pose pose
 

RC

RMS

Topic 

픽업 완료

/roomie/event/pickup_completed



#PickupCompleted.msg
int32 robot_id
int32 task_id
builtin_interfaces/Time timestamp
 

RC

RMS

Topic

수령 완료

/roomie/event/delivery_completed



#DeliveryCompleted.msg
int32 robot_id
int32 task_id
builtin_interfaces/Time timestamp
 

Action
 

RMS

RC

Action

작업 할당

/roomie/action/perform_task



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
task_type_id
0: 음식배송

1: 비품배송

2: 호출

3: 길안내

task_status_id
0: 접수됨

1: 준비 완료

2: 로봇 할당됨

3: 픽업 장소로 이동

4: 픽업 대기 중

5: 배송 중

6: 픽업 도착

7: 수령 완료

10: 호출 이동 중

11 : 호출 도착

20: 길안내 중

21: 길안내 도착

location_id
0: LOB_1

1: LOB_2

2: RES_1

3: RES_2

4: SUP_1

5: ELE_1

6: ELE_2

101: ROOM_101

order_info


# 주문 정보
"{
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
}"
RMS

RC

Action

복귀

/roomie/action/perform_return



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
 

===


From

To

인터페이스 항목

메시지 형식

비고

ROS2 Service
 

Robot GUI 

RC

도어 잠금 해제 요청

/robot_gui/unlock_door       



# UnlockDoor.srv
# Request
int32 robot_id
int32 task_id
---
# Response
int32 robot_id
bool success
int32 reason
 

RC

Robot GUI      

출발 카운트다운

/robot_gui/start_departure_countdown



# StartCountdown.srv
# Request
int32 robot_id
int32 task_id
---
# Response
int32 robot_id
bool success
int32 reason
 

RC

Robot GUI      

복귀 카운트다운

/robot_gui/start_return_countdown



# ReturnCountdown.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool success
int32 reason
 

ROS2 Topic
 

RC

Robot GUI

로봇 GUI 이벤트 전송

/robot_gui/event



# RobotGuiEvent.msg
int32 robot_id
int32 rgui_event_id
int32 task_id
builtin_interfaces/Time timestamp
string detail
rgui_event_id
1: 엘리베이터 버튼 조작 시작

2: 엘리베이터 버튼 조작 종료

3: 엘리베이터 탑승 시작

4: 엘리베이터 탑승 종료

5: 엘리베이터 하차 시작

6: 엘리베이터 하차 종료

7: 호출 이동 시작

8: 호출 이동 종료

9: 호실 번호 인식 완료

detail



# 호실 번호
"101"
10: 길안내 이동 시작

11: 길안내 이동 종료

12: 픽업장소 이동 시작

13: 픽업장소 이동 종료

detail



# 주문 정보
"{
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
}"
14: 배송장소 이동 시작 

15: 배송장소 도착 완료

16: 서랍 열림

17: 서랍 닫힘

18: 서랍 잠금

19: 충전 시작

20: 충전 종료

21: 투숙객 이탈

22: 투숙객 이탈 후 재등록

23: 투숙객 등록

24: 배송 수령 완료

25: 배송 수령 미완료

Robot GUI

RC

로봇 GUI 이벤트 전송

/robot_gui/event



# RobotGuiEvent.msg
int32 robot_id
int32 rgui_event_id
int32 task_id
builtin_interfaces/Time timestamp
string detail
rgui_event_id
100: [수령 완료] 클릭

101: 목적지 입력 완료

detai



# 목적지 정보
"LOCATION_NAME"
102: 사용자 점유 상태

detail



“OCCUPIED”
or
“VACANT”
103: [카드키로 입력] 선택

104: [서랍 열기] 클릭

105: [적재 완료] 클릭

106: 인식모드 전환 요청

detail



“0”: 대기모드
“1”: 등록모드
“2”: 추적모드
“3”: 엘리베이터모드

===


From

To

프로토콜

인터페이스 항목

메시지 형식

비고

Service
 

RC 

VS         

ROS2 Service 

인식 모드 전환 요청

/roomie/command/set_vs_mode



# SetVSMode.srv
# Request
int32 robot_id
int32 mode_id
---
# Response
int32 robot_id
bool success
mode_id
0: 대기모드

1: 등록모드

2: 추적모드

3: 엘리베이터모드

RC

VS

ROS2 Service

엘리베이터 입구 너비 감지 요청

/roomie/command/elevator_width



# ElevatorWidth.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
float32 left_boundary
float32 right_boundary
 

RC

VS

ROS2 Service

버튼 상태 감지 요청

/roomie/command/button_status



# ButtonStatus.srv
# Request
int32 robot_id
int32[] button_ids
---
# Response
int32 robot_id
float32[] xs
float32[] ys
float32[] depths
bool[] is_pressed
builtin_interfaces/Time[] timestamp
button_id
100: 하행버튼 

101: 상행버튼

1: 1층

2: 2층

3: 3층

RC

VS

ROS2 Service

엘리베이터 위치 및 방향 감지 요청

/roomie/command/elevator_status



# ElevatorStatus.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
int32 direction
int32 position
direction
0: upward

1: downward

position
현재 층

RC

VS

ROS2 Service

문 열림 감지 요청

/roomie/command/door_status



# DoorStatus.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool door_opened
door_opened
0: closed

1: opened

RC

VS

ROS2 Service

엘리베이터 탑승/하차시 공간 확보 여부 감지 결과

/rommie/command/space_availability



# SpaceAvailability.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool space_availability
 

RC

VS

ROS2 Service

현재 위치 감지 결과

/roomie/command/location



# Location.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
int32 location_id
id

name

0

LOB_WAITING

1

LOB_CALL

2

RES_PICKUP

3

RES_CALL

4

SUP_PICKUP

5

ELE_1

6

ELE_2

101

ROOM_101

102

ROOM_102

201

ROOM_201

202

ROOM_202

Topic
 

VS

RC

ROS2 Topic   

추적 이벤트

/vs/tracking_event



# TrackingEvent.msg
int32 robot_id
int32 tracking_event_id
int32 task_id
builtin_interfaces/Time timestamp
tracking_event_id
0: slow_down

1: maintain

2: lost

3: resume

VS

RC

ROS2 Topic

추적 대상 등록됨

/vs/registered



# Registered.msg
int32 robot_id
builtin_interfaces/Time timestamp
 

====


From

To

프로토콜

인터페이스 항목

메시지 형식

 

Topic
 

RC

AGUI

Topic

배터리 잔량

/roomie/status/battery



# BatteryStatus.msg
int32 robot_id
float32 charge_percentage
bool is_charging
 

RC

AGUI

Topic

현재 로봇 위치와 방향

/roomie/status/roomie_pose



# RoomiePose.msg
int32 robot_id
int32 floor
geometry_msgs/Pose pose
 

 ===


From

To

인터페이스 항목

메시지 형식

설명

Service
RC

IOC

서랍 잠금 제어 요청

/ioc/control_lock



# ControlLock.srv
# Request
int32 robot_id
bool locked
---
# Response
int32 robot_id
bool success
command: 수행할 명령 
False : 열림

True: 잠금

RC

IOC

카드 인식 요청

/ioc/read_card_info



# ReadCardInfo.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool success
int32 location_id
 

RC

IOC

도어 열림 상태 확인

/ioc/check_door_state



# CheckDoorState.srv
# Request
int32 robot_id
---
# ResponseGetItemState
int32 robot_id
bool is_opened
is_opened
true : 열린 상태

false : 닫힌 상태

RC

IOC

물품 적재 여부 확인

/ioc/check_item_loaded



# CheckItemLoaded.srv
# Request
int32 robot_id
---
# Response
int32 robot_id
bool item_loaded
item_loaded
true : 물품이 감지된 상태

false :  없는 상태

Topic
RC

IOC

로봇 상태 이벤트 (LED 반영용)

/roomie/status/robot_state



# RobotState.msg
int32 robot_id
int32 robot_state_id
robot_status_id 
0: 작업 불가능

1: 작업 가능

2: 작업 입력 중

3: 작업 수행 중

4: 복귀 대기 중

5: 복귀 중

6: 작업 실패

7: 시스템 오류

 