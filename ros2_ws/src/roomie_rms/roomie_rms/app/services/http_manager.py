"""
HTTP API 통합 관리자
FastAPI의 모든 HTTP 엔드포인트를 클래스 기반으로 관리합니다.
"""

import json
from datetime import datetime
from typing import Dict, Any, Optional, List
from fastapi import APIRouter, HTTPException, Request, Depends

from app.config import settings
from app.services import db_manager
from app.services.websocket_manager import manager as websocket_manager
from app.utils.logger import get_logger, log_database_operation
from app.utils.error_handler import safe_database_connection, database_transaction
from app.utils.exceptions import RoomieBaseException, raise_validation_error
from app.schemas.gui_models import *

logger = get_logger(__name__)

class HttpManager:
    """HTTP API 관리자"""
    
    def __init__(self):
        """HTTP Manager 초기화"""
        self.router = APIRouter()
        self._setup_routes()

    def _setup_routes(self):
        """HTTP API 라우터 설정"""
        
        @self.router.post("/get_food_menu", response_model=GetFoodMenuResponse)
        async def get_food_menu(request: GetFoodMenuRequest):
            """음식 메뉴 목록을 조회합니다."""
            payload = request.payload
            location_name = payload.location_name
            logger.info(
                "음식 메뉴 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "SGUI", "Method": "POST", "Path": "/api/gui/get_food_menu", "Location": location_name}
            )
            
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        # location_name으로 location_id 조회
                        location_id = None
                        if location_name:
                            cursor.execute("SELECT id FROM location WHERE name = %s", (location_name,))
                            location_result = cursor.fetchone()
                            if location_result:
                                location_id = location_result['id']
                                logger.info(
                                    f"위치 조회 성공: {location_name} -> {location_id}",
                                    category="API", subcategory="INFO",
                                    details={"Location": location_name, "LocationID": location_id}
                                )
                            else:
                                logger.warning(
                                    f"위치를 찾을 수 없음: {location_name}",
                                    category="API", subcategory="WARN",
                                    details={"Location": location_name}
                                )
                        
                        # 음식 메뉴 조회 (현재는 모든 메뉴를 반환, 향후 위치별 메뉴 차별화 가능)
                        cursor.execute("SELECT id, name, price, image FROM food")
                        results = cursor.fetchall()
                        log_database_operation("SELECT", "food", True, f"{len(results)}개 메뉴 조회")
                        
                        food_items = []
                        for row in results:
                            food_items.append(FoodItem(
                                id=row['id'],
                                name=row['name'],
                                price=row['price'],
                                image_path=row['image']
                            ))
                        
                        response_payload = GetFoodMenuResponsePayload(
                            menu_items=food_items,
                            estimated_time=settings.const.DEFAULT_ESTIMATED_TIME_MINUTES
                        )
                        
                        return GetFoodMenuResponse(
                            status="success",
                            message="메뉴 조회 성공",
                            payload=response_payload
                        )
            except RoomieBaseException as e:
                logger.error(
                    f"음식 메뉴 조회 실패: {e.message}",
                    category="API", subcategory="ERROR"
                )
                raise HTTPException(status_code=400, detail=e.message)
            except Exception as e:
                logger.error(
                    f"음식 메뉴 조회 중 예상치 못한 오류: {e}",
                    category="API", subcategory="ERROR"
                )
                raise HTTPException(status_code=500, detail="메뉴 조회 실패")

        @self.router.post("/get_supply_menu", response_model=GetSupplyMenuResponse)  
        async def get_supply_menu(request: GetSupplyMenuRequest):
            """물품 메뉴 목록을 조회합니다."""
            payload = request.payload
            location_name = payload.location_name
            logger.info(
                "물품 메뉴 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "SGUI", "Method": "POST", "Path": "/api/gui/get_supply_menu", "Location": location_name}
            )
            
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        # location_name으로 location_id 조회
                        location_id = None
                        if location_name:
                            cursor.execute("SELECT id FROM location WHERE name = %s", (location_name,))
                            location_result = cursor.fetchone()
                            if location_result:
                                location_id = location_result['id']
                                logger.info(
                                    f"위치 조회 성공: {location_name} -> {location_id}",
                                    category="API", subcategory="INFO",
                                    details={"Location": location_name, "LocationID": location_id}
                                )
                            else:
                                logger.warning(
                                    f"위치를 찾을 수 없음: {location_name}",
                                    category="API", subcategory="WARN",
                                    details={"Location": location_name}
                                )
                        
                        # 비품 메뉴 조회 (현재는 모든 비품을 반환, 향후 위치별 비품 차별화 가능)
                        cursor.execute("SELECT id, name, image FROM supply")
                        results = cursor.fetchall()
                        log_database_operation("SELECT", "supply", True, f"{len(results)}개 물품 조회")
                        
                        supply_items = []
                        for row in results:
                            supply_items.append(SupplyItem(
                                id=row['id'],
                                name=row['name'],
                                image_path=row['image']
                            ))
                        
                        response_payload = GetSupplyMenuResponsePayload(
                            menu_items=supply_items,
                            estimated_time=settings.const.DEFAULT_ESTIMATED_TIME_MINUTES
                        )
                        
                        return GetSupplyMenuResponse(
                            status="success",
                            message="물품 메뉴 조회 성공",
                            payload=response_payload
                        )
            except RoomieBaseException as e:
                logger.error(
                    f"물품 메뉴 조회 실패: {e.message}",
                    category="API", subcategory="ERROR"
                )
                raise HTTPException(status_code=400, detail=e.message)
            except Exception as e:
                logger.error(
                    f"물품 메뉴 조회 중 예상치 못한 오류: {e}",
                    category="API", subcategory="ERROR"
                )
                raise HTTPException(status_code=500, detail="물품 메뉴 조회 실패")

        @self.router.post("/get_locations", response_model=GetLocationsResponse)
        async def get_locations(request: GetLocationsRequest):
            """위치 목록을 조회합니다."""
            logger.info(
                "위치 목록 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/get_locations"}
            )
            
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        cursor.execute("SELECT id, name FROM location WHERE type = 'guest'")
                        results = cursor.fetchall()
                        log_database_operation("SELECT", "location", True, f"{len(results)}개 위치 조회")
                        
                        locations = []
                        for row in results:
                            locations.append(LocationInfo(
                                id=row['id'],
                                name=row['name']
                            ))
                        
                        response_payload = GetLocationsResponsePayload(locations=locations)
                        return GetLocationsResponse(
                            status="success",
                            message="위치 조회 성공",
                            payload=response_payload
                        )
            except RoomieBaseException as e:
                logger.error(
                    f"위치 목록 조회 실패: {e.message}",
                    category="API", subcategory="ERROR"
                )
                raise HTTPException(status_code=400, detail=e.message)
            except Exception as e:
                logger.error(
                    f"위치 목록 조회 중 예상치 못한 오류: {e}",
                    category="API", subcategory="ERROR"
                )
                raise HTTPException(status_code=500, detail="위치 조회 실패")

        @self.router.post("/create_delivery_task", response_model=CreateDeliveryTaskResponse)
        async def create_delivery_task(request_data: CreateDeliveryTaskRequest, request: Request):
            """배송 작업을 생성합니다."""
            payload = request_data.payload
            logger.info(
                "작업 생성 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/create_delivery_task", "Payload": payload.model_dump_json()}
            )
            
            try:
                rms_node = request.app.state.rms_node
                result = rms_node.task_manager.create_delivery_task(
                    location_name=payload.location_name,
                    task_type_name=payload.task_type_name,
                    order_details=payload.order_details
                )
                
                task_id = result["task_id"]
                order_id = result["order_id"]
                
                # WebSocket으로 새 주문 알림 전송
                order_items_list = []
                if isinstance(payload.order_details, dict):
                    # order_details가 딕셔너리인 경우 (예: {"items": [OrderItem, ...]})
                    for items in payload.order_details.values():
                        for item in items:
                            order_items_list.append(item.model_dump())
                else:
                    # order_details가 직접 OrderItem 리스트인 경우
                    for item in payload.order_details:
                        order_items_list.append(item.model_dump())
                
                # WebSocket 이벤트 데이터 구성 (명세서에 맞춘 구조)
                if payload.task_type_name == "음식배송":
                    event_data = {
                        "type": "event",
                        "action": "food_order_creation",
                        "payload": {
                            "task_id": str(task_id),
                            "location": payload.location_name,
                            "order_details": order_items_list
                        }
                    }
                    websocket_manager.broadcast_to_group("staff", event_data)
                    logger.info(
                        "SGUI로 음식 주문 생성 이벤트 전송",
                        category="API", subcategory="WS-EVENT",
                        details={"Target": "Staff", "Event": "food_order_creation", "TaskID": task_id}
                    )
                    
                elif payload.task_type_name == "비품배송":
                    event_data = {
                        "type": "event", 
                        "action": "supply_order_creation",
                        "payload": {
                            "task_id": str(task_id),
                            "location": payload.location_name,
                            "order_details": order_items_list
                        }
                    }
                    websocket_manager.broadcast_to_group("staff", event_data)
                    logger.info(
                        "SGUI로 비품 주문 생성 이벤트 전송",
                        category="API", subcategory="WS-EVENT",
                        details={"Target": "Staff", "Event": "supply_order_creation", "TaskID": task_id}
                    )
                
                response_payload = CreateDeliveryTaskResponsePayload(
                    task_id=task_id,
                    order_id=order_id if order_id is not None else 0,  # order_id가 None인 경우 0으로 설정
                    success=True,
                    message="배송 작업이 성공적으로 생성되었습니다.",
                    estimated_time=settings.const.DEFAULT_ESTIMATED_TIME_MINUTES,
                    task_creation_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                )
                
                logger.info(
                    "작업 생성 성공 및 예상 시간 응답",
                    category="API", subcategory="HTTP-RES",
                    details={"TaskID": task_id, "Client": "GGUI"}
                )
                return CreateDeliveryTaskResponse(
                    status="success",
                    message="배송 작업이 성공적으로 생성되었습니다.",
                    payload=response_payload
                )
                
            except RoomieBaseException as e:
                logger.error(f"작업 생성 실패: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=400, detail=e.message)
            except Exception as e:
                logger.error(f"예상치 못한 오류 발생: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="서버 내부 오류")

        @self.router.post("/change_task_status", response_model=TaskStatusChangeResponse)
        async def change_task_status(request_data: TaskStatusChangeRequest, request: Request):
            """작업 상태를 변경합니다."""
            payload = request_data.payload
            logger.info(
                f"작업 상태 변경 요청: {payload.task_id} -> {payload.new_status}",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "SGUI", "TaskID": payload.task_id, "NewStatus": payload.new_status}
            )
            
            try:
                rms_node = request.app.state.rms_node
                
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        status_id = settings.db_consts.task_status.get(payload.new_status)
                        if not status_id:
                            raise_validation_error(f"알 수 없는 상태 값: {payload.new_status}")
                        
                        cursor.execute("UPDATE task SET task_status_id = %s WHERE id = %s", (status_id, payload.task_id))
                        log_database_operation("UPDATE", "task", True, f"Task {payload.task_id} 상태 변경: {payload.new_status}", "INFO")

                # 로봇 할당 로직 트리거
                if payload.new_status == "준비 완료":
                    robot_id = rms_node.robot_manager.get_available_robot()
                    # threading.Thread(target=rms_node.task_manager.execute_task_assignment, args=(robot_id,)).start() # 비동기 처리 제거
                    rms_node.task_manager.execute_task_assignment(robot_id) # 동기 처리

                response_payload = TaskStatusChangeResponsePayload(
                    success=True, 
                    message="상태가 성공적으로 변경되었습니다."
                )
                logger.info(
                    "작업 상태 변경 완료",
                    category="API", subcategory="HTTP-RES",
                    details={"TaskID": payload.task_id}
                )
                return TaskStatusChangeResponse(
                    status="success",
                    message="상태가 성공적으로 변경되었습니다.",
                    payload=response_payload
                )
                
            except RoomieBaseException as e:
                logger.error(f"작업 상태 변경 실패: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=400, detail=e.message)
            except Exception as e:
                logger.error(f"작업 상태 변경 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="작업 상태 변경 실패")

        @self.router.get("/get_tasks", response_model=TaskListResponse)
        async def get_task_list(
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None,
            task_type: Optional[str] = None,
            task_status: Optional[str] = None,
            destination: Optional[str] = None
        ):
            """작업 목록을 조회합니다."""
            logger.info(
                "AGUI 작업 목록 조회 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "AGUI", "Method": "GET", "Path": "/api/gui/get_tasks"}
            )
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
                
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        cursor.execute(query, tuple(params))
                        tasks_from_db = cursor.fetchall()
                        
                        task_list = [TaskInDB(
                            task_id=row['id'],
                            task_type=row['task_type'],
                            task_status=row['task_status'],
                            destination=row['destination'],
                            robot_id=row['robot_id'],
                            task_creation_time=row['task_creation_time'],
                            task_completion_time=row['task_completion_time']
                        ) for row in tasks_from_db]
                        
                        log_database_operation("SELECT", "task", True, f"{len(task_list)}개 작업 목록 조회", "INFO")
                        logger.info(
                            f"{len(task_list)}개의 작업 목록을 AGUI로 전송합니다.",
                            category="API", subcategory="HTTP-RES",
                            details={"Client": "AGUI", "Count": len(task_list)}
                        )
                        return TaskListResponse(tasks=task_list)

            except RoomieBaseException as e:
                logger.error(f"작업 목록 조회 중 DB 오류: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail=e.message)
            except Exception as e:
                logger.error(f"작업 목록 조회 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="작업 목록 조회 실패")

        @self.router.get("/get_robots", response_model=RobotListResponse)
        async def get_robot_list(
            robot_id: Optional[int] = None,
            model_name: Optional[str] = None,
            robot_status: Optional[str] = None
        ):
            """로봇 목록을 조회합니다."""
            logger.info(
                "AGUI 로봇 목록 조회 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "AGUI", "Method": "GET", "Path": "/api/gui/get_robots"}
            )
            query = """
                SELECT
                    r.id as robot_id,
                    r.model_name,
                    r.installation_date,
                    rs.name as robot_status,
                    l.name as current_location,
                    rcs.battery_level,
                    rcs.is_charging
                FROM robot r
                JOIN robot_status rs ON r.current_status_id = rs.id
                LEFT JOIN location l ON r.current_location_id = l.id
                LEFT JOIN robot_current_state rcs ON r.id = rcs.robot_id
                WHERE 1=1
            """
            params = []
            
            if robot_id:
                query += " AND r.id = %s"
                params.append(robot_id)
            if model_name:
                query += " AND r.model_name = %s"
                params.append(model_name)
            if robot_status:
                query += " AND rs.name = %s"
                params.append(robot_status)
                
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        cursor.execute(query, tuple(params))
                        robots_from_db = cursor.fetchall()
                        
                        robot_list = [RobotInDB(
                            robot_id=row['robot_id'],
                            model_name=row['model_name'],
                            installation_date=row['installation_date'],
                            robot_status=row['robot_status'],
                            current_location=row['current_location'],
                            battery_level=row['battery_level'],
                            is_charging=row['is_charging']
                        ) for row in robots_from_db]
                        
                        log_database_operation("SELECT", "robot", True, f"{len(robot_list)}개 로봇 목록 조회")
                        logger.info(
                            f"{len(robot_list)}개의 로봇 목록을 AGUI로 전송합니다.",
                            category="API", subcategory="HTTP-RES",
                            details={"Client": "AGUI", "Count": len(robot_list)}
                        )
                        return RobotListResponse(robots=robot_list)

            except RoomieBaseException as e:
                logger.error(f"로봇 목록 조회 중 DB 오류: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail=e.message)
            except Exception as e:
                logger.error(f"로봇 목록 조회 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="로봇 목록 조회 실패")

        # --- GGUI HTTP 동기 인터페이스 추가 ---
        
        @self.router.post("/create_call_task", response_model=CreateCallTaskResponse)
        async def create_call_task(request: CreateCallTaskRequest, request_obj: Request):
            """호출 작업 생성 요청"""
            payload = request.payload
            location_name = payload.location
            logger.info(
                "호출 작업 생성 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/create_call_task", "Location": location_name}
            )
            
            try:
                # task_manager를 통해 실제 호출 작업 생성 (task_type_name을 "호출"로 설정)
                rms_node = request_obj.app.state.rms_node
                result = rms_node.task_manager.create_delivery_task(
                    location_name=location_name,
                    task_type_name="호출",
                    order_details={}  # 호출 작업은 주문 상세 정보가 없음
                )
                
                task_id = result["task_id"]
                
                # WebSocket으로 호출 알림 전송
                event_data = {
                    "type": "event",
                    "action": "call_request_acceptance",
                    "payload": {
                        "task_name": f"TASK_{task_id}",
                        "estimated_wait_time": 15
                    }
                }
                websocket_manager.broadcast_to_group("guest", event_data)
                logger.info(
                    "GGUI에 호출 수락 알림 전송",
                    category="API", subcategory="WS-EVENT",
                    details={"Target": "Guest", "Event": "call_request_acceptance", "TaskID": task_id}
                )
                
                response_payload = CreateCallTaskResponsePayload(
                    location_name=location_name,
                    task_name=f"TASK_{task_id}",
                    success=True,
                    task_creation_time=datetime.now().isoformat() + "+09:00"
                )
                
                logger.info(
                    "호출 작업 생성 완료",
                    category="API", subcategory="HTTP-RES",
                    details={"TaskID": task_id, "Client": "GGUI"}
                )
                return CreateCallTaskResponse(payload=response_payload)
                
            except RoomieBaseException as e:
                logger.error(f"호출 작업 생성 실패: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=400, detail=e.message)
            except Exception as e:
                logger.error(f"호출 작업 생성 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="호출 작업 생성 실패")

        @self.router.post("/get_food_menu_ggui", response_model=GetFoodMenuGGUIResponse)
        async def get_food_menu_ggui(request: GetFoodMenuGGUIRequest):
            """GGUI용 음식 메뉴 요청"""
            payload = request.payload
            location_name = payload.location_name
            logger.info(
                "GGUI 음식 메뉴 요청",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/get_food_menu_ggui", "Location": location_name}
            )
            
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        # location_name으로 location_id 조회
                        location_id = None
                        if location_name:
                            cursor.execute("SELECT id FROM location WHERE name = %s", (location_name,))
                            location_result = cursor.fetchone()
                            if location_result:
                                location_id = location_result['id']
                                logger.info(
                                    f"GGUI 위치 조회 성공: {location_name} -> {location_id}",
                                    category="API", subcategory="INFO",
                                    details={"Location": location_name, "LocationID": location_id}
                                )
                            else:
                                logger.warning(
                                    f"GGUI 위치를 찾을 수 없음: {location_name}",
                                    category="API", subcategory="WARN",
                                    details={"Location": location_name}
                                )
                        
                        # 음식 메뉴 조회 (현재는 모든 메뉴를 반환, 향후 위치별 메뉴 차별화 가능)
                        cursor.execute("SELECT name, price, image FROM food")
                        results = cursor.fetchall()
                        
                        food_items = [FoodMenuItem(
                            food_name=row['name'],
                            price=row['price'],
                            image=row['image']
                        ) for row in results]
                        
                        response_payload = GetFoodMenuGGUIResponsePayload(food_items=food_items)
                        return GetFoodMenuGGUIResponse(payload=response_payload)
                        
            except Exception as e:
                logger.error(f"GGUI 음식 메뉴 조회 중 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="음식 메뉴 조회 실패")

        @self.router.post("/get_supply_menu_ggui", response_model=GetSupplyMenuGGUIResponse)
        async def get_supply_menu_ggui(request: GetSupplyMenuGGUIRequest):
            """GGUI용 비품 메뉴 요청"""
            payload = request.payload
            location_name = payload.location_name
            logger.info(
                "GGUI 비품 메뉴 요청",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/get_supply_menu_ggui", "Location": location_name}
            )
            
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        # location_name으로 location_id 조회
                        location_id = None
                        if location_name:
                            cursor.execute("SELECT id FROM location WHERE name = %s", (location_name,))
                            location_result = cursor.fetchone()
                            if location_result:
                                location_id = location_result['id']
                                logger.info(
                                    f"GGUI 위치 조회 성공: {location_name} -> {location_id}",
                                    category="API", subcategory="INFO",
                                    details={"Location": location_name, "LocationID": location_id}
                                )
                            else:
                                logger.warning(
                                    f"GGUI 위치를 찾을 수 없음: {location_name}",
                                    category="API", subcategory="WARN",
                                    details={"Location": location_name}
                                )
                        
                        # 비품 메뉴 조회 (현재는 모든 비품을 반환, 향후 위치별 비품 차별화 가능)
                        cursor.execute("SELECT name, image FROM supply")
                        results = cursor.fetchall()
                        
                        supply_items = [SupplyMenuItem(
                            supply_name=row['name'],
                            image=row['image']
                        ) for row in results]
                        
                        response_payload = GetSupplyMenuGGUIResponsePayload(supply_items=supply_items)
                        return GetSupplyMenuGGUIResponse(payload=response_payload)
                        
            except Exception as e:
                logger.error(f"GGUI 비품 메뉴 조회 중 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="비품 메뉴 조회 실패")

        @self.router.post("/create_delivery_task_ggui", response_model=CreateDeliveryTaskGGUIResponse)
        async def create_delivery_task_ggui(request: CreateDeliveryTaskGGUIRequest, request_obj: Request):
            """GGUI용 배송 작업 생성 요청"""
            payload = request.payload
            location_name = payload.location_name
            logger.info(
                "GGUI 배송 작업 생성 요청",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/create_delivery_task_ggui", "Location": location_name}
            )
            
            try:
                # task_manager를 통해 실제 배송 작업 생성
                rms_node = request_obj.app.state.rms_node
                result = rms_node.task_manager.create_delivery_task(
                    location_name=location_name,
                    task_type_name=payload.task_type_name,
                    order_details=payload.order_details
                )
                
                task_id = result["task_id"]
                order_id = result["order_id"]
                
                # WebSocket으로 새 주문 알림 전송
                order_items_list = []
                if isinstance(payload.order_details, dict):
                    # order_details가 딕셔너리인 경우 (예: {"items": [OrderItem, ...]})
                    for items in payload.order_details.values():
                        for item in items:
                            if hasattr(item, 'model_dump'):
                                order_items_list.append(item.model_dump())
                            else:
                                order_items_list.append(item)
                else:
                    # order_details가 직접 리스트인 경우
                    for item in payload.order_details:
                        if hasattr(item, 'model_dump'):
                            order_items_list.append(item.model_dump())
                        else:
                            order_items_list.append(item)
                
                # WebSocket 이벤트 데이터 구성 (명세서에 맞춘 구조)
                if payload.task_type_name == "음식배송":
                    event_data = {
                        "type": "event",
                        "action": "food_order_creation",
                        "payload": {
                            "task_id": str(task_id),
                            "location": location_name,
                            "order_details": order_items_list
                        }
                    }
                    websocket_manager.broadcast_to_group("staff", event_data)
                    logger.info(
                        "SGUI에 음식 주문 생성 알림 전송",
                        category="API", subcategory="WS-EVENT",
                        details={"Target": "Staff", "Event": "food_order_creation", "TaskID": task_id}
                    )
                    
                elif payload.task_type_name == "비품배송":
                    event_data = {
                        "type": "event", 
                        "action": "supply_order_creation",
                        "payload": {
                            "task_id": str(task_id),
                            "location": location_name,
                            "order_details": order_items_list
                        }
                    }
                    websocket_manager.broadcast_to_group("staff", event_data)
                    logger.info(
                        "SGUI에 비품 주문 생성 알림 전송",
                        category="API", subcategory="WS-EVENT",
                        details={"Target": "Staff", "Event": "supply_order_creation", "TaskID": task_id}
                    )
                
                response_payload = CreateDeliveryTaskGGUIResponsePayload(
                    location_name=location_name,
                    task_name=f"TASK_{task_id}",
                    success=True,
                    estimated_time=settings.const.DEFAULT_ESTIMATED_TIME_MINUTES,
                    task_creation_time=datetime.now().isoformat() + "+09:00"
                )
                
                logger.info(
                    "GGUI 배송 작업 생성 완료",
                    category="API", subcategory="HTTP-RES",
                    details={"TaskID": task_id, "Client": "GGUI"}
                )
                return CreateDeliveryTaskGGUIResponse(payload=response_payload)
                
            except RoomieBaseException as e:
                logger.error(f"GGUI 작업 생성 실패: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=400, detail=e.message)
            except Exception as e:
                logger.error(f"GGUI 배송 작업 생성 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="배송 작업 생성 실패")

        @self.router.post("/get_call_history", response_model=GetCallHistoryResponse)
        async def get_call_history(request: GetCallHistoryRequest):
            """호출 내역 조회 요청"""
            payload = request.payload
            logger.info(
                "호출 내역 조회 요청",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/get_call_history", "TaskName": payload.task_name}
            )
            
            try:
                # TODO: 실제 호출 내역 조회 로직 구현
                response_payload = GetCallHistoryResponsePayload(
                    location_name=payload.location_name,
                    task_name=payload.task_name,
                    task_type_name="호출",
                    estimated_time=5,
                    robot_status=RobotStatus(x=0.0, y=0.0, floor_id=0)
                )
                
                return GetCallHistoryResponse(payload=response_payload)
                
            except Exception as e:
                logger.error(f"호출 내역 조회 중 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="호출 내역 조회 실패")

        @self.router.post("/get_order_history", response_model=GetOrderHistoryResponse)
        async def get_order_history(request: GetOrderHistoryRequest):
            """주문 내역 조회 요청"""
            payload = request.payload
            logger.info(
                "주문 내역 조회 요청",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/get_order_history", "TaskName": payload.task_name}
            )
            
            try:
                # TODO: 실제 주문 내역 조회 로직 구현
                response_payload = GetOrderHistoryResponsePayload(
                    request_location=payload.request_location,
                    task_name=payload.task_name,
                    task_type_name=payload.task_type_name,
                    estimated_time=55,
                    task_creation_time=datetime.now().isoformat() + "+09:00",
                    robot_assignment_time=datetime.now().isoformat() + "+09:00",
                    pickup_completion_time=datetime.now().isoformat() + "+09:00",
                    delivery_arrival_time=None
                )
                
                return GetOrderHistoryResponse(payload=response_payload)
                
            except Exception as e:
                logger.error(f"주문 내역 조회 중 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="주문 내역 조회 실패")

# 글로벌 인스턴스 생성
manager = HttpManager()

