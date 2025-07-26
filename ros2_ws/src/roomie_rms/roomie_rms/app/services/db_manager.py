import mysql.connector
from mysql.connector import pooling
import os
from app.config import settings # 설정 임포트
from app.utils.logger import get_logger, log_database_operation
from app.utils.error_handler import handle_database_errors
from app.utils.exceptions import raise_db_error

logger = get_logger(__name__)

# 전역 변수로 커넥션 풀을 관리
db_pool: pooling.MySQLConnectionPool = None

@handle_database_errors
def init_db_pool():
    """데이터베이스 커넥션 풀을 초기화합니다."""
    global db_pool
    if db_pool is not None:
        logger.warning("DB 커넥션 풀이 이미 초기화되어 있습니다")
        return

    try:
        # 먼저 데이터베이스 존재 확인/생성
        _check_and_create_database()
        
        logger.info(f"[DB] 커넥션 풀 초기화 시작 (pool_name={settings.DB_POOL_NAME}, pool_size={settings.DB_POOL_SIZE})")
        db_pool = pooling.MySQLConnectionPool(
            pool_name=settings.DB_POOL_NAME,
            pool_size=settings.DB_POOL_SIZE,
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME,
            # autocommit=True # 트랜잭션 관리를 위해 autocommit 비활성화
        )
        log_database_operation("INIT", "connection_pool", True, f"Pool size: {settings.DB_POOL_SIZE}")
        logger.info("[DB] 커넥션 풀 초기화 완료")
        
        # 커넥션 풀 생성 후, DB 스키마 및 초기 데이터 확인/생성
        _check_and_create_schema()

    except mysql.connector.Error as err:
        logger.error(f"[DB] 커넥션 풀 초기화 실패: {err}")
        db_pool = None # 초기화 실패 시 풀을 None으로 설정
        raise_db_error(f"[DB] 커넥션 풀 초기화 실패: {err}", original_exception=err)

def get_connection():
    """커넥션 풀에서 DB 연결을 가져옵니다."""
    if db_pool is None:
        logger.error("[DB] 커넥션 풀이 초기화되지 않았습니다")
        raise_db_error("[DB] 커넥션 풀이 초기화되지 않았습니다")
    
    try:
        connection = db_pool.get_connection()
        return connection
    except mysql.connector.Error as err:
        logger.error(f"[DB] 커넥션 풀에서 연결 획득 실패: {err}")
        raise_db_error(f"[DB] DB 연결 실패: {err}", original_exception=err)

def _load_constants_from_db():
    """DB의 lookup 테이블에서 상수 값들을 로드하여 settings 객체에 저장합니다."""
    logger.info("DB에서 애플리케이션 상수 로드를 시작합니다...")
    
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        
        lookup_tables = {
            'task_status': 'task_status',
            'robot_status': 'robot_status',
            'task_type': 'task_type',
            'location': 'location',
        }

        for setting_key, table_name in lookup_tables.items():
            query = f"SELECT id, name FROM `{table_name}`"
            cursor.execute(query)
            records = cursor.fetchall()
            
            # settings.db_consts.task_status 딕셔너리에 'name' -> 'id' 매핑 저장
            name_to_id_map = {record['name']: record['id'] for record in records}
            setattr(settings.db_consts, setting_key, name_to_id_map)
            
            logger.info(f"'{table_name}' 테이블에서 {len(records)}개의 상수를 로드했습니다.")
            
    except mysql.connector.Error as err:
        logger.error(f"[DB] 상수 로드 중 오류 발생: {err}")
        raise
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn and conn.is_connected():
            conn.close()

def _execute_sql_from_file(cursor, filepath):
    """SQL 파일의 내용을 실행합니다."""
    # 파일 존재 여부 미리 확인
    if not os.path.exists(filepath):
        logger.error(f"[DB] SQL 파일을 찾을 수 없음: {filepath}")
        raise FileNotFoundError(f"SQL 파일을 찾을 수 없습니다: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # 주석과 빈 줄을 무시하고 세미콜론으로 구분된 여러 SQL 문을 처리
            sql_script = f.read()
            # -- 로 시작하는 주석 제거
            sql_script = '\n'.join(line for line in sql_script.split('\n') if not line.strip().startswith('--'))
            # 여러 SQL 문을 분리하여 실행
            for command in sql_script.split(';'):
                command = command.strip()
                if command:
                    cursor.execute(command)
        logger.info(f"[DB] 성공적으로 SQL 파일 실행: {filepath}")
    except Exception as e:
        logger.error(f"[DB] SQL 파일 실행 중 오류 발생 ({filepath}): {e}")
        raise


def _check_and_create_database():
    """데이터베이스가 존재하는지 확인하고, 없으면 생성합니다."""
    conn = None
    try:
        # 데이터베이스 지정 없이 MySQL 서버에 연결
        conn = mysql.connector.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD
        )
        cursor = conn.cursor()
        
        # 데이터베이스 존재 확인 및 생성
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        logger.info(f"[DB] 데이터베이스 '{settings.DB_NAME}' 확인/생성 완료.")
        conn.commit()
        
    except mysql.connector.Error as err:
        logger.error(f"[DB] 데이터베이스 확인/생성 중 오류 발생: {err}")
        raise
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

def _check_and_create_schema():
    """DB 스키마와 초기 데이터가 존재하는지 확인하고, 없으면 생성합니다."""
    conn = None
    try:
        # 커넥션 풀에서 연결 가져오기 (이제 데이터베이스가 존재함)
        conn = get_connection()
        cursor = conn.cursor()

        # 테이블 존재 여부 확인 (예: 'robot' 테이블)
        cursor.execute("SHOW TABLES LIKE 'robot'")
        result = cursor.fetchone()

        if not result:
            logger.info("[DB] 테이블이 존재하지 않아 새로 생성합니다.")
            # 1. 스키마 파일 실행
            _execute_sql_from_file(cursor, settings.DB_SCHEMA_PATH)
            # 2. 초기 데이터 파일 실행
            _execute_sql_from_file(cursor, settings.DB_DATA_PATH)
            conn.commit()
            logger.info("[DB] 스키마 및 초기 데이터 생성 완료.")
        else:
            logger.info("[DB] 테이블이 이미 존재합니다. 스키마 생성을 건너뜁니다.")
        
        # 스키마/데이터 확인 후 DB 상수 로드
        _load_constants_from_db()

    except mysql.connector.Error as err:
        logger.error(f"[DB] 스키마 확인/생성 중 오류 발생: {err}")
        if conn: conn.rollback()
        raise
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

