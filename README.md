# 호텔 실내 배송 로봇



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
│       └── bringup/                   # 통합 launch 파일 모음
│
├── esp32_firmware/                     # Micro-ROS 전용 ESP32 펌웨어 개발
│   ├── arm_unit/                      # Arm 서보 제어용 펌웨어
│   │   └── src/
│   └── io_controller/                 # 센서, 서랍, LED 제어
│       └── src/
│
├── gui/                               # GUI 애플리케이션들
│   ├── admin_gui/                     # 관리자용 GUI
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

