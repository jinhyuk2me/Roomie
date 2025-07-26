import asyncio
import json
from datetime import datetime
from typing import Dict, Any

# ActionHandler를 사용하기 위해 임포트가 필요할 수 있습니다. (구조에 따라 다름)
# from app.services.action_handler import ActionHandler 

from app.utils.logger import get_logger, log_database_operation
from app.utils.error_handler import handle_exceptions, safe_database_connection, database_transaction
from app.utils.exceptions import raise_validation_error
from app.config import settings
from app.services import db_manager

logger = get_logger(__name__)

class TaskManager:
    """작업 생성, 할당 등 비즈니스 로직을 관리하는 클래스"""
    
    def __init__(self, robot_manager, action_handler):
        self.robot_manager = robot_manager
        self.action_handler = action_handler # ActionHandler 인스턴스를 저장

    def create_delivery_task(self, location_name: str, task_type_name: str, order_details: Dict[str, Any]) -> int:
        """API 요청으로부터 배송 작업을 생성합니다."""
        if not all([location_name, task_type_name, order_details]):
            raise_validation_error("필수 필드가 누락되었습니다.")

        with safe_database_connection(db_manager.get_connection) as conn:
            with database_transaction(conn) as cursor:
                # 1. 'location' 테이블에서 location_id 조회
                cursor.execute("SELECT id FROM location WHERE name = %s", (location_name,))
                location_result = cursor.fetchone()
                if not location_result:
                    raise_validation_error(f"알 수 없는 목적지: {location_name}")
                location_id = location_result['id']

                # 2. 'task' 테이블에 새로운 작업 삽입
                task_query = """
                    INSERT INTO task (type_id, task_status_id, location_id, task_creation_time)
                    VALUES (%s, %s, %s, %s)
                """
                creation_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                task_type_id = settings.db_consts.task_type[task_type_name]
                
                cursor.execute(task_query, (
                    task_type_id,
                    settings.db_consts.task_status[settings.const.TASK_STATUS_RECEIVED],
                    location_id,
                    creation_time
                ))
                task_id = cursor.lastrowid
                
                # 3. 'order' 테이블에 주문 정보 삽입 (task_type_id가 0 또는 1인 경우에만)
                order_id = None
                if task_type_id in [0, 1]:
                    # 초기 total_price는 0으로 설정 (나중에 아이템 처리 시 업데이트)
                    order_query = "INSERT INTO `order` (task_id, location_id, total_price) VALUES (%s, %s, %s)"
                    cursor.execute(order_query, (task_id, location_id, 0))
                    order_id = cursor.lastrowid

                # 4. 작업 유형에 따라 상세 주문 내역 처리 (order가 생성된 경우에만)
                if order_id is not None:
                    # order_details에서 items 추출
                    if isinstance(order_details, dict) and 'items' in order_details:
                        items = order_details['items']
                    else:
                        items = order_details  # 직접 리스트인 경우
                    
                    if task_type_name == settings.const.TASK_TYPE_FOOD_DELIVERY:
                        total_price = self._create_food_order_details(cursor, order_id, items)
                        # total_price 업데이트
                        cursor.execute("UPDATE `order` SET total_price = %s WHERE id = %s", (total_price, order_id))
                    elif task_type_name == settings.const.TASK_TYPE_SUPPLY_DELIVERY:
                        self._create_supply_order_details(cursor, order_id, items)
                        # 물품 배송은 가격이 없으므로 total_price는 0으로 유지
                
                log_database_operation("INSERT", "task, order", True, f"작업 생성 완료 | Task ID: {task_id}", "INFO")
                return {"task_id": task_id, "order_id": order_id}

    def _create_food_order_details(self, cursor, order_id, items):
        """음식 주문 상세 내역을 DB에 기록합니다."""
        total_price = 0
        for item in items:
            # OrderItem 객체인 경우와 딕셔너리인 경우 모두 처리
            if hasattr(item, 'name'):  # OrderItem 객체
                item_name = item.name
                item_quantity = item.quantity
            else:  # 딕셔너리
                item_name = item['name']
                item_quantity = item['quantity']
                
            cursor.execute("SELECT id, price FROM food WHERE name = %s", (item_name,))
            food_result = cursor.fetchone()
            if not food_result: continue
            food_id = food_result['id']
            total_price += food_result['price'] * item_quantity
            
            item_query = "INSERT INTO food_order_item (order_id, food_id, quantity) VALUES (%s, %s, %s)"
            cursor.execute(item_query, (order_id, food_id, item_quantity))
        
        return total_price

    def _create_supply_order_details(self, cursor, order_id, items):
        """물품 주문 상세 내역을 DB에 기록합니다."""
        for item in items:
            # OrderItem 객체인 경우와 딕셔너리인 경우 모두 처리
            if hasattr(item, 'name'):  # OrderItem 객체
                item_name = item.name
                item_quantity = item.quantity
            else:  # 딕셔너리
                item_name = item['name']
                item_quantity = item['quantity']
                
            cursor.execute("SELECT id FROM supply WHERE name = %s", (item_name,))
            supply_result = cursor.fetchone()
            if not supply_result: continue
            supply_id = supply_result['id']
            
            item_query = "INSERT INTO supply_order_item (order_id, supply_id, quantity) VALUES (%s, %s, %s)"
            cursor.execute(item_query, (order_id, supply_id, item_quantity))
            

    @handle_exceptions(default_return=None, reraise=False)
    def execute_task_assignment(self, robot_id):
        """(별도 스레드에서 실행) 준비된 작업을 찾아 로봇에 할당하고 액션을 호출합니다."""
        logger.info(
            "작업 할당 프로세스 시작",
            category="TASK", subcategory="ASSIGN",
            details={"RobotID": robot_id, "Status": "작업 가능"}
        )
        
        # goal_data를 try 블록 외부에서 선언하여 except 블록에서도 접근 가능하게 함
        goal_data = None
        task_id = None
        
        try:
            with safe_database_connection(db_manager.get_connection) as conn:
                with database_transaction(conn) as cursor:
                    # 1. 할당할 작업 찾기
                    query = """
                        SELECT t.id, t.type_id, t.location_id, tt.name as task_type_name
                        FROM task t
                        JOIN task_type tt ON t.type_id = tt.id
                        WHERE t.task_status_id = %s
                        ORDER BY t.task_creation_time ASC LIMIT 1 FOR UPDATE
                    """
                    cursor.execute(query, (settings.db_consts.task_status['준비 완료'],))
                    task_to_assign = cursor.fetchone()

                    if not task_to_assign:
                        logger.info(
                            "할당 가능한 작업 없음",
                            category="TASK", subcategory="ASSIGN",
                            details={"RobotID": robot_id}
                        )
                        return

                    task_id = task_to_assign['id']
                    logger.info(
                        f"가장 오래된 작업(Task {task_id})을 로봇 {robot_id}에 할당",
                        category="TASK", subcategory="ASSIGN",
                        details={"TaskID": task_id, "RobotID": robot_id}
                    )

                    # 2. 작업에 로봇 할당 및 상태 업데이트
                    update_query = "UPDATE task SET robot_id = %s, task_status_id = %s, robot_assignment_time = %s WHERE id = %s"
                    cursor.execute(update_query, (robot_id, settings.db_consts.task_status['로봇 할당됨'], datetime.now(), task_id))

                    # 3. 주문 정보 조회 (음식/비품 모두 처리하도록 수정)
                    order_info_json = self._get_order_info_json(cursor, task_id, task_to_assign['task_type_name'])

                    # 4. 픽업 위치 결정
                    task_type_name = task_to_assign['task_type_name']
                    pickup_location_name = None
                    if task_type_name == settings.const.TASK_TYPE_FOOD_DELIVERY:
                        pickup_location_name = settings.const.LOCATION_NAME_FOOD_PICKUP
                    elif task_type_name == settings.const.TASK_TYPE_SUPPLY_DELIVERY:
                        pickup_location_name = settings.const.LOCATION_NAME_SUPPLY_PICKUP
                    
                    if not pickup_location_name or pickup_location_name not in settings.db_consts.location:
                        raise ValueError(f"'{task_type_name}'에 대한 픽업 위치를 찾을 수 없거나 DB에 로드되지 않았습니다.")
                    
                    pickup_location_id = settings.db_consts.location[pickup_location_name]
                    
                    # 5. 액션 목표 데이터 생성
                    goal_data = {
                        'task_id': task_id,
                        'robot_id': robot_id,
                        'task_type_id': task_to_assign['type_id'], # 인터페이스 명세에 따라 추가
                        'task_status_id': settings.db_consts.task_status['로봇 할당됨'], # 인터페이스 명세에 따라 추가
                        'target_location_id': task_to_assign['location_id'], # 명확한 이름으로 변경
                        'pickup_location_id': pickup_location_id,
                        'order_info': order_info_json
                    }
                    log_database_operation("UPDATE", "task", True, f"작업 {task_id} 로봇 {robot_id}에 할당", "INFO")
            
            # 액션 목표 전송을 요청하고 즉시 다음 코드로 진행
            logger.info(
                "RC로 작업 수행 지시",
                category="ROS2", subcategory="ACTION-CALL",
                details={"Name": "/roomie/action/perform_task", "RobotID": robot_id, "TaskID": task_id}
            )
            self.action_handler.send_perform_task_goal(goal_data)

        except Exception as e:
            logger.error(
                f"작업 할당 중 심각한 오류 발생: {e}",
                category="TASK", subcategory="ASSIGN-ERROR",
                details={"RobotID": robot_id, "TaskID": task_id}
            )
            # 만약 오류가 발생하면, 할당된 task의 상태를 다시 '준비 완료'로 되돌리거나
            # '실패' 상태로 만드는 등의 롤백 로직을 여기에 추가
            # 예: self.rollback_task_assignment(task_id)

    def _get_order_info_json(self, cursor, task_id, task_type_name):
        """작업 ID와 유형에 따라 주문 상세 내역을 조회하여 JSON 문자열로 반환합니다."""
        items = []
        base_query = """
            SELECT o.id FROM `order` o WHERE o.task_id = %s
        """
        cursor.execute(base_query, (task_id,))
        order_result = cursor.fetchone()
        if not order_result:
            return json.dumps({"items": []})
        order_id = order_result['id']

        if task_type_name == settings.const.TASK_TYPE_FOOD_DELIVERY:
            item_query = """
                SELECT f.name, foi.quantity 
                FROM food_order_item foi
                JOIN food f ON foi.food_id = f.id
                WHERE foi.order_id = %s
            """
        elif task_type_name == settings.const.TASK_TYPE_SUPPLY_DELIVERY:
            item_query = """
                SELECT s.name, soi.quantity 
                FROM supply_order_item soi
                JOIN supply s ON soi.supply_id = s.id
                WHERE soi.order_id = %s
            """
        else:
            return json.dumps({"items": []})

        cursor.execute(item_query, (order_id,))
        order_items = cursor.fetchall()
        
        items = [{"name": item['name'], "quantity": item['quantity']} for item in order_items]
        return json.dumps({"items": items})