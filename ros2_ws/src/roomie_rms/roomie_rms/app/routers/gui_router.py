from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, HTTPException
from app.schemas.gui_models import *
from app.services.websocket_manager import manager
from app.utils.logger import logger, log_task_creation, log_websocket_event, get_current_timestamp
from app.services.db_manager import db_manager
from typing import List, Optional
import time
from datetime import datetime, timezone
import mysql.connector

router = APIRouter()

@router.post("/get_food_menu", response_model=GetFoodMenuResponse)
async def get_food_menu(request: GetFoodMenuRequest):
    """
    Guest GUI로부터 음식 메뉴 요청을 받아 DB에서 조회 후 반환
    """
    logger.info(f"음식 메뉴 요청 수신 | 요청 데이터: {request.payload}")
    
    conn = db_manager.get_connection()
    if not conn:
        raise HTTPException(status_code=503, detail="데이터베이스 연결에 실패했습니다.")

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT name, price, image FROM food")
        food_from_db = cursor.fetchall()
        
        # DB 컬럼명(name)을 Pydantic 모델 필드명(food_name)에 맞게 변환
        food_items = [
            {"food_name": item['name'], "price": item['price'], "image": item['image']}
            for item in food_from_db
        ]
        
        response_payload = {"food_items": food_items}
        logger.debug(f"음식 메뉴 응답 생성 | 메뉴 개수: {len(food_items)}개")
        return GetFoodMenuResponse(payload=response_payload)
        
    except mysql.connector.Error as err:
        logger.error(f"음식 메뉴 조회 중 DB 오류 발생: {err}")
        raise HTTPException(status_code=500, detail=f"데이터베이스 오류: {err}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()


@router.post("/create_delivery_task", response_model=CreateDeliveryTaskResponse)
async def create_delivery_task(request: CreateDeliveryTaskRequest):
    """
    GGUI로부터 배송 작업을 생성하고 DB에 저장 후 SGUI에 알림 전송
    """
    logger.info(f"배송 작업 생성 요청 수신 | 위치: {request.payload.location_name} | 작업 타입: {request.payload.task_type_name}")
    
    conn = db_manager.get_connection()
    if not conn:
        raise HTTPException(status_code=503, detail="데이터베이스 연결에 실패했습니다.")

    cursor = None
    try:
        cursor = conn.cursor(dictionary=True)
        
        # location_id와 task_type_id 조회
        cursor.execute("SELECT id FROM location WHERE name = %s", (request.payload.location_name,))
        location_result = cursor.fetchone()
        if not location_result:
            raise HTTPException(status_code=404, detail=f"요청한 위치를 찾을 수 없습니다: {request.payload.location_name}")
        location_id = location_result['id']
        
        cursor.execute("SELECT id FROM task_type WHERE name = %s", (request.payload.task_type_name,))
        task_type_result = cursor.fetchone()
        if not task_type_result:
            raise HTTPException(status_code=404, detail=f"요청한 작업 타입을 찾을 수 없습니다: {request.payload.task_type_name}")
        task_type_id = task_type_result['id']

        # 초기 상태 '접수됨' (id=0)으로 설정
        task_status_id = 0
        creation_timestamp = get_current_timestamp()

        # 트랜잭션 시작 (중간에 오류 발생 시 롤백)
        conn.start_transaction()

        # task 테이블에 작업 삽입
        task_query = """
            INSERT INTO task (type_id, task_status_id, location_id, task_creation_time)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(task_query, (task_type_id, task_status_id, location_id, creation_timestamp))
        task_id = cursor.lastrowid
        
        order_items = request.payload.order_details.get("items", [])
        
        # 음식 주문인 경우 order 및 food_order_item 테이블에 기록
        if request.payload.task_type_name == '음식배송' and order_items:
            # order 테이블에 주문 삽입
            total_price = sum(item.price * item.quantity for item in order_items)
            order_query = "INSERT INTO `order` (task_id, location_id, total_price) VALUES (%s, %s, %s)"
            cursor.execute(order_query, (task_id, location_id, total_price))
            order_id = cursor.lastrowid
            
            # food_order_item 테이블에 각 항목 삽입
            for item in order_items:
                cursor.execute("SELECT id FROM food WHERE name = %s", (item.name,))
                food_result = cursor.fetchone()
                if not food_result:
                    raise HTTPException(status_code=404, detail=f"주문 항목을 찾을 수 없습니다: {item.name}")
                food_id = food_result['id']
                item_query = "INSERT INTO food_order_item (order_id, food_id, quantity) VALUES (%s, %s, %s)"
                cursor.execute(item_query, (order_id, food_id, item.quantity))

        # 트랜잭션 커밋
        conn.commit()

        logger.info(f"DB에 배송 작업 저장 완료 | 작업ID: {task_id}")
        
        # SGUI에 이벤트 전송
        event_payload = {
            "task_id": task_id,
            "request_location": request.payload.location_name,
            "order_details": {
                "items": [item.model_dump() for item in order_items]
            },
            "created_at": creation_timestamp
        }
        sdui_event = FoodOrderCreationEvent(payload=event_payload)
        await manager.broadcast_to("staff", sdui_event.model_dump())
        logger.info(f"Staff GUI에 주문 이벤트 전송 완료 | 작업ID: {task_id}")

        # GGUI에 성공 응답 반환
        response_payload = {
            "location_name": request.payload.location_name,
            "task_name": str(task_id),
            "success": True,
            "estimated_time": 15, # 임의의 예상 시간(분)
            "task_creation_time": creation_timestamp
        }
        return CreateDeliveryTaskResponse(payload=response_payload)

    except mysql.connector.Error as err:
        logger.error(f"작업 생성 중 DB 오류 발생: {err}")
        if conn.in_transaction:
            conn.rollback() # 오류 발생 시 롤백
        raise HTTPException(status_code=500, detail=f"데이터베이스 오류: {err}")
    finally:
        if conn and conn.is_connected():
            if cursor:
                cursor.close()
            conn.close()


@router.websocket("/ws/guest/{location_name}")
async def websocket_guest_endpoint(websocket: WebSocket, location_name: str):
    """Guest GUI를 위한 WebSocket 엔드포인트 (특정 위치 기반)"""
    await manager.connect(websocket, "guest", location_name)
    log_websocket_event("연결", "guest", f"ID: {location_name}")
    try:
        while True:
            # 연결을 유지하고 클라이언트로부터의 메시지를 대기
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        log_websocket_event("연결 해제", "guest", f"ID: {location_name}")

@router.websocket("/ws/staff/{staff_id}")
async def websocket_staff_endpoint(websocket: WebSocket, staff_id: str):
    """Staff GUI를 위한 WebSocket 엔드포인트 (직원 ID 기반)"""
    await manager.connect(websocket, "staff", staff_id)
    log_websocket_event("연결", "staff", f"ID: {staff_id}")
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        log_websocket_event("연결 해제", "staff", f"ID: {staff_id}")

@router.websocket("/ws/admin/{admin_id}")
async def websocket_admin_endpoint(websocket: WebSocket, admin_id: str):
    """Admin GUI를 위한 WebSocket 엔드포인트 (관리자 ID 기반)"""
    await manager.connect(websocket, "admin", admin_id)
    log_websocket_event("연결", "admin", f"ID: {admin_id}")
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        log_websocket_event("연결 해제", "admin", f"ID: {admin_id}")


# ----------------------------------------------------------------
# AGUI (Admin GUI) 라우터
# ----------------------------------------------------------------

@router.get("/tasks", response_model=TaskListResponse)
def get_task_list(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    task_type: Optional[str] = None,
    task_status: Optional[str] = None,
    destination: Optional[str] = None
):
    """
    AGUI로부터 작업 목록 조회 요청을 받아 필터링된 결과를 반환합니다.
    """
    logger.info("AGUI 작업 목록 조회 요청 수신")
    query = """
        SELECT
            t.id,
            tt.name as task_type,
            ts.name as task_status,
            l.name as destination,
            t.robot_id,
            t.task_creation_time,
            t.task_completion_time
        FROM task t
        JOIN task_type tt ON t.type_id = tt.id
        JOIN task_status ts ON t.task_status_id = ts.id
        JOIN location l ON t.location_id = l.id
        WHERE 1=1
    """
    params = []
    
    if start_date:
        query += " AND t.task_creation_time >= %s"
        params.append(start_date)
    if end_date:
        query += " AND t.task_creation_time <= %s"
        params.append(end_date)
    if task_type:
        query += " AND tt.name = %s"
        params.append(task_type)
    if task_status:
        query += " AND ts.name = %s"
        params.append(task_status)
    if destination:
        query += " AND l.name = %s"
        params.append(destination)
        
    conn = db_manager.get_connection()
    if not conn:
        raise HTTPException(status_code=503, detail="데이터베이스 연결에 실패했습니다.")
        
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, tuple(params))
        tasks_from_db = cursor.fetchall()
        
        # Pydantic 모델로 변환
        task_list = [TaskInDB(
            task_id=row['id'],
            task_type=row['task_type'],
            task_status=row['task_status'],
            destination=row['destination'],
            robot_id=row['robot_id'],
            task_creation_time=row['task_creation_time'],
            task_completion_time=row['task_completion_time']
        ) for row in tasks_from_db]
        
        logger.info(f"{len(task_list)}개의 작업 목록을 AGUI로 전송합니다.")
        return TaskListResponse(tasks=task_list)

    except mysql.connector.Error as err:
        logger.error(f"작업 목록 조회 중 DB 오류 발생: {err}")
        raise HTTPException(status_code=500, detail=f"데이터베이스 오류: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


@router.get("/robots", response_model=RobotListResponse)
def get_robot_list(
    robot_id: Optional[int] = None,
    model_name: Optional[str] = None,
    robot_status: Optional[str] = None
):
    """
    AGUI로부터 로봇 목록 조회 요청을 받아 필터링된 결과를 반환합니다.
    """
    logger.info("AGUI 로봇 목록 조회 요청 수신")
    query = """
        SELECT
            r.id as robot_id,
            r.model_name,
            r.installation_date,
            rs.name as task_status,
            l.name as current_location,
            rcs.battery_level,
            e.name as error_code
        FROM robot r
        LEFT JOIN robot_current_state rcs ON r.id = rcs.robot_id
        LEFT JOIN robot_status rs ON rcs.robot_status_id = rs.id
        LEFT JOIN location l ON rcs.location_id = l.id
        LEFT JOIN error e ON rcs.error_id = e.id
        WHERE 1=1
    """
    params = []

    if robot_id is not None:
        query += " AND r.id = %s"
        params.append(robot_id)
    if model_name:
        query += " AND r.model_name = %s"
        params.append(model_name)
    if robot_status:
        query += " AND rs.name = %s"
        params.append(robot_status)

    conn = db_manager.get_connection()
    if not conn:
        raise HTTPException(status_code=503, detail="데이터베이스 연결에 실패했습니다.")

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, tuple(params))
        robots_from_db = cursor.fetchall()

        robot_list = [RobotInDB(
            robot_id=row['robot_id'],
            model_name=row['model_name'],
            installation_date=row['installation_date'],
            current_location=row['current_location'],
            battery_level=row['battery_level'],
            task_status=row['task_status'],
            has_error=bool(row['error_code']),
            error_code=row['error_code']
        ) for row in robots_from_db]
        
        logger.info(f"{len(robot_list)}개의 로봇 목록을 AGUI로 전송합니다.")
        return RobotListResponse(robots=robot_list)

    except mysql.connector.Error as err:
        logger.error(f"로봇 목록 조회 중 DB 오류 발생: {err}")
        raise HTTPException(status_code=500, detail=f"데이터베이스 오류: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()