# 호텔 실내 배송 로봇



### 폴더 구조 

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
├── esp32_firmware/                 # Micro-ROS 전용 ESP32 펌웨어 개발 디렉토리
│   ├── arm_unit/                   # Arm 서보 제어용 펌웨어
│   │   └── src/
│   └── io_controller/              # 센서, 서랍, LED 제어
│       └── src/
├── gui/                                # TCP GUI 앱들 (비 ROS 영역)
│   ├── admin_gui/
│   ├── staff_gui/
│   └── guest_gui/
│
├── config/                             # 공통 설정 파일 (.yaml, .json 등)
│   └── robot_model_config.yaml
│
├── scripts/                            # 빌드 및 런치 자동화 스크립트
│   ├── build_all.sh
│   └── launch_all.sh
│
├── docker/                             # Docker 환경 구성 (선택)
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── simulation/                         # 시뮬레이션 환경 (Gazebo, RViz 등)
│   ├── gazebo_worlds/
│   └── rviz/
│       └── roomie_config.rviz
│
├── docs/                               # 설계 문서
│   ├── architecture/
│   ├── interface/
│   ├── user_requirements.md
│   ├── system_requirements.md
│   └── README.md
│
├── .gitignore
├── README.md
└── LICENSE

```

