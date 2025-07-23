import logging
import sys
from datetime import datetime

# 1. 로거 인스턴스 생성
logger = logging.getLogger("roomie_rms")

# 2. 로그 레벨 설정 (기본값: INFO)
# DEBUG, INFO, WARNING, ERROR, CRITICAL 순으로 심각도가 높아집니다.
logger.setLevel(logging.INFO)

# 3. 로그 포맷터 생성
# 형식: [시간] - [로거이름] - [로그레벨] - [파일명:줄번호] - [메시지]
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
)

# 4. 콘솔 출력을 위한 핸들러 생성
# 핸들러가 이미 추가되었는지 확인하여 중복 로깅을 방지합니다.
if not logger.handlers:
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

# 5. 작업 생성 전용 로깅 함수
def log_task_creation(task_id: str, location: str, items: list, timestamp: str):
    """배송 작업 생성 시 전용 로그 (DB 저장 대비)"""
    items_summary = ", ".join([f"{item['name']}({item['quantity']}개)" for item in items])
    logger.info(f"새 배송 작업 생성 | 작업ID: {task_id} | 위치: {location} | 주문: [{items_summary}] | 시간: {timestamp}")

# 6. WebSocket 이벤트 전용 로깅 함수
def log_websocket_event(event_type: str, client_type: str, details: str = ""):
    """WebSocket 연결/해제 이벤트 로그"""
    logger.info(f"WebSocket {event_type} | 클라이언트: {client_type} | {details}")

# 7. Timestamp 생성 유틸리티 함수들
def get_current_timestamp() -> str:
    """현재 시간을 ISO 형식으로 반환 (DB 저장용)"""
    return datetime.now().isoformat()

def get_current_timestamp_kr() -> str:
    """현재 시간을 한국어 형식으로 반환"""
    return datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분 %S초') 