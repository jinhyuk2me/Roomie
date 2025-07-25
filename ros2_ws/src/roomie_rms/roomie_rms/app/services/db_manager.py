import mysql.connector
from mysql.connector import pooling
import os
from ..utils.logger import logger

# --- Database Configuration ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
}

DB_NAME = 'roomie_db'

SQL_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'sql')
SCHEMA_FILE = os.path.join(SQL_DIR, 'roomie_db_tables.sql')
DATA_FILE = os.path.join(SQL_DIR, 'roomie_db_data.sql')


class DatabaseManager:
    """
    MySQL 데이터베이스 연결 및 관리를 위한 싱글톤 클래스.
    커넥션 풀을 사용하여 FastAPI 애플리케이션에 최적화된 DB 연결을 제공합니다.
    """
    _instance = None
    _connection_pool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance._initialize_db()
        return cls._instance

    def _initialize_db(self):
        """
        데이터베이스 초기화
        - DB가 없으면 생성
        - 커넥션 풀 설정
        - 테이블과 초기 데이터 설정
        """
        try:
            # DB 존재 여부 확인 및 생성 (DB를 지정하지 않고 연결)
            temp_conn = mysql.connector.connect(**DB_CONFIG, use_pure=True)
            cursor = temp_conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            logger.info(f"데이터베이스 '{DB_NAME}'가 준비되었습니다.")
            cursor.close()
            temp_conn.close()

            # 커넥션 풀 생성 (미리 DB 커넥션을 여러 개 만들어 놓고 필요할 때마다 재사용)
            db_config_with_db = {**DB_CONFIG, 'database': DB_NAME, 'use_pure': True}
            self._connection_pool = pooling.MySQLConnectionPool(
                pool_name="roomie_pool",
                pool_size=5,
                **db_config_with_db
            )
            logger.info("데이터베이스 커넥션 풀이 생성되었습니다.")

            # 테이블 생성 및 초기 데이터 삽입
            self._setup_tables_and_data()

        except mysql.connector.Error as err:
            logger.error(f"데이터베이스 초기화 중 오류 발생: {err}")
            logger.error("DB_CONFIG의 user와 password를 올바르게 설정했는지 확인하세요.")
            exit(1)

    def _execute_sql_script(self, cursor, filepath):
        """파일로부터 SQL 스크립트를 읽어 실행합니다."""
        with open(filepath, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        
        # multi=True 옵션으로 여러 SQL 구문을 한 번에 실행
        for result in cursor.execute(sql_script, multi=True):
            if result.with_rows:
                # SELECT 구문의 결과를 소비해야 다음 구문으로 넘어갈 수 있음
                result.fetchall()

    def _setup_tables_and_data(self):
        """스키마에 따라 테이블을 생성하고, 비어있을 경우 초기 데이터를 삽입합니다."""
        conn = self.get_connection()
        if not conn:
            logger.error("테이블 및 데이터 설정에 실패했습니다 (DB 연결 불가).")
            return

        try:
            cursor = conn.cursor()
            
            # 테이블 생성 (SQL 파일 실행)
            logger.info("테이블 스키마를 설정합니다...")
            self._execute_sql_script(cursor, SCHEMA_FILE)
            logger.info("스키마 설정이 완료되었습니다.")

            # 데이터 중복 삽입 방지를 위해 `floor` 테이블 확인
            cursor.execute("SELECT COUNT(*) FROM floor")
            if cursor.fetchone()[0] == 0:
                logger.info("초기 데이터를 삽입합니다...")
                self._execute_sql_script(cursor, DATA_FILE)
                conn.commit()
                logger.info("데이터베이스에 초기 데이터가 성공적으로 삽입되었습니다.")
            else:
                logger.info("초기 데이터가 이미 존재하므로, 데이터 삽입을 건너뜁니다.")

        except mysql.connector.Error as err:
            logger.error(f"테이블 및 데이터 설정 중 오류 발생: {err}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_connection(self):
        """커넥션 풀에서 DB 연결을 가져옵니다."""
        if self._connection_pool is None:
            logger.error("커넥션 풀이 초기화되지 않았습니다.")
            return None
        try:
            return self._connection_pool.get_connection()
        except mysql.connector.Error as err:
            logger.error(f"커넥션 풀에서 연결을 가져오는 중 오류 발생: {err}")
            return None

# 다른 모듈에서 'from app.services.db_manager import db_manager'로 가져와서 사용
db_manager = DatabaseManager()

