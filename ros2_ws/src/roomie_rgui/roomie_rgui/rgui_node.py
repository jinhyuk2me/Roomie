import sys
import rclpy
from rclpy.node import Node
from PyQt6.QtWidgets import QApplication
from roomie_msgs.msg import RobotGuiEvent
from roomie_msgs.srv import UnlockDoor, StartCountdown, ReturnCountdown

from .screen_manager import ScreenManager
from .service_client import call_service

class RobotGuiNode(Node):
    def __init__(self, app):
        super().__init__('robot_gui_node')
        self.app = app
        self.screen = ScreenManager(self)

        # Publisher
        self.event_pub = self.create_publisher(RobotGuiEvent, '/robot_gui/event', 10)

        # Service Clients
        self.unlock_door_cli = self.create_client(UnlockDoor, '/robot_gui/unlock_door')
        self.departure_cli = self.create_client(StartCountdown, '/robot_gui/start_departure_countdown')
        self.return_cli = self.create_client(ReturnCountdown, '/robot_gui/start_return_countdown')

    def publish_event(self, event_id: int, robot_id: int, task_id: int = 0, detail: str = ""):
        from builtin_interfaces.msg import Time
        from rclpy.clock import Clock

        msg = RobotGuiEvent()
        msg.robot_id = robot_id
        msg.task_id = task_id
        msg.rgui_event_id = event_id
        msg.detail = detail
        msg.timestamp = Clock().now().to_msg()
        self.event_pub.publish(msg)

    def request_unlock_door(self, robot_id: int, task_id: int):
        req = UnlockDoor.Request()
        req.robot_id = robot_id
        req.task_id = task_id
        call_service(self, self.unlock_door_cli, req)

    def request_departure_countdown(self, robot_id: int, task_id: int):
        req = StartCountdown.Request()
        req.robot_id = robot_id
        req.task_id = task_id
        call_service(self, self.departure_cli, req)

    def request_return_countdown(self, robot_id: int):
        req = ReturnCountdown.Request()
        req.robot_id = robot_id
        call_service(self, self.return_cli, req)


def main():
    rclpy.init()
    app = QApplication(sys.argv)
    node = RobotGuiNode(app)
    sys.exit(app.exec())
