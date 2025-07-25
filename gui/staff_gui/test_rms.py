from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
import asyncio
import json
import uvicorn
from typing import List
import threading
import time

app = FastAPI(title="Test RMS Server")

# WebSocket 연결 관리
connected_clients: List[WebSocket] = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    print(f"Staff GUI 연결됨. 총 연결: {len(connected_clients)}")
    
    try:
        while True:
            # 연결 유지를 위해 대기
            await websocket.receive_text()
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print(f"Staff GUI 연결 해제됨. 총 연결: {len(connected_clients)}")

@app.post("/food_order_status_change")
async def food_order_status_change(request_data: dict):
    """준비완료 상태 변경 요청 처리"""
    print(f"준비완료 요청 받음: {request_data}")
    
    # 요청 데이터 검증
    if request_data.get("type") == "request" and request_data.get("action") == "food_order_status_change":
        task_id = request_data.get("payload", {}).get("task_id")
        
        if task_id:
            # 성공 응답
            response = {
                "type": "response",
                "action": "food_order_status_change",
                "payload": {
                    "task_id": task_id,
                    "status_changed": "food_ready"
                }
            }
            print(f"준비완료 처리됨: {task_id}")
            return JSONResponse(content=response)
    
    # 실패 응답
    return JSONResponse(content={"error": "Invalid request"}, status_code=400)

async def send_to_all_clients(message: dict):
    """모든 연결된 클라이언트에게 메시지 전송"""
    if connected_clients:
        message_str = json.dumps(message, ensure_ascii=False)
        disconnected = []
        
        for client in connected_clients:
            try:
                await client.send_text(message_str)
            except:
                disconnected.append(client)
        
        # 연결 해제된 클라이언트 제거
        for client in disconnected:
            if client in connected_clients:
                connected_clients.remove(client)

@app.get("/")
async def root():
    return {"message": "Test RMS Server Running", "connected_clients": len(connected_clients)}

@app.get("/send_test_order")
async def send_test_order():
    """테스트용 음식 주문 이벤트 전송"""
    order_event = {
        "type": "event",
        "action": "food_order_creation",
        "payload": {
            "task_id": f"TASK_{int(time.time())}",
            "request_location": "ROOM_307",
            "order_details": {
                "items": [
                    {
                        "name": "스파게티",
                        "quantity": 2,
                        "price": 15000
                    },
                    {
                        "name": "피자",
                        "quantity": 1,
                        "price": 15000
                    }
                ]
            }
        }
    }
    
    await send_to_all_clients(order_event)
    return {"message": "테스트 주문 전송됨", "order": order_event}

@app.get("/send_robot_arrival")
async def send_robot_arrival():
    """테스트용 로봇 도착 이벤트 전송"""
    arrival_event = {
        "type": "event", 
        "action": "food_pickup_arrival",
        "payload": {
            "task_id": "TASK_001",
            "robot_id": "ROBOT_01"
        }
    }
    
    await send_to_all_clients(arrival_event)
    return {"message": "로봇 도착 알림 전송됨", "event": arrival_event}

def run_auto_orders():
    """자동으로 주문 생성 (백그라운드)"""
    import asyncio
    
    async def auto_order_loop():
        counter = 1
        while True:
            await asyncio.sleep(30)  # 30초마다
            
            if connected_clients:  # 연결된 클라이언트가 있을 때만
                order_event = {
                    "type": "event",
                    "action": "food_order_creation", 
                    "payload": {
                        "task_id": f"AUTO_{counter:03d}",
                        "request_location": f"ROOM_{300 + (counter % 20)}",
                        "order_details": {
                            "items": [
                                {
                                    "name": ["스파게티", "피자", "스테이크", "버거"][counter % 4],
                                    "quantity": (counter % 3) + 1,
                                    "price": [15000, 18000, 25000, 12000][counter % 4]
                                }
                            ]
                        }
                    }
                }
                
                await send_to_all_clients(order_event)
                print(f"자동 주문 전송: AUTO_{counter:03d}")
                counter += 1
    
    # 새 이벤트 루프에서 실행
    def run_in_thread():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(auto_order_loop())
    
    thread = threading.Thread(target=run_in_thread, daemon=True)
    thread.start()

if __name__ == "__main__":
    print("🚀 Test RMS Server 시작...")
    print("📱 Staff GUI 테스트 가능:")
    print("   - http://localhost:8000/send_test_order (테스트 주문)")
    print("   - http://localhost:8000/send_robot_arrival (로봇 도착)")
    print("   - 30초마다 자동 주문 생성")
    
    # 자동 주문 생성 시작
    run_auto_orders()
    
    # 서버 실행
    uvicorn.run(app, host="0.0.0.0", port=8000) 