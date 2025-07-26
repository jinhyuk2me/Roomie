"""
에러 처리 데코레이터 및 유틸리티 함수들
표준화된 에러 처리를 위한 헬퍼 함수들
"""

import functools
from typing import Callable, Any, Dict, Optional, Type
import traceback
from contextlib import contextmanager
import mysql.connector

from .logger import logger
from .exceptions import (
    RoomieBaseException, DatabaseException, ROS2Exception,
    ErrorCode, raise_db_error, raise_ros_error
)


def handle_exceptions(
    default_return: Any = None,
    log_traceback: bool = True,
    reraise: bool = False
):
    """
    예외 처리 데코레이터
    
    Args:
        default_return: 예외 발생 시 반환할 기본값
        log_traceback: 스택 트레이스 로그 여부
        reraise: 예외를 다시 발생시킬지 여부
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except RoomieBaseException as e:
                # 커스텀 예외는 이미 구조화되어 있으므로 그대로 로그
                logger.error(f"Roomie 예외 발생 in {func.__name__}: {e.message}", 
                     extra={"error_code": e.error_code.value, "details": e.details})
                if log_traceback:
                    logger.error(f"스택 트레이스: {traceback.format_exc()}")
                
                if reraise:
                    raise
                return default_return
                
            except mysql.connector.Error as e:
                # MySQL 예외를 DatabaseException으로 변환
                logger.error(f"데이터베이스 오류 in {func.__name__}: {e}")
                if log_traceback:
                    logger.error(f"스택 트레이스: {traceback.format_exc()}")
                
                if reraise:
                    raise_db_error(f"데이터베이스 오류: {e}", original_exception=e)
                return default_return
                
            except Exception as e:
                # 일반 예외
                logger.error(f"예상치 못한 오류 in {func.__name__}: {e}")
                if log_traceback:
                    logger.error(f"스택 트레이스: {traceback.format_exc()}")
                
                if reraise:
                    raise
                return default_return
                
        return wrapper
    return decorator


def handle_database_errors(func: Callable) -> Callable:
    """데이터베이스 작업 전용 예외 처리 데코레이터"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except mysql.connector.Error as e:
            logger.error(f"데이터베이스 오류 in {func.__name__}: {e}")
            raise_db_error(f"데이터베이스 작업 실패: {e}", original_exception=e)
        except Exception as e:
            logger.error(f"예상치 못한 오류 in {func.__name__}: {e}")
            raise
    return wrapper


def handle_ros_errors(func: Callable) -> Callable:
    """ROS2 작업 전용 예외 처리 데코레이터"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"ROS2 오류 in {func.__name__}: {e}")
            raise_ros_error(f"ROS2 작업 실패: {e}", original_exception=e)
    return wrapper


@contextmanager
def database_transaction(connection):
    """
    데이터베이스 트랜잭션 컨텍스트 매니저
    
    Args:
        connection: MySQL 커넥션 객체
    """
    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)
        yield cursor
        connection.commit()
        logger.debug("데이터베이스 트랜잭션 커밋 성공")
    except Exception as e:
        connection.rollback()
        logger.error(f"데이터베이스 트랜잭션 롤백: {e}")
        raise
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


@contextmanager
def database_transaction(connection):
    """
    데이터베이스 트랜잭션 컨텍스트 매니저
    
    Args:
        connection: MySQL 커넥션 객체
    """
    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)
        yield cursor
        connection.commit()
        logger.debug("데이터베이스 트랜잭션 커밋 성공")
    except Exception as e:
        connection.rollback()
        logger.error(f"데이터베이스 트랜잭션 롤백: {e}")
        raise
    finally:
        if cursor:
            cursor.close()

@contextmanager
def safe_database_connection(get_connection_func: Callable):
    """
    안전한 데이터베이스 연결 컨텍스트 매니저
    
    Args:
        get_connection_func: 커넥션을 반환하는 함수
    """
    connection = None
    try:
        connection = get_connection_func()
        if not connection:
            raise_db_error("데이터베이스 연결을 가져올 수 없습니다")
        yield connection
    except mysql.connector.Error as e:
        logger.error(f"데이터베이스 연결 오류: {e}")
        raise_db_error(f"데이터베이스 연결 실패: {e}", original_exception=e)
    finally:
        if connection and connection.is_connected():
            connection.close()


def log_function_call(func: Callable) -> Callable:
    """함수 호출을 로그로 기록하는 데코레이터"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"함수 호출 시작: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.debug(f"함수 호출 완료: {func.__name__}")
            return result
        except Exception as e:
            logger.debug(f"함수 호출 실패: {func.__name__} - {e}")
            raise
    return wrapper


def validate_required_fields(required_fields: list):
    """필수 필드 유효성 검사 데코레이터"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 첫 번째 인자가 요청 객체라고 가정
            if args and hasattr(args[0], '__dict__'):
                request_obj = args[0]
                for field in required_fields:
                    if not hasattr(request_obj, field) or getattr(request_obj, field) is None:
                        from .exceptions import raise_validation_error
                        raise_validation_error(f"필수 필드가 누락되었습니다: {field}", field_name=field)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def format_error_response(exception: RoomieBaseException) -> Dict[str, Any]:
    """커스텀 예외를 API 응답 형식으로 변환"""
    return {
        "success": False,
        "error": {
            "code": exception.error_code.value,
            "message": exception.message,
            "details": exception.details
        }
    }


def log_and_reraise(exception_class: Type[Exception] = Exception):
    """로그를 남기고 예외를 다시 발생시키는 데코레이터"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_class as e:
                logger.error(f"예외 발생 in {func.__name__}: {e}")
                raise
        return wrapper
    return decorator 