import logging
import sys
from datetime import datetime
from typing import Optional, Dict, Any
from enum import Enum
import os
from logging.handlers import RotatingFileHandler
from app.config import settings

def datetime_to_ros_time(dt: datetime):
    """Python datetime을 ROS2 builtin_interfaces/Time으로 변환"""
    timestamp = dt.timestamp()
    sec = int(timestamp)
    nanosec = int((timestamp - sec) * 1e9)
    
    # ROS2 Time 구조 반환 (실제로는 builtin_interfaces.msg.Time 객체여야 함)
    return {
        'sec': sec,
        'nanosec': nanosec
    }

def ros_time_to_datetime(ros_time) -> datetime:
    """ROS2 builtin_interfaces/Time을 Python datetime으로 변환"""
    timestamp = ros_time.sec + ros_time.nanosec / 1e9
    return datetime.fromtimestamp(timestamp)

class LogLevel(Enum):
    """로그 레벨 열거형"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class RoomieLogger:
    """
    Roomie RMS 전용 로깅 시스템
    - 통일된 로그 포맷
    - 환경별 로그 레벨 설정
    - 구조화된 로깅 메시지
    - 노드 실행별 로그 파일 분리
    """
    
    _instance = None
    _logger = None
    _session_start_time = None
    _log_methods = ['info', 'debug', 'warning', 'error', 'critical']

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._logger is None:
            self._session_start_time = datetime.now()
            self._setup_logger()
            self._wrap_log_methods()
            self._log_session_start() # 세션 시작 로그 분리
    
    def _wrap_log_methods(self):
        """로거의 기본 메서드(info, debug 등)를 래핑하여 extra 파라미터를 쉽게 사용하고, 올바른 소스 파일 정보를 로깅하도록 함"""
        for method_name in self._log_methods:
            original_method = getattr(self._logger, method_name)

            def make_wrapper(method):
                def wrapper(msg, *args, category: str = 'GENERAL', subcategory: str = 'LOG', details: Dict[str, Any] = None, **kwargs):
                    details_dict = details or {}
                    details_str = ", ".join([f"{k}={v}" for k, v in details_dict.items()])
                    
                    extra = {
                        'category': category,
                        'subcategory': subcategory,
                        'details': details_str
                    }
                    # stacklevel=2: 래퍼 함수가 아닌 실제 호출 위치(파일, 라인넘버)를 로깅하도록 함
                    method(msg, *args, extra=extra, stacklevel=2, **kwargs)
                return wrapper

            wrapped_method = make_wrapper(original_method)
            setattr(self, method_name, wrapped_method)

    def _setup_logger(self):
        """로거 초기 설정 (핸들러 및 포맷터)"""
        self._logger = logging.getLogger("roomie_rms")
        
        # 환경 변수 또는 설정 파일에서 로그 레벨 읽기
        log_level = os.getenv("LOG_LEVEL", settings.LOG_LEVEL).upper()
        self._logger.setLevel(getattr(logging, log_level, logging.INFO))
        
        # 중복 핸들러 방지
        if not self._logger.handlers:
            self._add_console_handler()
            self._add_file_handler()
        
        # 전파 방지 (부모 로거로의 메시지 전달 차단)
        self._logger.propagate = False

    def _log_session_start(self):
        """세션 시작 정보를 로깅합니다."""
        log_level = os.getenv("LOG_LEVEL", settings.LOG_LEVEL).upper()
        self.info(
            f"RMS 노드 세션 시작 - {self._session_start_time.strftime('%Y-%m-%d %H:%M:%S')}",
            category="SYSTEM", subcategory="START"
        )
        self.info(
            f"로그 파일: {self._get_session_log_file()}",
            category="SYSTEM", subcategory="INFO"
        )
        self.info(
            f"로그 레벨: {log_level}",
            category="SYSTEM", subcategory="INFO"
        )
    
    def _get_session_log_file(self) -> str:
        """현재 세션의 로그 파일명 반환"""
        timestamp = self._session_start_time.strftime('%Y%m%d_%H%M%S')
        return f"roomie_rms_{timestamp}.log"
    
    def _session_preamble(self) -> str:
        """세션 시작 시간을 포함한 간단한 메시지를 반환합니다."""
        return self._session_start_time.strftime('%Y-%m-%d %H:%M:%S')

    def _add_console_handler(self):
        """콘솔 출력 핸들러 추가"""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self._get_formatter())
        self._logger.addHandler(console_handler)
    
    def _add_file_handler(self):
        """파일 출력 핸들러 추가 (세션별 로그 파일)"""
        log_dir = settings.LOG_DIR
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # 세션별 로그 파일 경로
        session_log_file = self._get_session_log_file()
        log_file_path = os.path.join(log_dir, session_log_file)
        
        file_handler = RotatingFileHandler(
            log_file_path,
            maxBytes=settings.LOG_MAX_BYTES,
            backupCount=settings.LOG_BACKUP_COUNT,
            encoding='utf-8'
        )
        file_handler.setFormatter(self._get_formatter())
        self._logger.addHandler(file_handler)
        
        # 기존 로그 파일에도 추가 (호환성 유지)
        legacy_log_file_path = os.path.join(log_dir, settings.LOG_FILE)
        legacy_handler = RotatingFileHandler(
            legacy_log_file_path,
            maxBytes=settings.LOG_MAX_BYTES,
            backupCount=settings.LOG_BACKUP_COUNT,
            encoding='utf-8'
        )
        legacy_handler.setFormatter(self._get_formatter())
        self._logger.addHandler(legacy_handler)

    def _get_formatter(self):
        """로그 포맷터 반환"""
        log_format = "[%(asctime)s] - [%(name)s] - [%(levelname)s] - [%(filename)s:%(lineno)d] | [%(category)s][%(subcategory)s] | %(details)s | %(message)s"
        return logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')
    
    def log_session_end(self):
        """세션 종료 로그"""
        if self._logger and self._session_start_time:
            session_duration = datetime.now() - self._session_start_time
            self.info(
                f"RMS 노드 세션 종료 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                category="SYSTEM", subcategory="END"
            )
            self.info(
                f"세션 지속 시간: {session_duration}",
                category="SYSTEM", subcategory="INFO"
            )
    
    @property
    def logger(self):
        """로거 인스턴스 반환"""
        return self._logger

# 싱글톤 로거 인스턴스
_roomie_logger = RoomieLogger()
# logger 객체를 RoomieLogger 인스턴스로 직접 할당
logger = _roomie_logger

# 편의 함수들 (새로운 로깅 형식에 맞게 수정)
def get_logger(name: Optional[str] = None):
    """
    로거 인스턴스를 반환합니다.
    
    Args:
        name: 로거 이름 (선택사항, 현재는 무시됨)
    
    Returns:
        RoomieLogger: 설정된 로거 인스턴스
    """
    return logger

def log_task_creation(task_id: str, location: str, items: list, timestamp: str):
    """배송 작업 생성 전용 로그"""
    items_summary = ", ".join([f"{item['name']}({item['quantity']}개)" for item in items])
    logger.info(
        f"배송 작업 생성",
        category="TASK",
        subcategory="CREATE",
        details={"TaskID": task_id, "Location": location, "Order": f"[{items_summary}]", "Timestamp": timestamp}
    )

def log_websocket_event(event_type: str, client_type: str, details: str = ""):
    """WebSocket 이벤트 전용 로그"""
    logger.info(
        details,
        category="API",
        subcategory="WS-EVENT",
        details={"Event": event_type, "ClientType": client_type}
    )

def log_database_operation(operation: str, table: str, success: bool, details: str = "", level: str = "INFO"):
    """데이터베이스 작업 전용 로그"""
    log_func = getattr(logger, level.lower(), logger.info)
    details_dict = {"Table": table}
    if details:
        details_dict["Info"] = details
        
    log_func(
        f"{operation} {'성공' if success else '실패'}",
        category="DB",
        subcategory=operation,
        details=details_dict
    )

def log_ros_event(event_type: str, node_info: str, details: str = ""):
    """ROS2 이벤트 전용 로그"""
    logger.info(
        details,
        category="ROS2",
        subcategory=event_type,
        details={"Node": node_info}
    )

def log_node_startup():
    """노드 시작 로그"""
    logger.info(f"시스템 정보: Python {sys.version}", category="SYSTEM", subcategory="INFO")
    logger.info(f"작업 디렉토리: {os.getcwd()}", category="SYSTEM", subcategory="INFO")

def log_node_shutdown():
    """노드 종료 로그"""
    logger.info("RMS 노드 종료 프로세스 시작", category="SYSTEM", subcategory="SHUTDOWN")
    _roomie_logger.log_session_end()

def get_current_timestamp() -> str:
    """현재 시간을 ISO 형식으로 반환 (DB 저장용)"""
    return datetime.now().isoformat()

def get_current_timestamp_kr() -> str:
    """현재 시간을 한국어 형식으로 반환"""
    return datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
