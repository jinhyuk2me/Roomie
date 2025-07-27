# roomie_rms Module

## 1. 개요

### 1.1 목표
- 로봇 컨트롤러(RC)와 ROS2 통신을 통한 실시간 제어
- PyQt6 기반 데스크톱 GUI와 이중 통신 방식 제공:
  - **HTTP API**: 동기식 데이터 요청/응답 (설정, 조회, 명령)
  - **WebSocket**: 비동기식 실시간 이벤트 (상태, 알림, 스트리밍)
- MySQL 데이터베이스를 통한 데이터 관리 및 로그 저장
- 메인 서버를 통한 로봇 관리 시스템

### 1.2 주요 기능
- **ROS2 통신**: 로봇 컨트롤러와의 실시간 명령/상태 교환
- **이중 통신 방식**:
  - **HTTP API**: RESTful 방식의 동기식 데이터 처리
  - **WebSocket**: 실시간 이벤트 스트리밍
- **데이터베이스 연동**: 로봇, 작업, 위치, 주문 정보 관리
- **통합 데이터 관리**: 동기/비동기 데이터 흐름 통합 관리
- **모듈화된 아키텍처**: 관심사 분리를 통한 유지보수성 향상
- **통합 로깅 시스템**: 표준화된 로깅 및 에러 처리

## 2. 시스템 아키텍처

```
┌─────────────────┐   HTTP API       ┌─────────────────┐    ROS2      ┌─────────────────┐
│  Desktop GUI    │ ◄──────────────► │   RMS Node      │ ◄──────────► │ Robot Controller│
│   (PyQt6)       │                  │  (Hybrid)       │              │  (ROS2)         │
│                 │   WebSocket      │                 │              │                 │
│                 │ ◄──────────────► │ ┌─────────────┐ │              │                 │
└─────────────────┘                  │ │ FastAPI     │ │              └─────────────────┘
                                     │ │ Server      │ │
                                     │ └─────────────┘ │
                                     │ ┌─────────────┐ │
                                     │ │ ROS2 Node   │ │
                                     │ │ (rclpy)     │ │
                                     │ └─────────────┘ │
                                     └─────────────────┘
                                             │
                                             │ SQL  
                                             ▼
                                     ┌─────────────────┐
                                     │   MySQL DB      │
                                     └─────────────────┘
```

🔄 데이터 흐름:
- GUI → HTTP → RMS Node (FastAPI) → 내부 처리 → RMS Node (ROS2) → Topics → Robot Controller
- Robot Controller → Topics → RMS Node (ROS2) → 내부 처리 → RMS Node (FastAPI) → WebSocket → GUI

## 3. 기술 스택

### 3.1 메인 서버 (Backend)
- **언어**: Python 3.12
- **웹 프레임워크**: FastAPI (HTTP + WebSocket 통합 지원)
- **ASGI 서버**: uvicorn
- **비동기 처리**: asyncio
- **ROS2 클라이언트**: rclpy
- **데이터베이스**: MySQL 8.0 + mysql-connector-python

### 3.2 GUI 애플리케이션 (Frontend)
- **언어**: Python 3.12
- **GUI 프레임워크**: PyQt6
- **HTTP 클라이언트**: QNetworkAccessManager
- **WebSocket 클라이언트**: QWebSocket

### 3.3 로봇 컨트롤러
- **ROS2 Distribution**: Jazzy Jalopy
- **통신 방식**: Topics, Services, Actions

## 4. 시스템 구성 요소

### 4.1 Roomie Main Server(RMS) 모듈

