import rclpy
from rclpy.node import Node
import uvicorn
from app.main import app
from app.utils.logger import logger
import threading

class RmsNode(Node):
    def __init__(self):
        super().__init__('rms_node')
        self.get_logger().info('RMS ROS2 Node has been started.')
        logger.info('RMS ROS2 노드가 초기화되었습니다.')
        # TODO: ROS2 Publisher, Subscriber, Service 등 초기화

def run_fastapi():
    """FastAPI 서버를 실행하는 함수"""
    logger.info('FastAPI 서버를 시작합니다. (호스트: 0.0.0.0, 포트: 8000)')
    uvicorn.run(app, host="0.0.0.0", port=8000)

def main(args=None):
    logger.info('Roomie RMS 시스템을 시작합니다.')
    
    # 1. FastAPI 서버를 별도 스레드에서 실행
    logger.info('FastAPI 서버 스레드를 생성합니다.')
    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.daemon = True
    fastapi_thread.start()

    # 2. ROS2 노드 실행
    logger.info('ROS2 노드를 초기화합니다.')
    rclpy.init(args=args)
    rms_node = RmsNode()
    
    try:
        logger.info('ROS2 노드 스핀을 시작합니다.')
        rclpy.spin(rms_node)
    except KeyboardInterrupt:
        logger.warning('사용자에 의해 시스템이 중단됩니다.')
    finally:
        logger.info('RMS 시스템을 종료합니다.')
        rms_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()