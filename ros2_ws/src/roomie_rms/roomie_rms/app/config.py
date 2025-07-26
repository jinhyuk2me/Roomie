"""
Roomie RMS 설정 관리 모듈

이 모듈은 애플리케이션의 모든 설정을 중앙집중식으로 관리합니다:
- API 엔드포인트
- ROS2 인터페이스 이름
- 데이터베이스 설정 
- 로깅 설정
- 애플리케이션 상수
"""

from pydantic_settings import BaseSettings
from typing import Dict, Optional

# API 엔드포인트 경로를 관리하는 클래스
class ApiEndpoints:
    GET_FOOD_MENU = "/get_food_menu"
    GET_SUPPLY_MENU = "/get_supply_menu"
    CREATE_DELIVERY_TASK = "/create_delivery_task"
    CHANGE_TASK_STATUS = "/change_task_status"
    GET_TASKS = "/tasks"
    GET_ROBOTS = "/robots"
    WS_GUEST = "/ws/guest/{location_name}"
    WS_STAFF = "/ws/staff/{staff_id}"
    WS_ADMIN = "/ws/admin/{admin_id}"

# ROS2 인터페이스 이름(토픽, 서비스, 액션)을 관리하는 클래스
class ROSInterfaces:
    # Services
    GET_LOCATIONS_SERVICE = "/roomie/command/get_locations"
    CREATE_TASK_SERVICE = "/roomie/command/create_task"
    # Actions
    PERFORM_TASK_ACTION = "/roomie/action/perform_task"
    PERFORM_RETURN_ACTION = "/roomie/action/perform_return"
    # Publishers
    TASK_STATE_TOPIC = "/roomie/status/task_state"
    # Subscribers
    ROBOT_STATE_TOPIC = "/roomie/status/robot_state"
    ARRIVAL_TOPIC = "/roomie/event/arrival"
    BATTERY_STATUS_TOPIC = "/roomie/status/battery_status"
    ROOMIE_POSE_TOPIC = "/roomie/status/roomie_pose"
    PICKUP_COMPLETED_TOPIC = "/roomie/event/pickup_completed"
    DELIVERY_COMPLETED_TOPIC = "/roomie/event/delivery_completed"

# 데이터베이스에서 동적으로 로드될 상수를 저장하는 클래스
class DatabaseConstants:
    """
    애플리케이션 시작 시 DB에서 로드되는 상수 값을 저장합니다.
    (예: 'name' -> 'id' 매핑)
    """
    task_status: Dict[str, int] = {}
    robot_status: Dict[str, int] = {}
    task_type: Dict[str, int] = {}
    location: Dict[str, int] = {}

