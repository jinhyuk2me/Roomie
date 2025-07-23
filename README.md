# 호텔 실내 배송 로봇 Roomie


### 프로젝트 구조

```
Roomie/
├── ros2_ws/                            # ROS2 공통 워크스페이스
│   ├── build/                          # colcon build 시 자동 생성
│   ├── install/
│   ├── log/
│   └── src/
│       ├── roomie_msgs/               # 공용 메시지 (msg/srv/action 정의)
│       ├── roomie_rc/                 # 로봇 제어 노드 (RC)
│       ├── roomie_rgui/               # 로봇 GUI 노드 (RGUI)
│       ├── roomie_vs/                 # Vision Service 노드 (VS)
│       ├── roomie_rms/                # Main Server 노드 (RMS)
│       ├── roomie_agui/               # 관리자 GUI 노드 (Admin GUI)
│       └── bringup/                   # 통합 launch 파일 모음
│
├── esp32_firmware/                     # Micro-ROS 전용 ESP32 펌웨어 개발
│   ├── arm_unit/                      # Arm 서보 제어용 펌웨어
│   │   └── src/
│   └── io_controller/                 # 센서, 서랍, LED 제어
│       └── src/
│
├── gui/                               # GUI 애플리케이션들 (비 ROS)
│   ├── staff_gui/                     # 직원용 GUI
│   └── guest_gui/                     # 투숙객용 GUI
│
├── assets/                            # 이미지 및 리소스 파일
│   └── images/
│
├── docs/                              # 설계 문서
│   ├── architecture/                  # 시스템 아키텍처
│   ├── interface.md                   # 통신 인터페이스 정의
│   └── state_diagram/                 # 상태 다이어그램
│
├── .gitignore
├── README.md
└── LICENSE
```

### 개발 시작하기

1. **ROS2 환경 설정**
   ```bash
   cd ros2_ws
   colcon build
   source install/setup.bash
   ```

2. **메시지 확인**
   ```bash
   ros2 interface list | grep roomie
   ```

### 패키지 설명

- **roomie_msgs**: 시스템 전체에서 사용하는 메시지, 서비스, 액션 정의
- **roomie_rc**: 로봇 제어 및 내비게이션
- **roomie_rms**: 메인 서버 (태스크 관리, 데이터베이스)
- **roomie_vs**: 비전 서비스 (객체 감지, 추적)
- **roomie_rgui**: 로봇 탑재 GUI
- **roomie_agui**: 관리자 GUI (ROS2 토픽 구독)

