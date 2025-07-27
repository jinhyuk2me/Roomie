import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from app.utils.logger import get_logger, log_ros_event
from app.config import settings
from app.services import db_manager

from roomie_msgs.msg import (
    RobotState, TaskState, Arrival, BatteryStatus, RoomiePose, 
    PickupCompleted, DeliveryCompleted
)
from roomie_msgs.srv import GetLocations, CreateTask
from roomie_msgs.action import PerformTask, PerformReturn

logger = get_logger(__name__)

class RmsBaseNode(Node):
    """
    Roomie RMS의 기본 ROS2 노드 클래스.
    
    이 클래스는 ROS2 인터페이스 설정과 외부 서비스 매니저 초기화를 담당합니다.
    실제 콜백 구현은 상속받는 핸들러 클래스들에서 수행됩니다.
    
    Attributes:
        websocket_manager: WebSocket 연결 관리 매니저
        task_state_pub: 작업 상태 퍼블리셔
        robot_state_sub: 로봇 상태 서브스크라이버
        arrival_sub: 도착 이벤트 서브스크라이버
        battery_status_sub: 배터리 상태 서브스크라이버
        roomie_pose_sub: 로봇 위치 서브스크라이버
        pickup_completed_sub: 픽업 완료 서브스크라이버
        delivery_completed_sub: 배송 완료 서브스크라이버
        get_locations_service: 위치 조회 서비스 서버
        create_task_service: 작업 생성 서비스 서버
        perform_task_client: 작업 수행 액션 클라이언트
        perform_return_client: 복귀 액션 클라이언트
    """
    
    def __init__(self, node_name: str = 'rms_node') -> None:
        """
        RMS 기본 노드 초기화.
        
        Args:
            node_name: ROS2 노드 이름
        """
        super().__init__(node_name)
        logger.info(f"'{node_name}' 노드 초기화 시작...")

        self._initialize_managers()
        self._setup_ros_interfaces()

        logger.info("ROS2 인터페이스 및 매니저 초기화 완료")
    
    def _initialize_managers(self) -> None:
        """
        외부 서비스 매니저(DB) 초기화.
        
        Raises:
            Exception: DB 초기화 실패 시 발생
        """
        try:
            db_manager.init_db_pool()
        except Exception as e:
            logger.error(f"DB 초기화 실패. 노드를 시작할 수 없습니다: {e}")
            raise e
        logger.info("DB 매니저 초기화 완료")
    
    def _setup_ros_interfaces(self) -> None:
        """
        ROS2 Publisher, Subscriber, Service, Action 클라이언트 설정.
        
        이 메서드는 모든 ROS2 인터페이스를 초기화하며,
        실제 콜백 함수는 상속받는 핸들러 클래스에서 구현됩니다.
        """
        
        # --- Publishers (RMS -> RC) ---
        self.task_state_pub = self.create_publisher(TaskState, settings.ros.TASK_STATE_TOPIC, 10)

        # --- Subscribers (RC -> RMS) ---
        # 실제 콜백 함수는 TopicHandler에서 구현됩니다.
        self.create_subscription(RobotState, settings.ros.ROBOT_STATE_TOPIC, self.robot_state_callback, 10)
        self.create_subscription(TaskState, settings.ros.TASK_STATE_TOPIC, self.task_state_callback, 10)
        self.create_subscription(Arrival, settings.ros.ARRIVAL_TOPIC, self.arrival_callback, 10)
        self.create_subscription(BatteryStatus, settings.ros.BATTERY_STATUS_TOPIC, self.battery_status_callback, 10)
        self.create_subscription(RoomiePose, settings.ros.ROOMIE_POSE_TOPIC, self.roomie_pose_callback, 10)
        self.create_subscription(PickupCompleted, settings.ros.PICKUP_COMPLETED_TOPIC, self.pickup_completed_callback, 10)
        self.create_subscription(DeliveryCompleted, settings.ros.DELIVERY_COMPLETED_TOPIC, self.delivery_completed_callback, 10)
        
        # --- Service Servers ---
        # 실제 콜백 함수는 ServiceHandler에서 구현됩니다.
        self.get_locations_srv = self.create_service(
            GetLocations,
            settings.ros.GET_LOCATIONS_SERVICE,
            self.get_locations_callback
        )

        # --- Service Clients ---
        self.create_task_cli = self.create_client(CreateTask, settings.ros.CREATE_TASK_SERVICE)

        # --- Action Clients ---
        self._perform_task_ac = ActionClient(self, PerformTask, settings.ros.PERFORM_TASK_ACTION)
        self._perform_return_ac = ActionClient(self, PerformReturn, settings.ros.PERFORM_RETURN_ACTION)
        
        log_ros_event("SETUP", self.get_name(), "ROS2 인터페이스 설정 완료")

    # --- Placeholder 콜백 메서드 ---
    # 이 메서드들은 실제 로직을 담고 있지 않으며,
    # 상속받는 핸들러 클래스에서 오버라이드(override)됩니다.
    def robot_state_callback(self, msg):
        raise NotImplementedError("robot_state_callback must be implemented in a handler class")

    def task_state_callback(self, msg):
        raise NotImplementedError("task_state_callback must be implemented in a handler class")
    
    def arrival_callback(self, msg):
        raise NotImplementedError("arrival_callback must be implemented in a handler class")

    def battery_status_callback(self, msg):
        raise NotImplementedError("battery_status_callback must be implemented in a handler class")

    def roomie_pose_callback(self, msg):
        raise NotImplementedError("roomie_pose_callback must be implemented in a handler class")

    def pickup_completed_callback(self, msg):
        raise NotImplementedError("pickup_completed_callback must be implemented in a handler class")

    def delivery_completed_callback(self, msg):
        raise NotImplementedError("delivery_completed_callback must be implemented in a handler class")
        
    def get_locations_callback(self, request, response):
        raise NotImplementedError("get_locations_callback must be implemented in a handler class") 