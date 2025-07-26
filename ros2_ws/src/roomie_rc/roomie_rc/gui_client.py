#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile

# ROS2 메시지 import
from roomie_msgs.msg import RobotGuiEvent
from roomie_msgs.srv import StartCountdown, ReturnCountdown
from std_srvs.srv import Trigger  # UnlockDoor는 std_srvs/Trigger 사용


class GUIClient:
    """
    RGUI(Robot GUI)와의 통신을 담당하는 클라이언트
    """
    
    def __init__(self, parent_node: Node):
        self.node = parent_node
        
        # QoS 프로파일 설정
        self.qos_profile = QoSProfile(depth=10)
        
        # Publishers, Subscribers, Service Clients/Servers 초기화
        self._init_publishers()
        self._init_subscribers()
        self._init_service_clients()
        self._init_service_servers()
        
        self.node.get_logger().info('GUI Client 초기화 완료')
    
    def _init_publishers(self):
        """Publisher 초기화"""
        # GUI 이벤트 Publisher (RC → RGUI)
        self.gui_event_pub = self.node.create_publisher(
            RobotGuiEvent,
            '/robot_gui/event',
            self.qos_profile
        )
        self.node.get_logger().info('GUI Event Publisher 초기화 완료')
    
    def _init_subscribers(self):
        """Subscriber 초기화"""
        # GUI 이벤트 Subscriber (RGUI → RC)
        self.gui_event_sub = self.node.create_subscription(
            RobotGuiEvent,
            '/robot_gui/event',
            self._gui_event_callback,
            self.qos_profile
        )
        self.node.get_logger().info('GUI Event Subscriber 초기화 완료')
    
    def _init_service_clients(self):
        """Service Client 초기화"""
        # 출발 카운트다운 Service Client (RC → RGUI)
        self.start_countdown_client = self.node.create_client(
            StartCountdown,
            '/robot_gui/start_countdown'
        )
        
        # 복귀 카운트다운 Service Client (RC → RGUI)
        self.return_countdown_client = self.node.create_client(
            ReturnCountdown,
            '/robot_gui/start_return_countdown'
        )
        
        self.node.get_logger().info('GUI Service Clients 초기화 완료')
    
    def _init_service_servers(self):
        """Service Server 초기화"""
        # 도어 잠금 해제 Service Server (RGUI → RC)
        self.unlock_door_server = self.node.create_service(
            Trigger,
            '/robot_gui/unlock_door',
            self._unlock_door_callback
        )
        self.node.get_logger().info('UnlockDoor Service Server 초기화 완료')
    
    def _gui_event_callback(self, msg):
        """GUI 이벤트 콜백 (RGUI → RC)"""
        self.node.get_logger().info(f'GUI 이벤트 수신: robot_id={msg.robot_id}, event_id={msg.rgui_event_id}')
        self.node.get_logger().info(f'이벤트 내용: {msg.detail}')
        
        # 메인 노드에 GUI 이벤트 알림
        if hasattr(self.node, 'handle_gui_event'):
            self.node.handle_gui_event(msg)
    
    def _unlock_door_callback(self, request, response):
        """도어 잠금 해제 서비스 콜백 (RGUI → RC)"""
        self.node.get_logger().info('GUI에서 도어 잠금 해제 요청 수신')
        
        # 메인 노드에 도어 잠금 해제 요청 전달
        if hasattr(self.node, 'handle_unlock_door_request'):
            success = self.node.handle_unlock_door_request()
            response.success = success
            response.message = "도어 잠금 해제 완료" if success else "도어 잠금 해제 실패"
        else:
            response.success = True
            response.message = "도어 잠금 해제 요청 처리됨"
        
        self.node.get_logger().info(f'도어 잠금 해제 응답: {response.success}')
        return response
    
    def send_gui_event(self, event_id, detail="", task_id=0):
        """GUI 이벤트 전송 (RC → RGUI)"""
        msg = RobotGuiEvent()
        msg.robot_id = self.node.robot_id
        msg.rgui_event_id = event_id
        msg.task_id = task_id
        msg.timestamp = self.node.get_clock().now().to_msg()
        msg.detail = detail
        
        self.gui_event_pub.publish(msg)
        self.node.get_logger().info(f'GUI에게 이벤트 전송: event_id={event_id}, detail="{detail}"')
    
    def start_countdown(self, robot_id, task_id, task_type_id):
        """출발 카운트다운 시작 (RC → RGUI)"""
        if not self.start_countdown_client.wait_for_service(timeout_sec=2.0):
            self.node.get_logger().warn('StartCountdown 서비스를 찾을 수 없습니다')
            return False
        
        request = StartCountdown.Request()
        request.robot_id = robot_id
        request.task_id = task_id
        request.task_type_id = task_type_id
        
        self.node.get_logger().info(f'GUI 카운트다운 시작 요청: robot_id={robot_id}, task_id={task_id}, task_type_id={task_type_id}')
        
        try:
            future = self.start_countdown_client.call_async(request)
            
            # 비동기 호출만 (데드락 방지)
            self.node.get_logger().info('GUI 카운트다운 요청 전송 완료')
            return True
                
        except Exception as e:
            self.node.get_logger().error(f'GUI 카운트다운 요청 실패: {e}')
            return False
    
    def start_return_countdown(self):
        """복귀 카운트다운 시작 (RC → RGUI)"""
        if not self.return_countdown_client.wait_for_service(timeout_sec=2.0):
            self.node.get_logger().warn('ReturnCountdown 서비스를 찾을 수 없습니다')
            return False
        
        request = ReturnCountdown.Request()
        request.robot_id = self.node.robot_id
        
        self.node.get_logger().info('GUI 복귀 카운트다운 시작 요청')
        
        try:
            future = self.return_countdown_client.call_async(request)
            # TODO: 나중에 async 처리 개선
            self.node.get_logger().info('GUI 복귀 카운트다운 요청 전송 완료')
            return True
        except Exception as e:
            self.node.get_logger().error(f'GUI 복귀 카운트다운 요청 실패: {e}')
            return False 