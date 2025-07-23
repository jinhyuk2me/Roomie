from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.schemas.gui_models import *
from app.services.websocket_manager import manager
from app.utils.logger import logger, log_task_creation, log_websocket_event, get_current_timestamp
from typing import List
import time
from datetime import datetime, timezone

router = APIRouter()

# 임시 음식 메뉴 데이터 (DB 대신 사용)
TEMP_FOOD_MENU = [
    FoodItem(food_name="스파게티", price=15000, image="/images/spaghetti.jpg"),
    FoodItem(food_name="피자", price=25000, image="/images/pizza.jpg")
]
# 생성된 작업을 임시로 저장할 딕셔너리 (DB 대신 사용)
tasks = {}

# 태스크 ID를 순차적으로 부여하기 위한 카운터
task_counter = 0

@router.post("/get_food_menu", response_model=GetFoodMenuResponse)
async def get_food_menu(request: GetFoodMenuRequest):
    """
    Guest GUI로부터 음식 메뉴 요청을 받아 응답 반환
    """
    logger.info(f"음식 메뉴 요청 수신 | 요청 데이터: {request.payload}")
    
    response_payload = {"food_items": [item.model_dump() for item in TEMP_FOOD_MENU]}
    
    logger.debug(f"음식 메뉴 응답 생성 | 메뉴 개수: {len(TEMP_FOOD_MENU)}개")
    return GetFoodMenuResponse(payload=response_payload)

@router.post("/create_delivery_task", response_model=CreateDeliveryTaskResponse)
async def create_delivery_task(request: CreateDeliveryTaskRequest):
    """
    GGUI로부터 음식 배송 작업을 생성하고 SGUI에 알림 전송
    """
    global task_counter
    
    # 작업 생성 시작 로그
    logger.info(f"배송 작업 생성 요청 수신 | 위치: {request.payload.location_name} | 작업 타입: {request.payload.task_type_name}")
    
    # 1. 새로운 태스크 ID 생성 (순차적 번호 사용)
    task_counter += 1
    task_id = str(task_counter)
    
    # 2. 현재 시간 timestamp 생성
    creation_timestamp = get_current_timestamp()
    
    # 3. 작업 정보 저장 (임시 DB) - timestamp 포함
    task_data = {
        "payload": request.payload,
        "created_at": creation_timestamp,
        "task_id": task_id,
        "status": "created"
    }
    tasks[task_id] = task_data
    
    # 4. 주문 상세 정보 추출
    order_items = request.payload.order_details.get("items", [])
    
    # 5. 작업 생성 전용 로그 (DB 저장 대비)
    log_task_creation(
        task_id=task_id,
        location=request.payload.location_name,
        items=[{"name": item.name, "quantity": item.quantity, "price": item.price} for item in order_items],
        timestamp=creation_timestamp
    )

    # 6. SGUI에 보낼 이벤트 생성
    event_payload = {
        "task_id": task_id,
        "request_location": request.payload.location_name,
        "order_details": {
            "items": [item.model_dump() for item in order_items]
        },
        "created_at": creation_timestamp
    }
    sdui_event = FoodOrderCreationEvent(payload=event_payload)
    
    # 7. Staff 클라이언트들에게 주문 발생 이벤트 전송
    try:
        await manager.broadcast_to("staff", sdui_event.model_dump())
        logger.info(f"Staff GUI에 주문 이벤트 전송 완료 | 작업ID: {task_id}")
    except Exception as e:
        logger.error(f"Staff GUI 이벤트 전송 실패 | 작업ID: {task_id} | 에러: {str(e)}")

    # 8. GGUI에 응답 반환
    response_payload = {
        "location_name": request.payload.location_name,
        "task_name": task_id,
        "success": True,
        "error_code": None,
        "error_message": None,
        "estimated_time": 15, # 임의의 예상 시간(분)
        "task_creation_time": creation_timestamp
    }
    
    logger.info(f"배송 작업 생성 완료 | 작업ID: {task_id} | 예상 시간: 15분")
    return CreateDeliveryTaskResponse(payload=response_payload)

@router.websocket("/ws/guest")
async def websocket_guest_endpoint(websocket: WebSocket):
    """Guest GUI를 위한 WebSocket 엔드포인트"""
    client_host = websocket.client.host if websocket.client else "unknown"
    logger.info(f"Guest WebSocket 연결 요청 | 클라이언트: {client_host}")
    
    await manager.connect(websocket, "guest")
    log_websocket_event("연결", "guest", f"호스트: {client_host}")
    
    try:
        while True:
            message = await websocket.receive_text()
            logger.debug(f"Guest WebSocket 메시지 수신 | 내용: {message}")
    except WebSocketDisconnect:
        manager.disconnect(websocket, "guest")
        log_websocket_event("연결 해제", "guest", f"호스트: {client_host}")

@router.websocket("/ws/staff")
async def websocket_staff_endpoint(websocket: WebSocket):
    """Staff GUI를 위한 WebSocket 엔드포인트"""
    client_host = websocket.client.host if websocket.client else "unknown"
    logger.info(f"Staff WebSocket 연결 요청 | 클라이언트: {client_host}")
    
    await manager.connect(websocket, "staff")
    log_websocket_event("연결", "staff", f"호스트: {client_host}")
    
    try:
        while True:
            message = await websocket.receive_text()
            logger.debug(f"Staff WebSocket 메시지 수신 | 내용: {message}")
    except WebSocketDisconnect:
        manager.disconnect(websocket, "staff")
        log_websocket_event("연결 해제", "staff", f"호스트: {client_host}")