# 애플리케이션에서 사용되는 정적 상수 값을 관리하는 클래스
class AppConstants:
    """
    DB에 저장되지 않는 순수 애플리케이션 레벨의 상수.
    """
    # Task & Location Names (DB의 name과 일치해야 하는 핵심 문자열)
    TASK_TYPE_FOOD_DELIVERY: str = "음식배송"
    TASK_TYPE_SUPPLY_DELIVERY: str = "비품배송"
    TASK_TYPE_CALL: str = "호출"
    TASK_TYPE_GUIDANCE: str = "길안내"
    
    # Task Status Names (DB의 name과 일치)
    TASK_STATUS_RECEIVED: str = "접수됨"
    TASK_STATUS_READY: str = "준비 완료"
    TASK_STATUS_ROBOT_ASSIGNED: str = "로봇 할당됨"
    TASK_STATUS_MOVING_TO_PICKUP: str = "픽업 장소로 이동"
    TASK_STATUS_WAITING_FOR_PICKUP: str = "픽업 대기 중"
    TASK_STATUS_DELIVERING: str = "배송 중"
    TASK_STATUS_DELIVERY_ARRIVED: str = "배송 도착"
    TASK_STATUS_COMPLETED: str = "수령 완료"
    TASK_STATUS_CALL_RECEIVED: str = "호출 접수됨"
    TASK_STATUS_CALL_ROBOT_ASSIGNED: str = "호출 로봇 할당됨"
    TASK_STATUS_CALL_MOVING: str = "호출 이동 중"
    TASK_STATUS_CALL_ARRIVED: str = "호출 도착"
    TASK_STATUS_GUIDANCE_RECEIVED: str = "길안내 접수됨"
    TASK_STATUS_GUIDANCE_IN_PROGRESS: str = "길안내 중"
    TASK_STATUS_GUIDANCE_ARRIVED: str = "길안내 도착"
    
    # Location Names (DB의 name과 일치)
    LOCATION_LOB_WAITING: str = "LOB_WAITING"
    LOCATION_LOB_CALL: str = "LOB_CALL"
    LOCATION_RES_PICKUP: str = "RES_PICKUP"
    LOCATION_RES_CALL: str = "RES_CALL"
    LOCATION_SUP_PICKUP: str = "SUP_PICKUP"
    LOCATION_ELE_1: str = "ELE_1"
    LOCATION_ELE_2: str = "ELE_2"
    LOCATION_ROOM_101: str = "ROOM_101"
    LOCATION_ROOM_102: str = "ROOM_102"
    LOCATION_ROOM_201: str = "ROOM_201"
    LOCATION_ROOM_202: str = "ROOM_202"
    
    # Food Items (DB의 name과 일치)
    FOOD_SPAGHETTI: str = "스파게티"
    FOOD_PIZZA: str = "피자"
    FOOD_STEAK: str = "스테이크"
    FOOD_BURGER: str = "버거"
    
    # Supply Items (DB의 name과 일치)
    SUPPLY_TOOTHBRUSH: str = "칫솔"
    SUPPLY_TOWEL: str = "타월"
    SUPPLY_WATER: str = "생수"
    SUPPLY_SPOON: str = "수저"
    
    # Robot Status Names (DB의 name과 일치)
    ROBOT_STATUS_UNAVAILABLE: str = "작업 불가능"
    ROBOT_STATUS_AVAILABLE: str = "작업 가능"
    ROBOT_STATUS_INPUTTING: str = "작업 입력 중"
    ROBOT_STATUS_WORKING: str = "작업 수행 중"
    ROBOT_STATUS_WAITING_RETURN: str = "복귀 대기 중"
    ROBOT_STATUS_RETURNING: str = "복귀 중"
    ROBOT_STATUS_FAILED: str = "작업 실패"
    ROBOT_STATUS_ERROR: str = "시스템 오류"
    
    LOCATION_NAME_FOOD_PICKUP: str = "RES_PICKUP"
    LOCATION_NAME_SUPPLY_PICKUP: str = "SUP_PICKUP"
    
    # Defaults
    DEFAULT_ESTIMATED_TIME_MINUTES: int = 30
    # Timeouts
    SERVICE_TIMEOUT_SEC: float = 1.0
    ACTION_TIMEOUT_SEC: float = 1.0


class Settings(BaseSettings):
    """
    애플리케이션 메인 설정 클래스
    환경변수나 .env 파일에서 값을 로드할 수 있습니다.
    """
    
    # 데이터베이스 설정
    DB_HOST: str = "localhost"
    DB_USER: str = "root"
    DB_PASSWORD: str = "1234"
    DB_NAME: str = "roomie_db"
    DB_POOL_NAME: str = "roomie_pool"
    DB_POOL_SIZE: int = 5

    # FastAPI 서버 설정
    FASTAPI_HOST: str = "0.0.0.0"
    FASTAPI_PORT: int = 8000

    # 로그 설정
    LOG_DIR: str = "logs"
    LOG_FILE: str = "roomie_rms.log"
    LOG_LEVEL: str = "INFO"
    LOG_MAX_BYTES: int = 10 * 1024 * 1024  # 10 MB
    LOG_BACKUP_COUNT: int = 5

    # SQL 파일 경로
    DB_SCHEMA_PATH: str = "static/sql/roomie_db_tables.sql"
    DB_DATA_PATH: str = "static/sql/roomie_db_data.sql"
    
    # 클래스로 분리된 설정들을 포함
    api: ApiEndpoints = ApiEndpoints()
    ros: ROSInterfaces = ROSInterfaces()
    const: AppConstants = AppConstants()
    db_consts: DatabaseConstants = DatabaseConstants()  # DB에서 로드될 상수를 위한 공간
    
    class Config:
        """Pydantic 설정"""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# 설정 객체 생성
settings = Settings()
