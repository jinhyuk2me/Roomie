"""
Roomie RMS 통합 노드

ROS2 노드와 FastAPI 서버를 통합하여 운영하는 메인 모듈입니다.
"""

import asyncio
import threading
import uvicorn
import rclpy
from rclpy.executors import MultiThreadedExecutor
from fastapi import FastAPI

from app.utils.logger import get_logger, log_node_startup, log_node_shutdown
from app.services import http_manager, websocket_manager, db_manager
from ros_core.base_node import RmsBaseNode
from ros_core.business.robot_manager import RobotManager
from ros_core.business.task_manager import TaskManager
from ros_core.handlers.action_handler import ActionHandler
from ros_core.handlers.service_handler import ServiceHandler
from ros_core.handlers.topic_handler import TopicHandler

logger = get_logger(__name__)

class RmsNode(RmsBaseNode, ServiceHandler, TopicHandler, ActionHandler):
    """
    Roomie RMS 통합 노드
    
    ROS2 노드와 FastAPI 서버를 통합하여 운영하는 메인 클래스입니다.
    로봇 관리, 작업 관리, GUI 통신을 담당합니다.
    """
    
    def __init__(self) -> None:
        """RMS 노드 초기화"""
        super().__init__('rms_node')
        
        # ROS2 노드의 로거를 RMS 로거로 교체하여 일관성 유지
        self.get_logger().info = logger.info
        self.get_logger().error = logger.error
        self.get_logger().warning = logger.warning
        self.get_logger().debug = logger.debug
        
        # 비즈니스 로직 매니저 초기화
        self.robot_manager: RobotManager = RobotManager(self)
        self.task_manager: TaskManager = TaskManager(self.robot_manager, self)  # self는 ActionHandler를 상속받은 RmsNode
        
        # 핸들러 초기화 (의존성 주입)
        ServiceHandler.__init__(self, robot_manager=self.robot_manager, task_manager=self.task_manager)
        TopicHandler.__init__(self, robot_manager=self.robot_manager, task_manager=self.task_manager, node=self)
        ActionHandler.__init__(self, robot_manager=self.robot_manager, task_manager=self.task_manager, db_manager=db_manager, node=self)
        
        # 이벤트 루프 설정 (DeprecationWarning 해결)
        try:
            self.loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
        except RuntimeError:
            self.loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)
        
        logger.info("RMS 통합 노드 초기화 완료", category="SYSTEM", subcategory="INIT")

    def get_loop(self) -> asyncio.AbstractEventLoop:
        """현재 이벤트 루프를 반환합니다."""
        return self.loop
    
    # --- TopicHandler 콜백 메서드 오버라이드 ---
    def robot_state_callback(self, msg):
        """로봇 상태 콜백"""
        TopicHandler.robot_state_callback(self, msg)
    
    def task_state_callback(self, msg):
        """작업 상태 콜백"""
        TopicHandler.task_state_callback(self, msg)
    
    def arrival_callback(self, msg):
        """도착 이벤트 콜백"""
        TopicHandler.arrival_callback(self, msg)
    
    def battery_status_callback(self, msg):
        """배터리 상태 콜백"""
        TopicHandler.battery_status_callback(self, msg)
    
    def roomie_pose_callback(self, msg):
        """로봇 포즈 콜백"""
        TopicHandler.roomie_pose_callback(self, msg)
    
    def pickup_completed_callback(self, msg):
        """픽업 완료 콜백"""
        TopicHandler.pickup_completed_callback(self, msg)
    
    def delivery_completed_callback(self, msg):
        """배송 완료 콜백"""
        TopicHandler.delivery_completed_callback(self, msg)
    
    # --- ServiceHandler 콜백 메서드 오버라이드 ---
    def get_locations_callback(self, request, response):
        """위치 조회 서비스 콜백"""
        return ServiceHandler.get_locations_callback(self, request, response)

def create_app(rms_node: RmsNode) -> FastAPI:
    """FastAPI 앱 생성 및 설정"""
    app = FastAPI(title="Roomie RMS API Server")
    
    # RMS 노드 인스턴스를 앱 상태에 설정
    app.state.rms_node = rms_node
    
    # API 라우터 등록
    app.include_router(http_manager.manager.router, prefix="/api/gui")
    app.include_router(websocket_manager.manager.router, prefix="/api/gui")
    
    @app.get("/")
    async def root():
        return {"message": "Roomie RMS API Server is running"}

    @app.get("/health")
    async def health():
        return {"status": "healthy", "rms_node": "connected"}
    
    return app

def main():
    """메인 실행 함수"""
    # 노드 시작 로그
    log_node_startup()
    
    from app.config import settings
    
    rclpy.init()
    
    try:
        # RMS 노드 인스턴스 생성
        rms_node = RmsNode()
        
        # FastAPI 앱 생성
        app = create_app(rms_node)
        
        # FastAPI 서버를 별도 스레드에서 실행
        fastapi_thread = threading.Thread(
            target=lambda: uvicorn.run(
                app, 
                host=settings.FASTAPI_HOST, 
                port=settings.FASTAPI_PORT,
                log_level="info"
            )
        )
        fastapi_thread.daemon = True
        logger.info(
            f"FastAPI 서버 시작",
            category="SYSTEM", subcategory="START",
            details={"Host": settings.FASTAPI_HOST, "Port": settings.FASTAPI_PORT}
        )
        fastapi_thread.start()
        
        # ROS2 노드를 메인 스레드에서 실행
        logger.info("RMS 노드 실행 시작", category="SYSTEM", subcategory="RUN")
        executor: MultiThreadedExecutor = MultiThreadedExecutor()
        executor.add_node(rms_node)
        
        try:
            executor.spin()
        finally:
            logger.info("RMS 노드 종료 중...", category="SYSTEM", subcategory="SHUTDOWN")
            executor.shutdown()
            rms_node.destroy_node()

    except KeyboardInterrupt:
        logger.warning("사용자에 의해 RMS 노드가 중단되었습니다.", category="SYSTEM", subcategory="INTERRUPT")
    except Exception as e:
        logger.critical(f"RMS 노드 실행 중 치명적 오류 발생: {e}", category="SYSTEM", subcategory="CRITICAL")
        raise
    finally:
        # 노드 종료 로그
        log_node_shutdown()
        logger.info("RMS 노드 종료", category="SYSTEM", subcategory="END")
        rclpy.shutdown()

if __name__ == '__main__':
    main()