```
roomie_rms/
└── roomie_rms/
    ├── __init__.py
    ├── rms_node.py              # ROS2 Node 진입점
    │
    ├── ros_core/                # ROS2 핵심 로직
    │   ├── base_node.py         # 기본 ROS2 노드 설정
    │   ├── handlers/            # ROS2 인터페이스 핸들러
    │   │   ├── action_handler.py    # Action 클라이언트 처리
    │   │   ├── service_handler.py   # Service 서버 콜백
    │   │   └── topic_handler.py     # Topic 퍼블리셔/서브스크라이버
    │   └── business/            # 비즈니스 로직 매니저
    │       ├── task_manager.py      # 작업 할당 및 관리
    │       └── robot_manager.py     # 로봇 상태 관리
    │
    ├── app/                     # FastAPI Server
    │   ├── __init__.py
    │   ├── main.py              # FastAPI 앱 생성 및 매니저 라우터 포함
    │   ├── config.py            # 설정 관리
    │   │
    │   ├── services/            # 통합 서비스 매니저
    │   │   ├── __init__.py
    │   │   ├── http_manager.py      # HTTP API 통합 관리
    │   │   ├── websocket_manager.py # WebSocket 통합 관리
    │   │   └── db_manager.py        # 데이터베이스 관리자
    │   │
    │   ├── schemas/             # 데이터 모델 (Pydantic)
    │   │   ├── __init__.py
    │   │   ├── rc_models.py     # 로봇 컨트롤러 데이터 모델 (ROS2 msgs 구조)
    │   │   └── gui_models.py    # GUI 데이터 모델 (요청-응답 json 구조)
    │   │
    │   └── utils/               # 기타 유틸리티
    │       ├── __init__.py
    │       ├── logger.py        # 통합 로깅 시스템
    │       ├── exceptions.py    # 커스텀 예외 클래스
    │       └── error_handler.py # 에러 처리 데코레이터 및 컨텍스트 매니저
    │
    ├── testing/                 # 테스트 도구
    │   ├── __init__.py
    │   ├── sgui_app.py          # Staff GUI 애플리케이션
    │   ├── ggui_app.py          # Guest GUI 애플리케이션
    │   └── rc_gui.py            # RC 시뮬레이터 (GUI + ROS2 Node 통합)
    │
    ├── logs/                    # 로그 파일 저장소
    │   └── roomie_rms_*.log     # 애플리케이션 로그 (세션별로 생성)
    │
    └── static/                  # 정적 파일
        ├── images/              # 이미지 파일
        │   ├── food/            # 음식 이미지
        │   └── supply/          # 물품 이미지
        └── sql/                 # 데이터베이스 스키마 및 초기 데이터
            ├── roomie_db_tables.sql  # 테이블 스키마
            └── roomie_db_data.sql    # 초기 데이터
```

## 5. 핵심 구현 기능

### 5.1 🆕 통합 서비스 매니저 아키텍처
- **`services/http_manager.py`**: 모든 HTTP API 엔드포인트를 클래스 기반으로 통합 관리
  - `HttpManager` 클래스: FastAPI 라우터를 내장하여 모든 HTTP API 처리
  - 음식/물품 메뉴, 위치 조회, 작업 생성/변경, 작업/로봇 목록 관리
  - 의존성 주입 함수 포함

- **`services/websocket_manager.py`**: WebSocket 통신을 클래스 기반으로 통합 관리
  - `WebSocketManager` 클래스: 연결 관리, 메시지 브로드캐스트, FastAPI 라우터 내장
  - 게스트/스태프/관리자별 WebSocket 엔드포인트 제공
  - 실시간 이벤트 전송 및 연결 상태 관리

- **기존 `routers/` 폴더 제거**: 모든 라우터 로직이 각 매니저 내부로 통합

### 5.2 모듈화된 아키텍처
- **기존**: 단일 `rms_node.py` 파일 (631라인)에 모든 로직 집중
- **개선**: 관심사 분리를 통한 모듈화
  - `ros_core/`: ROS2 관련 핵심 로직
  - `handlers/`: ROS2 인터페이스별 처리 로직
  - `business/`: 비즈니스 로직 분리
  - `services/`: 통신 프로토콜별 매니저 분리

### 5.3 통합 로깅 시스템
- **표준화된 로깅**: 모든 모듈에서 일관된 로그 포맷
- **파일 로깅**: 로테이션 기능을 포함한 파일 저장
- **로그 레벨 관리**: 환경변수 기반 로그 레벨 설정
- **이모지 제거**: 깔끔한 로그 메시지 (로그 레벨 중복 표시 제거)

### 5.4 에러 처리 표준화
- **커스텀 예외**: 계층적 예외 클래스 구조
- **데코레이터 기반 처리**: 반복적인 에러 처리 로직 자동화
- **컨텍스트 매니저**: 데이터베이스 트랜잭션 안전성 보장

