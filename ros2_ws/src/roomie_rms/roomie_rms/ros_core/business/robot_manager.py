from datetime import datetime
from app.utils.logger import get_logger, log_database_operation
from app.utils.error_handler import handle_database_errors

logger = get_logger(__name__)

class RobotManager:
    """로봇 상태 조회, 업데이트 등 비즈니스 로직을 관리하는 클래스"""
    
    def __init__(self, node):
        self.node = node

    def get_available_robot(self):
        """사용 가능한 로봇을 찾아 반환합니다."""
        # TODO: 실제 로봇 선택 로직 구현
        # 현재는 항상 1번 로봇을 반환하도록 시뮬레이션
        return 1

    @handle_database_errors
    def update_robot_current_state(self, cursor, robot_id, status_id=None, location_id=None, battery_level=None, error_id=None):
        """(Helper) robot_current_state 테이블을 동시성 문제 없이 안전하게 업데이트합니다."""
        
        # 1. SELECT ... FOR UPDATE로 해당 로봇의 현재 상태 레코드를 잠그고 가져옵니다.
        cursor.execute(
            "SELECT robot_id FROM robot_current_state WHERE robot_id = %s FOR UPDATE",
            (robot_id,)
        )
        current_state_record = cursor.fetchone()

        current_time = datetime.now()
        
        if current_state_record:
            # 2a. 레코드가 있으면 UPDATE
            update_fields = ["last_updated_time = %s"]
            values = [current_time]
            
            if status_id is not None:
                update_fields.append("robot_status_id = %s")
                values.append(status_id)
            if location_id is not None:
                update_fields.append("location_id = %s")
                values.append(location_id)
            if battery_level is not None:
                update_fields.append("battery_level = %s")
                values.append(battery_level)
            if error_id is not None:
                update_fields.append("error_id = %s")
                values.append(error_id)
            
            values.append(robot_id)
            
            query = f"UPDATE robot_current_state SET {', '.join(update_fields)} WHERE robot_id = %s"
            cursor.execute(query, tuple(values))

        else:
            # 2b. 레코드가 없으면 INSERT
            query = """
                INSERT INTO robot_current_state 
                (robot_id, robot_status_id, location_id, battery_level, error_id, last_updated_time)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (robot_id, status_id, location_id, battery_level, error_id, current_time))
        
        log_database_operation("UPDATE", "robot_current_state", True, f"Robot ID {robot_id} 상태 업데이트") 