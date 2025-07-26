"""
WebSocket 연결 관리자 모듈

클라이언트 연결 관리, 메시지 전송, 브로드캐스팅 기능을 제공합니다.
"""

from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from typing import Dict, List
import json
import asyncio

from app.utils.logger import get_logger

logger = get_logger(__name__)

class WebSocketManager:
    """WebSocket 연결을 관리하는 클래스"""
    
    def __init__(self):
        # 연결된 클라이언트들을 저장 {client_type: {client_id: websocket}}
        self.connections: Dict[str, Dict[str, WebSocket]] = {
            "guest": {},
            "staff": {},
            "admin": {}
        }
        self.router = APIRouter()
        self._setup_routes()

    def _setup_routes(self):
        """WebSocket 라우터 설정"""
        
        @self.router.websocket("/ws/guest/{client_id}")
        async def guest_websocket_endpoint(websocket: WebSocket, client_id: str):
            await self.connect(websocket, "guest", client_id)
            try:
                while True:
                    data = await websocket.receive_text()
                    logger.debug(f"게스트 메시지 수신: {client_id} | {data}")
            except WebSocketDisconnect:
                self.disconnect("guest", client_id)

        @self.router.websocket("/ws/staff/{client_id}")
        async def staff_websocket_endpoint(websocket: WebSocket, client_id: str):
            await self.connect(websocket, "staff", client_id)
            try:
                while True:
                    data = await websocket.receive_text()
                    logger.debug(f"직원 메시지 수신: {client_id} | {data}")
            except WebSocketDisconnect:
                self.disconnect("staff", client_id)

        @self.router.websocket("/ws/admin/{client_id}")
        async def admin_websocket_endpoint(websocket: WebSocket, client_id: str):
            await self.connect(websocket, "admin", client_id)
            try:
                while True:
                    data = await websocket.receive_text()
                    logger.debug(f"관리자 메시지 수신: {client_id} | {data}")
            except WebSocketDisconnect:
                self.disconnect("admin", client_id)

    async def connect(self, websocket: WebSocket, client_type: str, client_id: str):
        """클라이언트 연결을 설정합니다."""
        await websocket.accept()
        self.connections[client_type][client_id] = websocket
        
        # 클라이언트 정보 로깅
        client_host = websocket.client.host if websocket.client else "unknown"
        connected_count = len(self.connections[client_type])
        
        logger.info(
            f"WebSocket 연결됨 | "
            f"타입: {client_type.upper()} | "
            f"ID: {client_id} | "
            f"IP: {client_host} | "
            f"현재 {client_type} 연결 수: {connected_count}"
        )

    def disconnect(self, client_type: str, client_id: str):
        """클라이언트 연결을 해제합니다."""
        if client_id in self.connections[client_type]:
            del self.connections[client_type][client_id]
            
        remaining_count = len(self.connections[client_type])
        logger.info(
            f"WebSocket 연결 해제됨 | "
            f"타입: {client_type.upper()} | "
            f"ID: {client_id} | "
            f"남은 {client_type} 연결 수: {remaining_count}"
        )

    async def send_to_client(self, client_type: str, client_id: str, message: str):
        """특정 클라이언트에게 메시지를 전송합니다."""
        if client_type in self.connections and client_id in self.connections[client_type]:
            connection = self.connections[client_type][client_id]
            try:
                await connection.send_text(message)
                logger.info(
                    f"메시지 전송 완료 | "
                    f"대상: {client_type.upper()}({client_id}) | "
                    f"크기: {len(message)}bytes"
                )
            except Exception as e:
                logger.error(f"메시지 전송 실패: {client_type}({client_id}) - {e}")
                # 연결이 끊어진 경우 제거
                self.disconnect(client_type, client_id)
        else:
            logger.warning(f"전송 실패 | 대상을 찾을 수 없음: {client_type}({client_id})")

    def send_to_client_sync(self, client_type: str, client_id: str, message: str):
        """동기적으로 클라이언트에게 메시지를 전송합니다."""
        try:
            asyncio.create_task(self.send_to_client(client_type, client_id, message))
        except Exception as e:
            logger.error(f"동기 메시지 전송 실패: {e}")

    async def broadcast_to(self, client_type: str, message: str):
        """특정 타입의 모든 클라이언트에게 브로드캐스트합니다."""
        if client_type in self.connections and self.connections[client_type]:
            connected_count = len(self.connections[client_type])
            
            # 메시지에서 이벤트 타입 추출 (JSON인 경우)
            try:
                data = json.loads(message)
                event_type = data.get('action', 'unknown')
            except:
                event_type = 'text'
            
            logger.info(
                f"브로드캐스트 시작 | "
                f"대상: {client_type.upper()} 그룹 ({connected_count}개 연결) | "
                f"이벤트: {event_type}"
            )
            
            # 연결 목록을 복사하여 반복 중 딕셔너리 크기 변경 문제 방지
            for client_id, connection in list(self.connections[client_type].items()):
                try:
                    await connection.send_text(message)
                    logger.debug(f"브로드캐스트 성공: {client_type}({client_id})")
                except Exception as e:
                    logger.error(f"브로드캐스트 실패: {client_type}({client_id}) - {e}")
                    
            logger.info(f"브로드캐스트 완료 | {client_type.upper()} 그룹")
        else:
            logger.warning(f"브로드캐스트 스킵 | {client_type.upper()} 그룹에 연결된 클라이언트 없음")

    def send_to_client_by_location(self, client_type: str, location_name: str, message: str):
        """특정 위치의 클라이언트에게 메시지를 전송합니다."""
        # 현재 구현에서는 위치 정보가 client_id에 포함되어 있다고 가정
        # 실제로는 더 정교한 위치 기반 라우팅이 필요할 수 있습니다
        target_client_id = location_name.lower()  # 예: ROOM_101 -> room_101
        
        if client_type in self.connections and target_client_id in self.connections[client_type]:
            try:
                connection = self.connections[client_type][target_client_id]
                # 비동기 메서드를 동기적으로 호출 (threading 환경에서)
                import asyncio
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(connection.send_text(message))
                loop.close()
                
                logger.info(f"위치 기반 메시지 전송 완료: {client_type}@{location_name}")
            except Exception as e:
                logger.error(f"위치 기반 메시지 전송 실패: {client_type}@{location_name} - {e}")
        else:
            logger.warning(f"위치 기반 전송 대상 없음: {client_type}@{location_name}")

    def send_to_client_sync(self, client_type: str, client_id: str, message: str):
        """동기적으로 특정 클라이언트에게 메시지를 전송합니다."""
        if client_type in self.connections and client_id in self.connections[client_type]:
            try:
                connection = self.connections[client_type][client_id]
                # 비동기 메서드를 동기적으로 호출
                import asyncio
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(connection.send_text(message))
                loop.close()
                
                logger.info(f"동기 메시지 전송 완료: {client_type}({client_id})")
            except Exception as e:
                logger.error(f"동기 메시지 전송 실패: {client_type}({client_id}) - {e}")
        else:
            logger.warning(f"동기 전송 대상 없음: {client_type}({client_id})")

    def broadcast_to_group(self, client_type: str, message_dict_or_str):
        """그룹에 메시지를 브로드캐스트합니다 (동기 버전)."""
        if isinstance(message_dict_or_str, dict):
            import json
            message = json.dumps(message_dict_or_str)
        else:
            message = message_dict_or_str
            
        if client_type in self.connections and self.connections[client_type]:
            try:
                # 비동기 메서드를 동기적으로 호출
                import asyncio
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(self._broadcast_to_group_async(client_type, message))
                loop.close()
            except Exception as e:
                logger.error(f"동기 브로드캐스트 실패: {client_type} - {e}")
        else:
            logger.warning(f"동기 브로드캐스트 대상 없음: {client_type}")

    async def _broadcast_to_group_async(self, client_type: str, message: str):
        """내부 비동기 브로드캐스트 메서드"""
        if client_type in self.connections and self.connections[client_type]:
            connected_count = len(self.connections[client_type])
            
            # 메시지에서 이벤트 타입 추출 (JSON인 경우)
            try:
                data = json.loads(message)
                event_type = data.get('action', 'unknown')
            except:
                event_type = 'text'
            
            logger.info(
                f"비동기 브로드캐스트 시작 | "
                f"대상: {client_type.upper()} 그룹 ({connected_count}개 연결) | "
                f"이벤트: {event_type}"
            )
            
            # 연결 목록을 복사하여 반복 중 딕셔너리 크기 변경 문제 방지
            for client_id, connection in list(self.connections[client_type].items()):
                try:
                    await connection.send_text(message)
                    logger.debug(f"비동기 브로드캐스트 성공: {client_type}({client_id})")
                except Exception as e:
                    logger.error(f"비동기 브로드캐스트 실패: {client_type}({client_id}) - {e}")
                    
            logger.info(f"비동기 브로드캐스트 완료 | {client_type.upper()} 그룹")
        else:
            logger.warning(f"비동기 브로드캐스트 대상 없음: {client_type}")

# 글로벌 인스턴스 생성
manager = WebSocketManager()