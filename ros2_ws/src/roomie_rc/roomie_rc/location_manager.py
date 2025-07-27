#!/usr/bin/env python3

"""
위치 관리 모듈
현재는 하드코딩된 데이터, 나중에 RMS 서버에서 받아올 예정
"""

class LocationManager:
    """
    위치 정보를 관리하는 클래스
    """
    
    def __init__(self):
        # 하드코딩된 위치 데이터베이스
        self.location_database = {
            0: {
                "name": "LOB_WAITING",
                "x": -0.2,
                "y": 0.5,
                "floor_id": 0  # 1층
            },
            2: {
                "name": "RES_PICKUP", 
                "x": -0.3,
                "y": 2.5,
                "floor_id": 0  # 1층
            },
            4: {
                "name": "SUP_PICKUP",
                "x": -0.3, 
                "y": 4.5,
                "floor_id": 0  # 1층
            },
            5: {
                "name": "ELE_1",
                "x": 9.25,
                "y": 1.7,
                "floor_id": 0  # 1층 (엘리베이터)
            },
            101: {
                "name": "ROOM_101",
                "x": 5.3,
                "y": 3.5,
                "floor_id": 0  # 1층
            },
            102: {
                "name": "ROOM_102", 
                "x": 7.4,
                "y": 3.5,
                "floor_id": 0  # 1층
            }
            # TODO: 나중에 더 많은 위치 추가 (201, 202 등)
        }
    
    def get_location_info(self, location_id):
        """
        location_id로 위치 정보 조회
        
        Args:
            location_id (int): 위치 ID
            
        Returns:
            dict: 위치 정보 (name, x, y, floor_id) 또는 None
        """
        return self.location_database.get(location_id)
    
    def get_coordinates(self, location_id):
        """
        location_id로 좌표 조회
        
        Args:
            location_id (int): 위치 ID
            
        Returns:
            tuple: (x, y, floor_id) 또는 None
        """
        location = self.get_location_info(location_id)
        if location:
            return (location["x"], location["y"], location["floor_id"])
        return None
    
    def get_floor_id(self, location_id):
        """
        location_id로 층 정보 조회
        
        Args:
            location_id (int): 위치 ID
            
        Returns:
            int: floor_id 또는 None
        """
        location = self.get_location_info(location_id)
        return location["floor_id"] if location else None
    
    def need_elevator(self, current_floor_id, target_location_id):
        """
        엘리베이터가 필요한지 확인
        
        Args:
            current_floor_id (int): 현재 층
            target_location_id (int): 목적지 위치 ID
            
        Returns:
            bool: 엘리베이터 필요 여부
        """
        target_floor = self.get_floor_id(target_location_id)
        if target_floor is None:
            return False
        return current_floor_id != target_floor
    
    def plan_route(self, current_floor_id, target_location_id):
        """
        경로 계획
        
        Args:
            current_floor_id (int): 현재 층
            target_location_id (int): 목적지 위치 ID
            
        Returns:
            list: 경유지 포함한 경로 [location_id, ...]
        """
        if self.need_elevator(current_floor_id, target_location_id):
            # 층이 다르면 엘리베이터 경유
            return [5, target_location_id]  # ELE_1 → 목적지
        else:
            # 같은 층이면 직접 이동
            return [target_location_id]
    
    def get_all_locations(self):
        """
        모든 위치 정보 반환 (디버깅용)
        
        Returns:
            dict: 전체 위치 데이터베이스
        """
        return self.location_database
    
    def load_from_server(self, robot_id):
        """
        나중에 RMS 서버에서 위치 데이터 로드
        TODO: /roomie/command/get_locations 서비스 호출
        
        Args:
            robot_id (int): 로봇 ID
            
        Returns:
            bool: 로드 성공 여부
        """
        # TODO: 서버에서 데이터 받아오기 구현
        print(f"TODO: 서버에서 위치 데이터 로드 (robot_id: {robot_id})")
        return True 