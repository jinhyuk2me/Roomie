#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# ROS2 메시지 import
from roomie_msgs.srv import Location


class VSClient:
    """
    VS(Vision Service)와의 통신을 담당하는 클라이언트
    """
    
    def __init__(self, parent_node: Node):
        self.node = parent_node
        
        # Vision Service 클라이언트 초기화
        self._init_vs_clients()
        
        self.node.get_logger().info('VS Client 초기화 완료')
    
    def _init_vs_clients(self):
        """Vision Service 클라이언트 초기화"""
        # 현재 위치 감지 Service Client (RC → VS)
        self.location_client = self.node.create_client(
            Location,
            '/vs/command/location'
        )
        self.node.get_logger().info('VS Location Service Client 초기화 완료')
    
    def get_current_location(self):
        """현재 위치 감지 요청"""
        if not self.location_client.service_is_ready():
            self.node.get_logger().warn('VS Location 서비스를 찾을 수 없습니다')
            return 0  # 기본값 반환
        
        request = Location.Request()
        request.robot_id = self.node.robot_id
        
        self.node.get_logger().info('VS에서 현재 위치 감지 요청')
        
        try:
            # 비동기 호출만 (데드락 방지)
            future = self.location_client.call_async(request)
            self.node.get_logger().info('VS 위치 감지 요청 전송 완료')
            return 0  # 시뮬레이션용 기본값
                
        except Exception as e:
            self.node.get_logger().error(f'VS 위치 감지 요청 중 오류: {e}')
            return 0
    
    def get_location_info(self):
        """현재 위치 상세 정보 조회"""
        location_id = self.get_current_location()
        
        # Location ID에 따른 위치 이름 매핑 (참고용)
        location_names = {
            0: "LOB_WAITING",
            1: "LOB_CALL", 
            2: "RES_PICKUP",
            3: "RES_CALL",
            4: "SUP_PICKUP",
            5: "ELE_1",
            6: "ELE_2",
            101: "ROOM_101",
            102: "ROOM_102",
            201: "ROOM_201",
            202: "ROOM_202"
        }
        
        location_name = location_names.get(location_id, f"UNKNOWN_{location_id}")
        self.node.get_logger().info(f'현재 위치: {location_name} (ID: {location_id})')
        
        return location_id, location_name 