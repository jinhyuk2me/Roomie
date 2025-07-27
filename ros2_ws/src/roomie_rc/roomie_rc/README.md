# Roomie RC (Robot Control) Module

로봇 제어 Python 모듈 - 서비스 로봇의 중심 제어 노드

## 📁 구조

- `rc_node.py` - 메인 로봇 제어 노드 (중심 허브)
- `rms_client.py` - RMS(Roomie Main Service) 통신 클라이언트
- `gui_client.py` - RGUI(Robot GUI) 통신 클라이언트  
- `vs_client.py` - VS(Vision Service) 통신 클라이언트
- `ioc_client.py` - IOC(IO Controller) 통신 클라이언트

## 🚀 주요 기능

### ✅ 구현 완료
- **RMS 통신**: 작업 할당, 상태 발행, 이벤트 처리
- **GUI 통신**: 서비스/토픽 양방향 통신, 사용자 인터랙션
- **하드웨어 통신**: VS(위치 감지), IOC(서랍/센서 제어)  
- **배송 프로세스**: 픽업/배송 스켈레톤 구현
- **상태 관리**: 로봇 상태 자동 전환

### 🔄 TODO
- 실제 내비게이션 연동
- 배송 작업 알고리즘 고도화
- 센서 실시간 모니터링

## 📡 통신 인터페이스

### RMS 통신
- **Action**: `/roomie/action/perform_task` (작업 할당 받기)
- **Publisher**: 로봇 상태, 배터리, 위치, 이벤트 발행
- **Subscriber**: 작업 상태 구독

### GUI 통신  
- **Topic**: `/robot_gui/event` (양방향 이벤트)
- **Service**: 카운트다운, 도어 잠금 해제

### 하드웨어 통신
- **VS**: 위치 감지 (`/vs/command/location`)
- **IOC**: 서랍 제어, 센서 확인

## 🏃 실행 방법

```bash
# 빌드
colcon build --packages-select roomie_rc

# 실행  
source install/setup.bash
ros2 run roomie_rc rc_node
``` 