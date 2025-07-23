from fastapi import WebSocket
from collections import defaultdict
import json

class WebSocketManager:
    def __init__(self):
        # key: client_type (e.g., "staff", "guest"), value: list of WebSockets
        self.connections: defaultdict[str, list[WebSocket]] = defaultdict(list)

    async def connect(self, websocket: WebSocket, client_type: str):
        await websocket.accept()
        self.connections[client_type].append(websocket)
        print(f"New connection from a {client_type} client.")

    def disconnect(self, websocket: WebSocket, client_type: str):
        self.connections[client_type].remove(websocket)
        print(f"A {client_type} client disconnected.")

    async def broadcast_to(self, client_type: str, data: dict):
        """특정 타입의 클라이언트에게만 메시지를 전송합니다."""
        message = json.dumps(data)
        if self.connections[client_type]:
            for connection in self.connections[client_type]:
                await connection.send_text(message)

# 싱글톤 인스턴스
manager = WebSocketManager()