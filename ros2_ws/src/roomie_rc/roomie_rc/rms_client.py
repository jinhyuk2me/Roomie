#!/usr/bin/env python3

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from rclpy.qos import QoSProfile
from builtin_interfaces.msg import Time

# ROS2 메시지 import
from roomie_msgs.action import PerformTask, PerformReturn
from roomie_msgs.msg import RobotState, BatteryStatus, RoomiePose, Arrival
from roomie_msgs.msg import PickupCompleted, DeliveryCompleted, TaskState
from roomie_msgs.srv import CreateTask
from geometry_msgs.msg import Pose, Point, Quaternion


class RMSClient:
    """
    RMS(Roomie Main Service)와의 통신을 담당하는 클라이언트
    """
    
    def __init__(self, parent_node: Node):
        self.node = parent_node
        
        # QoS 프로파일 설정
        self.qos_profile = QoSProfile(depth=10)
        
        # Action Server, Publishers, Subscribers 초기화
        self._init_action_servers()
        self._init_publishers()
        self._init_subscribers()
        self._init_service_clients()
        
        self.node.get_logger().info('RMS Client 초기화 완료')
    
    def _init_action_servers(self):
        """Action Server 초기화"""
        self.perform_task_server = ActionServer(
            self.node,
            PerformTask,
            '/roomie/action/perform_task',
            self._perform_task_callback
        )
        self.node.get_logger().info('PerformTask Action Server 초기화 완료')
        
        self.perform_return_server = ActionServer(
            self.node,
            PerformReturn,
            '/roomie/action/perform_return',
            self._perform_return_callback
        )
        self.node.get_logger().info('PerformReturn Action Server 초기화 완료')
    
    def _init_publishers(self):
        """Publisher 초기화"""
        # 로봇 상태 Publisher
        self.robot_state_pub = self.node.create_publisher(
            RobotState,
            '/roomie/status/robot_state',
            self.qos_profile
        )
        
        # 배터리 상태 Publisher  
        self.battery_status_pub = self.node.create_publisher(
            BatteryStatus,
            '/roomie/status/battery_status',
            self.qos_profile
        )
        
        # 로봇 위치 Publisher
        self.roomie_pose_pub = self.node.create_publisher(
            RoomiePose,
            '/roomie/status/roomie_pose',
            self.qos_profile
        )
        
        # 이벤트 Publishers
        self.arrival_pub = self.node.create_publisher(
            Arrival,
            '/roomie/event/arrival',
            self.qos_profile
        )
        
        self.pickup_completed_pub = self.node.create_publisher(
            PickupCompleted,
            '/roomie/event/pickup_completed',
            self.qos_profile
        )
        
        self.delivery_completed_pub = self.node.create_publisher(
            DeliveryCompleted,
            '/roomie/event/delivery_completed',
            self.qos_profile
        )
        
        self.node.get_logger().info('RMS Publishers 초기화 완료')
    
    def _init_subscribers(self):
        """Subscriber 초기화"""
        self.task_state_sub = self.node.create_subscription(
            TaskState,
            '/roomie/status/task_state',
            self._task_state_callback,
            self.qos_profile
        )
        self.node.get_logger().info('TaskState Subscriber 초기화 완료')
    
    def _init_service_clients(self):
        """Service Client 초기화"""
        self.create_task_client = self.node.create_client(
            CreateTask,
            '/roomie/command/create_task'
        )
        self.node.get_logger().info('CreateTask Service Client 초기화 완료')
    
    def _perform_task_callback(self, goal_handle):
        """PerformTask Action 콜백"""
        self.node.get_logger().info(f'작업 할당 받음: task_id={goal_handle.request.task_id}')
        self.node.get_logger().info(f'작업 타입: {goal_handle.request.task_type_id}')
        self.node.get_logger().info(f'픽업 장소: {goal_handle.request.pickup_location_id}')
        self.node.get_logger().info(f'목적지: {goal_handle.request.target_location_id}')
        
        # 작업 할당 처리
        if hasattr(self.node, 'handle_task_assignment'):
            self.node.handle_task_assignment(goal_handle.request, None)  # goal_handle 제거
        
        # 즉시 성공 결과 반환
        result = PerformTask.Result()
        result.robot_id = goal_handle.request.robot_id
        result.task_id = goal_handle.request.task_id
        result.success = True
        result.message = "작업 할당 완료"
        
        goal_handle.succeed()
        return result

    def _perform_return_callback(self, goal_handle):
        """PerformReturn Action 콜백"""
        self.node.get_logger().info('=== 복귀 액션 수신 ===')
        self.node.get_logger().info(f'로봇 ID: {goal_handle.request.robot_id}')
        
        # Goal이 이미 executing 상태이므로 별도 execute() 호출 불필요
        
        # 메인 노드에 복귀 작업 알림
        if hasattr(self.node, 'handle_return_task'):
            self.node.handle_return_task()
        
        # 결과 반환 (즉시 완료되는 복귀 작업)
        result = PerformReturn.Result()
        result.robot_id = goal_handle.request.robot_id
        result.message = "복귀 작업 완료"
        
        goal_handle.succeed()
        return result
    
    def _task_state_callback(self, msg):
        """TaskState 콜백"""
        self.node.get_logger().info(f'작업 상태 수신: task_id={msg.task_id}, state={msg.task_state_id}')
        
        # 메인 노드에 작업 상태 변경 알림
        if hasattr(self.node, 'handle_task_state_change'):
            self.node.handle_task_state_change(msg)
    
    def publish_robot_state(self, robot_state_id):
        """로봇 상태 발행 (task_id 제거됨)"""
        msg = RobotState()
        msg.robot_id = self.node.robot_id
        msg.robot_state_id = robot_state_id
        
        self.robot_state_pub.publish(msg)
        self.node.get_logger().info(f'RMS에게 로봇 상태 발행: {robot_state_id}')
    
    def publish_battery_status(self, charge_percentage=85.0, is_charging=False):
        """배터리 상태 발행"""
        msg = BatteryStatus()
        msg.robot_id = self.node.robot_id
        msg.charge_percentage = charge_percentage
        msg.is_charging = is_charging
        
        self.battery_status_pub.publish(msg)
    #    self.node.get_logger().info(f'배터리 상태 발행: {charge_percentage}%')
    
    def publish_roomie_pose(self, floor_id=0, x=0.0, y=0.0, z=0.0):
        """로봇 위치 발행 (floor → floor_id로 변경)"""
        msg = RoomiePose()
        msg.robot_id = self.node.robot_id
        msg.floor_id = floor_id
        
        # Pose 설정
        msg.pose = Pose()
        msg.pose.position = Point(x=x, y=y, z=z)
        msg.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)
        
        self.roomie_pose_pub.publish(msg)
    #    self.node.get_logger().info(f'위치 발행: floor_id={floor_id}, x={x}, y={y}')
    
    def publish_arrival_event(self, location_id, task_id=0):
        """도착 이벤트 발행"""
        msg = Arrival()
        msg.robot_id = self.node.robot_id
        msg.task_id = task_id
        msg.location_id = location_id
        
        self.arrival_pub.publish(msg)
        self.node.get_logger().info(f'RMS에게 도착 이벤트 발행: location {location_id}')
    
    def publish_pickup_completed(self, task_id=0):
        """픽업 완료 이벤트 발행"""
        msg = PickupCompleted()
        msg.robot_id = self.node.robot_id
        msg.task_id = task_id
        msg.timestamp = self.node.get_clock().now().to_msg()
        
        self.pickup_completed_pub.publish(msg)
        self.node.get_logger().info('RMS에게 픽업 완료 이벤트 발행')
    
    def publish_delivery_completed(self, task_id=0):
        """수령 완료 이벤트 발행"""
        msg = DeliveryCompleted()
        msg.robot_id = self.node.robot_id
        msg.task_id = task_id
        msg.timestamp = self.node.get_clock().now().to_msg()
        
        self.delivery_completed_pub.publish(msg)
        self.node.get_logger().info('RMS에게 수령 완료 이벤트 발행') 