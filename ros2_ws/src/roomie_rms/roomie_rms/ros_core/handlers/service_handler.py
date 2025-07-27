from app.utils.logger import get_logger, log_ros_event, log_database_operation
from app.utils.error_handler import handle_database_errors, database_transaction, safe_database_connection
from app.utils.exceptions import DatabaseException
from app.services import db_manager

logger = get_logger(__name__)

class ServiceHandler:
    """ROS2 Service 콜백 함수들을 관리하는 클래스"""
    def __init__(self, robot_manager, task_manager):
        self.robot_manager = robot_manager
        self.task_manager = task_manager
    
    @handle_database_errors
    def get_locations_callback(self, request, response):
        """RC로부터 위치 정보 요청을 받아 DB에 저장된 모든 위치 정보를 반환합니다."""
        logger.info(
            "위치 정보 요청",
            category="ROS2", subcategory="SERVICE-REQ",
            details={"RobotID": request.robot_id, "Service": "/roomie/command/get_locations"}
        )
        
        try:
            with safe_database_connection(db_manager.get_connection) as conn:
                with conn.cursor(dictionary=True) as cursor:
                    cursor.execute("SELECT id, floor_id, location_x, location_y FROM location WHERE location_x IS NOT NULL AND location_y IS NOT NULL")
                    locations = cursor.fetchall()
                    
                    response.robot_id = request.robot_id
                    response.success = True
                    response.location_ids = [loc['id'] for loc in locations]
                    response.floor_ids = [loc['floor_id'] for loc in locations]
                    response.location_xs = [loc['location_x'] for loc in locations]
                    response.location_ys = [loc['location_y'] for loc in locations]
                    
                    log_database_operation("SELECT", "location", True, f"{len(locations)}개 위치 정보 조회")
                    logger.info(
                        f"위치 정보 {len(locations)}개를 전송 완료",
                        category="ROS2", subcategory="SERVICE-RES",
                        details={"RobotID": request.robot_id, "Count": len(locations)}
                    )
                    
        except (DatabaseException, Exception) as e:
            logger.error(
                f"위치 정보 조회 실패: {e}",
                category="ROS2", subcategory="SERVICE-ERROR",
                details={"RobotID": request.robot_id}
            )
            response.success = False
                
        return response 