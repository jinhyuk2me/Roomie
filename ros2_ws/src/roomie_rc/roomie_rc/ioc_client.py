#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# ROS2 메시지 import
from roomie_msgs.srv import ControlLock, ReadCardInfo
from roomie_msgs.srv import CheckDoorState, CheckItemLoaded


class IOCClient:
    """
    IOC(IO Controller)와의 통신을 담당하는 클라이언트
    """
    
    def __init__(self, parent_node: Node):
        self.node = parent_node
        
        # IO Controller 클라이언트 초기화
        self._init_ioc_clients()
        
        self.node.get_logger().info('IOC Client 초기화 완료')
    
    def _init_ioc_clients(self):
        """IO Controller 클라이언트 초기화"""
        # 서랍 잠금 제어 Service Client (RC → IOC)
        self.control_lock_client = self.node.create_client(
            ControlLock,
            '/ioc/control_lock'
        )
        
        # 카드 정보 읽기 Service Client (RC → IOC)
        self.read_card_client = self.node.create_client(
            ReadCardInfo,
            '/ioc/read_card_info'
        )
        
        # 서랍문 상태 확인 Service Client (RC → IOC)
        self.check_door_client = self.node.create_client(
            CheckDoorState,
            '/ioc/check_door_state'
        )
        
        # 물품 적재 확인 Service Client (RC → IOC)
        self.check_item_client = self.node.create_client(
            CheckItemLoaded,
            '/ioc/check_item_loaded'
        )
        
        self.node.get_logger().info('IOC Service Clients 초기화 완료')
    
    def control_drawer_lock(self, locked: bool):
        """서랍 잠금 제어 (IOC)"""
        if not self.control_lock_client.wait_for_service(timeout_sec=2.0):
            self.node.get_logger().warn('IOC ControlLock 서비스를 찾을 수 없습니다')
            return True  # 시뮬레이션에서는 성공으로 처리
        
        request = ControlLock.Request()
        request.robot_id = self.node.robot_id
        request.locked = locked
        
        action = "잠금" if locked else "열림"
        self.node.get_logger().info(f'IOC 서랍 {action} 요청')
        
        try:
            # 비동기 호출만 (데드락 방지)
            future = self.control_lock_client.call_async(request)
            self.node.get_logger().info(f'IOC 서랍 {action} 요청 전송 완료')
            return True
                
        except Exception as e:
            self.node.get_logger().error(f'IOC 서랍 제어 요청 실패: {e}')
            return False
    
    def read_card_info(self):
        """카드 정보 읽기 요청"""
        if not self.read_card_client.service_is_ready():
            self.node.get_logger().warn('IOC ReadCardInfo 서비스를 찾을 수 없습니다')
            return False, 0
        
        request = ReadCardInfo.Request()
        request.robot_id = self.node.robot_id
        
        self.node.get_logger().info('IOC 카드 정보 읽기 요청')
        
        try:
            # 비동기 호출만 (데드락 방지)
            future = self.read_card_client.call_async(request)
            self.node.get_logger().info('IOC 카드 읽기 요청 전송 완료')
            return True, 101  # 시뮬레이션용 기본값 (success=True, location_id=101)
                
        except Exception as e:
            self.node.get_logger().error(f'IOC 카드 읽기 요청 중 오류: {e}')
            return False, 0
    
    def check_door_state(self):
        """서랍문 상태 확인 (IOC)"""
        if not self.check_door_client.service_is_ready():
            self.node.get_logger().warn('IOC CheckDoorState 서비스를 찾을 수 없습니다')
            return False  # 시뮬레이션에서는 닫힌 상태로 처리
        
        request = CheckDoorState.Request()
        request.robot_id = self.node.robot_id
        
        self.node.get_logger().info('IOC 서랍문 상태 확인')
        
        try:
            # 비동기 호출만 (데드락 방지)
            future = self.check_door_client.call_async(request)
            self.node.get_logger().info('IOC 서랍문 상태 확인 요청 전송 완료')
            
            # 시뮬레이션: 기본적으로 닫힘 상태로 가정
            self.node.get_logger().info('시뮬레이션: 서랍문 닫힘')
            return False
                
        except Exception as e:
            self.node.get_logger().error(f'IOC 서랍문 상태 확인 실패: {e}')
            return False
    
    def check_item_loaded(self):
        """물품 적재 확인 (IOC)"""
        if not self.check_item_client.service_is_ready():
            self.node.get_logger().warn('IOC CheckItemLoaded 서비스를 찾을 수 없습니다')
            return True  # 시뮬레이션에서는 물품 있음으로 처리
        
        request = CheckItemLoaded.Request()
        request.robot_id = self.node.robot_id
        
        self.node.get_logger().info('IOC 물품 적재 확인')
        
        try:
            # 비동기 호출만 (데드락 방지)
            future = self.check_item_client.call_async(request)
            self.node.get_logger().info('IOC 물품 적재 확인 요청 전송 완료')
            
            # 시뮬레이션: 기본적으로 물품 있음으로 가정
            self.node.get_logger().info('시뮬레이션: 물품 적재됨')
            return True
                
        except Exception as e:
            self.node.get_logger().error(f'IOC 물품 적재 확인 실패: {e}')
            return True
    
    # 편의 메서드들
    
    def unlock_drawer(self):
        """서랍 열기 (편의 메서드)"""
        return self.control_drawer_lock(False)
    
    def lock_drawer(self):
        """서랍 잠그기 (편의 메서드)"""
        return self.control_drawer_lock(True)
    
    def is_drawer_open(self):
        """서랍이 열려있는지 확인 (편의 메서드)"""
        return self.check_door_state()

    def has_item(self):
        """물품이 있는지 확인 (편의 메서드)"""
        return self.check_item_loaded() 