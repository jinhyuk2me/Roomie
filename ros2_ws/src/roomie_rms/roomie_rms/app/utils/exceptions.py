"""
Roomie RMS 커스텀 예외 클래스들
표준화된 에러 처리를 위한 예외 정의
"""

from typing import Optional, Dict, Any
from enum import Enum


class ErrorCode(Enum):
    """에러 코드 열거형"""
    # 데이터베이스 관련
    DB_CONNECTION_FAILED = "DB_CONNECTION_FAILED"
    DB_QUERY_FAILED = "DB_QUERY_FAILED"
    DB_TRANSACTION_FAILED = "DB_TRANSACTION_FAILED"
    DB_RECORD_NOT_FOUND = "DB_RECORD_NOT_FOUND"
    
    # ROS2 관련
    ROS_SERVICE_UNAVAILABLE = "ROS_SERVICE_UNAVAILABLE"
    ROS_ACTION_FAILED = "ROS_ACTION_FAILED"
    ROS_TOPIC_PUBLISH_FAILED = "ROS_TOPIC_PUBLISH_FAILED"
    
    # 작업 관리 관련
    TASK_CREATION_FAILED = "TASK_CREATION_FAILED"
    TASK_ASSIGNMENT_FAILED = "TASK_ASSIGNMENT_FAILED"
    TASK_NOT_FOUND = "TASK_NOT_FOUND"
    INVALID_TASK_STATUS = "INVALID_TASK_STATUS"
    
    # 로봇 관련
    ROBOT_NOT_AVAILABLE = "ROBOT_NOT_AVAILABLE"
    ROBOT_NOT_FOUND = "ROBOT_NOT_FOUND"
    ROBOT_COMMUNICATION_FAILED = "ROBOT_COMMUNICATION_FAILED"
    
    # WebSocket 관련
    WEBSOCKET_CONNECTION_FAILED = "WEBSOCKET_CONNECTION_FAILED"
    WEBSOCKET_SEND_FAILED = "WEBSOCKET_SEND_FAILED"
    
    # 유효성 검사 관련
    VALIDATION_FAILED = "VALIDATION_FAILED"
    INVALID_PARAMETER = "INVALID_PARAMETER"
    MISSING_REQUIRED_FIELD = "MISSING_REQUIRED_FIELD"
    
    # 일반적인 오류
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    EXTERNAL_SERVICE_ERROR = "EXTERNAL_SERVICE_ERROR"


class RoomieBaseException(Exception):
    """Roomie RMS 기본 예외 클래스"""
    
    def __init__(
        self, 
        message: str,
        error_code: ErrorCode,
        details: Optional[Dict[str, Any]] = None,
        original_exception: Optional[Exception] = None
    ):
        self.message = message
        self.error_code = error_code
        self.details = details or {}
        self.original_exception = original_exception
        super().__init__(message)
    
    def to_dict(self) -> Dict[str, Any]:
        """예외 정보를 딕셔너리로 변환"""
        return {
            "error_code": self.error_code.value,
            "message": self.message,
            "details": self.details
        }


class DatabaseException(RoomieBaseException):
    """데이터베이스 관련 예외"""
    pass


class ROS2Exception(RoomieBaseException):
    """ROS2 관련 예외"""
    pass


class TaskManagementException(RoomieBaseException):
    """작업 관리 관련 예외"""
    pass


class RobotException(RoomieBaseException):
    """로봇 관련 예외"""
    pass


class WebSocketException(RoomieBaseException):
    """WebSocket 관련 예외"""
    pass


class ValidationException(RoomieBaseException):
    """유효성 검사 관련 예외"""
    pass


# 편의 함수들
def raise_db_error(message: str, details: Optional[Dict] = None, original_exception: Optional[Exception] = None):
    """데이터베이스 오류 발생"""
    raise DatabaseException(
        message=message,
        error_code=ErrorCode.DB_CONNECTION_FAILED,
        details=details,
        original_exception=original_exception
    )


def raise_ros_error(message: str, details: Optional[Dict] = None, original_exception: Optional[Exception] = None):
    """ROS2 오류 발생"""
    raise ROS2Exception(
        message=message,
        error_code=ErrorCode.ROS_SERVICE_UNAVAILABLE,
        details=details,
        original_exception=original_exception
    )


def raise_task_error(message: str, error_code: ErrorCode = ErrorCode.TASK_CREATION_FAILED, 
                    details: Optional[Dict] = None, original_exception: Optional[Exception] = None):
    """작업 관리 오류 발생"""
    raise TaskManagementException(
        message=message,
        error_code=error_code,
        details=details,
        original_exception=original_exception
    )


def raise_validation_error(message: str, field_name: str = "", details: Optional[Dict] = None):
    """유효성 검사 오류 발생"""
    error_details = {"field": field_name} if field_name else {}
    if details:
        error_details.update(details)
    
    raise ValidationException(
        message=message,
        error_code=ErrorCode.VALIDATION_FAILED,
        details=error_details
    ) 