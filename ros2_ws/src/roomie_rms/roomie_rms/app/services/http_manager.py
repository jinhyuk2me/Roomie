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
        
        # --- GGUI HTTP 동기 인터페이스 ---
        
        @self.router.post("/create_call_task", response_model=CreateCallTaskResponse)
        async def create_call_task(request: CreateCallTaskRequest, request_obj: Request):
            """(GGUI) 호출 작업 생성 요청"""
            payload = request.payload
            location_name = payload.location
            logger.info(
                "GGUI 호출 작업 생성 요청 수신",
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
                await websocket_manager.broadcast_to("guest", json.dumps(event_data))
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
                
                response = CreateCallTaskResponse(payload=response_payload)
                logger.info(
                    "GGUI 호출 작업 생성 응답 전송",
                    category="API", subcategory="HTTP-RES",
                    details={"TaskID": task_id, "Client": "GGUI", "Response": response.model_dump_json()}
                )
                return response
                
            except RoomieBaseException as e:
                logger.error(f"호출 작업 생성 실패: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=400, detail=e.message)
            except Exception as e:
                logger.error(f"호출 작업 생성 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="호출 작업 생성 실패")

        @self.router.post("/get_food_menu", response_model=GetFoodMenuResponse)
        async def get_food_menu(request: GetFoodMenuRequest):
            """(GGUI) 음식 메뉴 요청"""
            payload = request.payload
            location_name = payload.location_name
            logger.info(
                "GGUI 음식 메뉴 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/get_food_menu", "Location": location_name}
            )
            
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        # 음식 메뉴 조회
                        cursor.execute("SELECT name, price, image FROM food")
                        results = cursor.fetchall()
                        
                        food_items = [FoodMenuItem(
                            food_name=row['name'],
                            price=row['price'],
                            image=row['image']
                        ) for row in results]
                        
                        response_payload = GetFoodMenuResponsePayload(food_items=food_items)
                        response = GetFoodMenuResponse(payload=response_payload)
                        logger.info(
                            "GGUI 음식 메뉴 응답 전송",
                            category="API", subcategory="HTTP-RES",
                            details={"Client": "GGUI", "Response": response.model_dump_json()}
                        )
                        return response
                        
            except Exception as e:
                logger.error(f"GGUI 음식 메뉴 조회 중 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="음식 메뉴 조회 실패")

        @self.router.post("/get_supply_menu", response_model=GetSupplyMenuResponse)
        async def get_supply_menu(request: GetSupplyMenuRequest):
            """(GGUI) 비품 메뉴 요청"""
            payload = request.payload
            location_name = payload.location_name
            logger.info(
                "GGUI 비품 메뉴 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/get_supply_menu", "Location": location_name}
            )
            
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        # 비품 메뉴 조회
                        cursor.execute("SELECT name, image FROM supply")
                        results = cursor.fetchall()
                        
                        supply_items = [SupplyMenuItem(
                            supply_name=row['name'],
                            image=row['image']
                        ) for row in results]
                        
                        response_payload = GetSupplyMenuResponsePayload(supply_items=supply_items)
                        response = GetSupplyMenuResponse(payload=response_payload)
                        logger.info(
                            "GGUI 비품 메뉴 응답 전송",
                            category="API", subcategory="HTTP-RES",
                            details={"Client": "GGUI", "Response": response.model_dump_json()}
                        )
                        return response
                        
            except Exception as e:
                logger.error(f"GGUI 비품 메뉴 조회 중 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="비품 메뉴 조회 실패")

        @self.router.post("/create_delivery_task", response_model=CreateDeliveryTaskResponse)
        async def create_delivery_task(request: CreateDeliveryTaskRequest, request_obj: Request):
            """(GGUI) 배송 작업 생성 요청"""
            payload = request.payload
            location_name = payload.location_name
            logger.info(
                "GGUI 배송 작업 생성 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/create_delivery_task", "Payload": payload.model_dump_json()}
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
                
                # WebSocket으로 SGUI에 새 주문 알림 전송
                raw_items = []
                if isinstance(payload.order_details, dict):
                    for value in payload.order_details.values():
                        if isinstance(value, list):
                            raw_items = value
                            break
                
                order_items_list = []
                if payload.task_type_name == "음식배송":
                    action_type = "food_order_creation"
                    # 음식의 경우 name, quantity, price를 모두 포함
                    for item in raw_items:
                        order_items_list.append({
                            "name": item.name,
                            "quantity": item.quantity,
                            "price": item.price if item.price is not None else 0 # price가 없는 경우 0으로 처리
                        })
                else: # 비품배송의 경우
                    action_type = "supply_order_creation"
                    # 비품의 경우 name, quantity만 포함 (명세서 기준)
                    for item in raw_items:
                        order_items_list.append({
                            "name": item.name,
                            "quantity": item.quantity
                        })
                
                # 1. event_data 변수 정의
                event_data = {
                    "type": "event",
                    "action": action_type,
                    "payload": {
                        "task_id": task_id,
                        "request_location": location_name,
                        "order_details": {"items": order_items_list}
                    }
                }
                
                # 2. 로그 기록
                logger.info(
                    f"SGUI로 '{action_type}' 이벤트 전송",
                    category="API", subcategory="WS-EVENT",
                    details={
                        "Target": "staff", 
                        "TaskID": task_id,
                        "Message": json.dumps(event_data)
                    }
                )
                
                # 3. 메시지 전송
                await websocket_manager.broadcast_to("staff", json.dumps(event_data))
                
                response_payload = CreateDeliveryTaskResponsePayload(
                    location_name=location_name,
                    task_name=f"TASK_{task_id}",
                    success=True,
                    estimated_time=settings.const.DEFAULT_ESTIMATED_TIME_MINUTES,
                    task_creation_time=datetime.now().isoformat() + "+09:00"
                )
                
                response = CreateDeliveryTaskResponse(payload=response_payload)
                logger.info(
                    "GGUI 배송 작업 생성 응답 전송",
                    category="API", subcategory="HTTP-RES",
                    details={"TaskID": task_id, "Client": "GGUI", "Response": response.model_dump_json()}
                )
                return response
                
            except RoomieBaseException as e:
                logger.error(f"GGUI 작업 생성 실패: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=400, detail=e.message)
            except Exception as e:
                logger.error(f"GGUI 배송 작업 생성 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="배송 작업 생성 실패")

        @self.router.post("/get_call_history", response_model=GetCallHistoryResponse)
        async def get_call_history(request: GetCallHistoryRequest):
            """(GGUI) 호출 내역 조회 요청"""
            payload = request.payload
            logger.info(
                "GGUI 호출 내역 조회 요청",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "GGUI", "Method": "POST", "Path": "/api/gui/get_call_history", "TaskName": payload.task_name}
            )
            
            try:
                # TODO: 실제 호출 내역 조회 로직 구현
                response_payload = GetCallHistoryResponsePayload(
                    location_name=payload.location_name,
                    task_name=payload.task_name,
                    task_type_name="호출", # task_name으로 조회해서 실제 타입 반환해야 함
                    estimated_time=5, # task_name으로 조회해서 계산해야 함
                    robot_status=RobotStatus(x=0.0, y=0.0, floor_id=0) # 로봇 상태 조회 로직 필요
                )
                
                response = GetCallHistoryResponse(payload=response_payload)
                logger.info(
                    "GGUI 호출 내역 조회 응답",
                    category="API", subcategory="HTTP-RES",
                    details={"Client": "GGUI", "Response": response.model_dump_json()}
                )
                return response
                
            except Exception as e:
                logger.error(f"GGUI 호출 내역 조회 중 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="GGUI 호출 내역 조회 실패")

        @self.router.post("/get_order_history", response_model=GetOrderHistoryResponse)
        async def get_order_history(request: GetOrderHistoryRequest):
            """(GGUI) 주문 내역 조회 요청"""
            payload = request.payload
            logger.info(
                "GGUI 주문 내역 조회 요청 수신",
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
                
                response = GetOrderHistoryResponse(payload=response_payload)
                logger.info(
                    "GGUI 주문 내역 조회 응답 전송",
                    category="API", subcategory="HTTP-RES",
                    details={"Client": "GGUI", "Response": response.model_dump_json()}
                )
                return response
                
            except Exception as e:
                logger.error(f"GGUI 주문 내역 조회 중 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="GGUI 주문 내역 조회 실패")

        # --- SGUI HTTP 동기 인터페이스 ---

        @self.router.post("/food_order_status_change", response_model=FoodOrderStatusChangeResponse)
        async def food_order_status_change(request_data: FoodOrderStatusChangeRequest, request: Request):
            """(SGUI) 음식 주문 작업 상태를 '준비 완료'로 변경합니다."""
            payload = request_data.payload
            task_id_str = payload.task_id
            
            logger.info(
                "SGUI 음식 주문 상태 변경 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "SGUI", "TaskID": task_id_str}
            )
            
            try:
                task_id = int(task_id_str.replace("TASK_", ""))
                new_status = "준비 완료"
                rms_node = request.app.state.rms_node
                
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        status_id = settings.db_consts.task_status.get(new_status)
                        if not status_id:
                            raise_validation_error(f"알 수 없는 상태 값: {new_status}")
                        
                        cursor.execute("UPDATE task SET task_status_id = %s WHERE id = %s", (status_id, task_id))
                        log_database_operation("UPDATE", "task", True, f"Task {task_id} 상태 변경: {new_status}", "INFO")

                # 로봇 할당 로직 트리거
                if new_status == "준비 완료":
                    robot_id = rms_node.robot_manager.get_available_robot()
                    rms_node.task_manager.execute_task_assignment(robot_id)

                response_payload = FoodOrderStatusChangeResponsePayload(
                    task_id=task_id_str,
                    status_changed="food_ready"
                )
                response = FoodOrderStatusChangeResponse(payload=response_payload)
                
                logger.info(
                    "SGUI 음식 주문 상태 변경 응답 전송",
                    category="API", subcategory="HTTP-RES",
                    details={"Client": "SGUI", "Response": response.model_dump_json()}
                )
                return response
                
            except RoomieBaseException as e:
                logger.error(f"SGUI 음식 주문 상태 변경 실패: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=400, detail=e.message)
            except Exception as e:
                logger.error(f"SGUI 음식 주문 상태 변경 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="SGUI 음식 주문 상태 변경 실패")

        # --- AGUI HTTP 동기 인터페이스 ---

        @self.router.post("/task_list", response_model=TaskListResponse)
        async def task_list(request: TaskListRequest):
            """(AGUI) 작업 목록을 조회합니다."""
            filters = request.payload.filters
            logger.info(
                "AGUI 작업 목록 조회 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "AGUI", "Method": "POST", "Path": "/api/gui/task_list", "Filters": filters.model_dump_json()}
            )
            query = """
                SELECT
                    t.id as task_id,
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
            
            if filters.start_date:
                query += " AND t.task_creation_time >= %s"
                params.append(filters.start_date)
            if filters.end_date:
                query += " AND t.task_creation_time <= %s"
                params.append(filters.end_date)
            if filters.task_type:
                query += " AND tt.name = %s"
                params.append(filters.task_type)
            if filters.task_status:
                query += " AND ts.name = %s"
                params.append(filters.task_status)
            if filters.destination:
                query += " AND l.name = %s"
                params.append(filters.destination)
                
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        cursor.execute(query, tuple(params))
                        tasks_from_db = cursor.fetchall()
                        
                        task_list = [TaskInDB(
                            task_id=row['task_id'],
                            task_type=row['task_type'],
                            task_status=row['task_status'],
                            destination=row['destination'],
                            robot_id=row['robot_id'],
                            task_creation_time=row['task_creation_time'],
                            task_completion_time=row['task_completion_time']
                        ) for row in tasks_from_db]
                        
                        log_database_operation("SELECT", "task", True, f"{len(task_list)}개 작업 목록 조회", "INFO")
                        response_payload = TaskListResponsePayload(tasks=task_list)
                        response = TaskListResponse(payload=response_payload)
                        logger.info(
                            "AGUI 작업 목록 응답 전송",
                            category="API", subcategory="HTTP-RES",
                            details={"Client": "AGUI", "Count": len(task_list)}
                        )
                        return response

            except RoomieBaseException as e:
                logger.error(f"작업 목록 조회 중 DB 오류: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail=e.message)
            except Exception as e:
                logger.error(f"작업 목록 조회 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="작업 목록 조회 실패")

        @self.router.post("/robot_list", response_model=RobotListResponse)
        async def robot_list(request: RobotListRequest):
            """(AGUI) 로봇 목록을 조회합니다."""
            filters = request.payload.filters
            logger.info(
                "AGUI 로봇 목록 조회 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "AGUI", "Method": "POST", "Path": "/api/gui/robot_list", "Filters": filters.model_dump_json()}
            )
            query = """
                SELECT
                    r.id as robot_id,
                    r.model_name,
                    r.installation_date,
                    rs.name as robot_status,
                    l.name as current_location,
                    rcs.battery_level,
                    e.name as error_code,
                    (CASE WHEN e.id IS NOT NULL THEN TRUE ELSE FALSE END) as has_error
                FROM robot r
                LEFT JOIN robot_status rs ON r.current_status_id = rs.id
                LEFT JOIN location l ON r.current_location_id = l.id
                LEFT JOIN robot_current_state rcs ON r.id = rcs.robot_id
                LEFT JOIN error e ON rcs.error_id = e.id
                WHERE 1=1
            """
            params = []
            
            if filters.robot_id:
                query += " AND r.id = %s"
                params.append(int(filters.robot_id.replace("ROBOT_", "")))
            if filters.model_name:
                query += " AND r.model_name = %s"
                params.append(filters.model_name)
            if filters.robot_status:
                query += " AND rs.name = %s"
                params.append(filters.robot_status)
                
            try:
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        cursor.execute(query, tuple(params))
                        robots_from_db = cursor.fetchall()
                        
                        robot_list = [RobotInDB(
                            robot_id=row['robot_id'],
                            model_name=row['model_name'],
                            installation_date=row['installation_date'],
                            current_location=row['current_location'],
                            battery_level=row['battery_level'],
                            task_status=row['robot_status'],
                            has_error=row['has_error'],
                            error_code=row['error_code']
                        ) for row in robots_from_db]
                        
                        log_database_operation("SELECT", "robot", True, f"{len(robot_list)}개 로봇 목록 조회")
                        response_payload = RobotListResponsePayload(robots=robot_list)
                        response = RobotListResponse(payload=response_payload)
                        logger.info(
                            "AGUI 로봇 목록 응답 전송",
                            category="API", subcategory="HTTP-RES",
                            details={"Client": "AGUI", "Count": len(robot_list)}
                        )
                        return response

            except RoomieBaseException as e:
                logger.error(f"로봇 목록 조회 중 DB 오류: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail=e.message)
            except Exception as e:
                logger.error(f"로봇 목록 조회 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="로봇 목록 조회 실패")

        @self.router.post("/task_detail", response_model=TaskDetailResponse)
        async def task_detail(request: TaskDetailRequest):
            """(AGUI) 작업 상세 정보를 조회합니다."""
            task_id_str = request.payload.task_id
            logger.info(
                "AGUI 작업 상세 정보 요청 수신",
                category="API", subcategory="HTTP-REQ",
                details={"Client": "AGUI", "Method": "POST", "Path": "/api/gui/task_detail", "TaskID": task_id_str}
            )
            
            try:
                task_id = int(task_id_str.replace("TASK_", ""))
                
                query = """
                    SELECT
                        robot_assignment_time,
                        pickup_completion_time,
                        delivery_arrival_time,
                        task_completion_time
                    FROM task
                    WHERE id = %s
                """
                
                with safe_database_connection(db_manager.get_connection) as conn:
                    with database_transaction(conn) as cursor:
                        cursor.execute(query, (task_id,))
                        task_details = cursor.fetchone()
                        
                        if not task_details:
                            raise HTTPException(status_code=404, detail=f"작업을 찾을 수 없습니다: {task_id_str}")
                            
                        def format_time(dt):
                            return dt.isoformat() + 'Z' if dt else None

                        response_payload = TaskDetailResponsePayload(
                            robot_assignment_time=format_time(task_details.get('robot_assignment_time')),
                            pickup_completion_time=format_time(task_details.get('pickup_completion_time')),
                            delivery_arrival_time=format_time(task_details.get('delivery_arrival_time')),
                            task_completion_time=format_time(task_details.get('task_completion_time'))
                        )
                        
                        response = TaskDetailResponse(payload=response_payload)
                        logger.info(
                            "AGUI 작업 상세 응답 전송",
                            category="API", subcategory="HTTP-RES",
                            details={"Client": "AGUI", "Response": response.model_dump_json()}
                        )
                        return response

            except ValueError:
                raise HTTPException(status_code=400, detail=f"잘못된 형식의 작업 ID: {task_id_str}")
            except RoomieBaseException as e:
                logger.error(f"작업 상세 정보 조회 중 DB 오류: {e.message}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail=e.message)
            except Exception as e:
                logger.error(f"작업 상세 정보 조회 중 예상치 못한 오류: {e}", category="API", subcategory="ERROR")
                raise HTTPException(status_code=500, detail="작업 상세 정보 조회 실패")

# 글로벌 인스턴스 생성
manager = HttpManager()

