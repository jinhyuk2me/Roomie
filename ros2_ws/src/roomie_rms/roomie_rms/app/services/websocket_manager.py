from fastapi import WebSocket
from collections import defaultdict
import json
from app.utils.logger import logger

class WebSocketManager:
    def __init__(self):
        # client_type과 client_id를 키로 해서 WebSocket 객체를 저장
        self.connections: defaultdict[str, dict[str, WebSocket]] = defaultdict(dict)
        # 연결 해제 시 클라이언트 정보를 역으로 찾기 위한 매핑 구조
        self.reverse_lookup: dict[WebSocket, tuple[str, str]] = {}

    async def connect(self, websocket: WebSocket, client_type: str, client_id: str):
        await websocket.accept()
        self.connections[client_type][client_id] = websocket
        self.reverse_lookup[websocket] = (client_type, client_id)
        logger.info(f"WebSocket client connected: type='{client_type}', id='{client_id}'")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.reverse_lookup:
            client_type, client_id = self.reverse_lookup.pop(websocket)
            if client_id in self.connections[client_type]:
                del self.connections[client_type][client_id]
            logger.info(f"WebSocket client disconnected: type='{client_type}', id='{client_id}'")

    async def send_to_client(self, client_type: str, client_id: str, data: dict):
        """특정 클라이언트에게 메시지를 전송합니다."""
        message = json.dumps(data, ensure_ascii=False)
        websocket = self.connections[client_type].get(client_id)
        if websocket:
            await websocket.send_text(message)
            logger.debug(f"Sent message to client: type='{client_type}', id='{client_id}'")

    async def broadcast_to(self, client_type: str, data: dict):
        """특정 타입의 모든 클라이언트에게 메시지를 브로드캐스트합니다."""
        message = json.dumps(data, ensure_ascii=False)
        if self.connections[client_type]:
            # Create a list of connections to iterate over, to avoid issues with dict size changing during iteration
            for connection in list(self.connections[client_type].values()):
                await connection.send_text(message)
            logger.debug(f"Broadcasted message to all '{client_type}' clients.")

# 싱글톤 인스턴스
manager = WebSocketManager()