### 5.5 의존성 주입
- **매니저 인스턴스 주입**: 핸들러들이 필요한 매니저를 생성자에서 받음
- **내부 의존성 주입**: 각 매니저 클래스 내부에서 RMS 노드 참조 관리

## 6. 실행 방법

### 6.1 환경 설정
```bash
# 1. ROS2 환경 활성화
source /home/jay/project_ws/ros-repo-2/ros2_ws/install/setup.bash

# 2. Python 가상환경 활성화
source /home/jay/venv/roomie_venv/bin/activate
```

### 6.2 메인 시스템 실행
```bash
# RMS 노드 실행 (FastAPI + ROS2)
cd /home/jay/project_ws/ros-repo-2/ros2_ws/src/roomie_rms/roomie_rms
python rms_node.py
```

### 6.3 테스트 도구 실행

#### 6.3.1 RC 시뮬레이터
```bash
# RC 시뮬레이터 실행 (ROS2 환경 필요)
cd /home/jay/project_ws/ros-repo-2/ros2_ws/src/roomie_rms/roomie_rms
python testing/rc_gui.py
```

#### 6.3.2 Staff GUI (SGUI)
```bash
# Staff GUI 실행 (ROS2 환경 불필요)
cd /home/jay/project_ws/ros-repo-2/ros2_ws/src/roomie_rms/roomie_rms
python testing/sgui_app.py
```

#### 6.3.3 Guest GUI (GGUI)
```bash
# Guest GUI 실행 (ROS2 환경 불필요)
cd /home/jay/project_ws/ros-repo-2/ros2_ws/src/roomie_rms/roomie_rms
python testing/ggui_app.py
```

## 7. 개발 환경

### 7.1 필요 패키지
- **ROS2**: `roomie_msgs` (커스텀 메시지 패키지)
- **Python**: `fastapi`, `uvicorn`, `PyQt6`, `mysql-connector-python`, `rclpy`
- **데이터베이스**: MySQL 8.0

### 7.2 로그 설정
- **로그 파일**: `logs/roomie_rms_YYYYMMDD_HHMMSS.log`
- **로그 레벨**: 환경변수 `LOG_LEVEL` 또는 `settings.LOG_LEVEL`
- **로그 로테이션**: 10MB 단위, 최대 5개 백업 파일

### 7.3 데이터베이스 설정
- **자동 생성**: 데이터베이스가 없으면 자동으로 생성
- **스키마 초기화**: `static/sql/roomie_db_tables.sql`에서 테이블 생성
- **초기 데이터**: `static/sql/roomie_db_data.sql`에서 기본 데이터 삽입

## 8. API 엔드포인트

### 8.1 HTTP API (`/api/gui/`)
- `POST /api/gui/get_food_menu`: 음식 메뉴 조회
- `POST /api/gui/get_supply_menu`: 물품 메뉴 조회
- `POST /api/gui/get_locations`: 위치 목록 조회
- `POST /api/gui/create_delivery_task`: 배송 작업 생성
- `POST /api/gui/change_task_status`: 작업 상태 변경
- `GET /api/gui/get_tasks`: 작업 목록 조회 (필터링 지원)
- `GET /api/gui/get_robots`: 로봇 목록 조회 (필터링 지원)

### 8.2 WebSocket (`/api/gui/ws/`)
- `/api/gui/ws/guest/{location_name}`: 게스트용 실시간 이벤트
- `/api/gui/ws/staff/{staff_id}`: 스태프용 실시간 이벤트
- `/api/gui/ws/admin/{admin_id}`: 관리자용 실시간 이벤트

### 8.3 정적 파일
- `/images/`: 음식 및 물품 이미지 제공

## 9. 데이터베이스 구조
- **robot**: 로봇 정보
- **task**: 작업 정보
- **location**: 위치 정보
- **order**: 주문 정보
- **food_order_item**: 음식 주문 상세 정보
- **supply_order_item**: 물품 주문 상세 정보
- **food**: 음식 메뉴
- **supply**: 물품 메뉴
- **task_type**: 작업 유형
- **task_status**: 작업 상태
