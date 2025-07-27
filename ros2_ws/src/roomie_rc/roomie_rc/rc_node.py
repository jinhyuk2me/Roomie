#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from .rms_client import RMSClient
from .gui_client import GUIClient  
from .vs_client import VSClient
from .ioc_client import IOCClient
from .location_manager import LocationManager
from .nav_client import NavClient # 새로 추가


import threading


class RCNode(Node):
    """
    Roomie Robot Controller (RC) Node
    로봇 제어의 중심 노드
    """
    
    def __init__(self):
        super().__init__('rc_node')
        
        # 로봇 정보
        self.robot_id = 1  # TODO: 파라미터로 받기
        self.current_task = None
        self.robot_state = 1  # 1: 작업 가능
        self.current_floor_id = 0  # 현재 로봇이 있는 층 (0: 1층)
        self.current_task_state_id = 0  # 현재 작업 상태 ID
        
        # 위치 관리자 초기화
        self.location_manager = LocationManager()
        
        # 작업 관련 정보 저장
        self.order_info_string = ""  # order_info 원본 문자열 저장
        self.pickup_location_info = None
        self.target_location_info = None
        self.current_action_goal_handle = None  # 현재 PerformTask Action Goal Handle
        
        # 통신 클라이언트 초기화
        self.rms_client = RMSClient(self)
        self.gui_client = GUIClient(self)
        self.vs_client = VSClient(self)
        self.ioc_client = IOCClient(self)
        self.nav_client = NavClient(self)
        
        # 주기적 상태 발행 타이머 (5초마다)
        self.status_timer = self.create_timer(5.0, self.publish_periodic_status)
        
        self.get_logger().info('RC Node가 시작되었습니다.')
        self.get_logger().info(f'Robot ID: {self.robot_id}')
        self.get_logger().info(f'현재 층: {self.current_floor_id} (1층)')
        
        # 위치 데이터베이스 정보 로그
        self.log_location_database()
        
        # 초기 상태 발행
        self.publish_initial_status()
    
    def log_location_database(self):
        """위치 데이터베이스 정보 로그 출력"""
        self.get_logger().info('=== 위치 데이터베이스 ===')
        for location_id, info in self.location_manager.get_all_locations().items():
            self.get_logger().info(f'ID {location_id}: {info["name"]} ({info["x"]}, {info["y"]}) floor={info["floor_id"]}')
    
    def publish_initial_status(self):
        """초기 상태 발행"""
        self.get_logger().info('초기 상태 발행 중...')
        self.rms_client.publish_robot_state(self.robot_state)
        self.rms_client.publish_battery_status(85.0, False)
        self.rms_client.publish_roomie_pose(self.current_floor_id, 0.0, 0.0, 0.0)
    
    def publish_periodic_status(self):
        """주기적 상태 발행"""
        self.rms_client.publish_robot_state(self.robot_state)  # task_id 제거
        self.rms_client.publish_battery_status(85.0, False)  # TODO: 실제 배터리 상태 읽기
        self.rms_client.publish_roomie_pose(self.current_floor_id, 0.0, 0.0, 0.0)  # TODO: 실제 위치 읽기
    
    def change_robot_state(self, new_state):
        """로봇 상태 변경"""
        self.robot_state = new_state
        self.get_logger().info(f'로봇 상태 변경: {new_state}')
        
        # RMS에게 상태 발행 (task_id 제거)
        self.rms_client.publish_robot_state(new_state)
    
    def handle_task_assignment(self, task_goal, goal_handle=None):
        """작업 할당 처리"""
        self.get_logger().info('=== 작업 할당 처리 시작 ===')
        
        # 1. 작업 정보 저장 (goal_handle은 더 이상 사용하지 않음)
        self.current_task = task_goal
        self.order_info_string = task_goal.order_info  # 원본 문자열 저장
        
        # 2. 장소 정보 조회
        self.pickup_location_info = self.location_manager.get_location_info(task_goal.pickup_location_id)
        self.target_location_info = self.location_manager.get_location_info(task_goal.target_location_id)
        
        if not self.pickup_location_info or not self.target_location_info:
            self.get_logger().error(f'장소 정보를 찾을 수 없습니다. 픽업: {task_goal.pickup_location_id}, 배송: {task_goal.target_location_id}')
            return
        
        # 3. 로봇 상태 변경 (1: 작업 가능 → 3: 작업 수행 중)
        self.change_robot_state(3)  # 3: 작업 수행 중
        
        # 4. 작업 정보 로그
        self.get_logger().info(f'작업 시작: task_id={task_goal.task_id}')
        self.get_logger().info(f'픽업 장소: {self.pickup_location_info["name"]} ({self.pickup_location_info["x"]}, {self.pickup_location_info["y"]})')
        self.get_logger().info(f'배송 장소: {self.target_location_info["name"]} ({self.target_location_info["x"]}, {self.target_location_info["y"]})')
        self.get_logger().info(f'주문 정보: {self.order_info_string}')
        
        # 5. 경로 계획
        pickup_route = self.location_manager.plan_route(self.current_floor_id, task_goal.pickup_location_id)
        self.get_logger().info(f'픽업 경로: {pickup_route}')
        
        # 6. 다음 단계 안내
        self.get_logger().info('작업 할당 완료. RMS에서 task_state_id=3 전송 대기 중...')

    def handle_task_state_change(self, task_state_msg):
        """작업 상태 변경 처리"""
        # 현재 작업 상태 ID와 수신된 작업 상태 ID가 동일하면 중복 처리 방지
        if self.current_task_state_id == task_state_msg.task_state_id:
            # self.get_logger().info(f'이미 처리 중인 작업 상태({task_state_msg.task_state_id})입니다. 중복 실행을 건너뜁니다.')
            return # 함수 실행을 여기서 중단
        
        self.get_logger().info(f'작업 상태 변경 처리: state={task_state_msg.task_state_id}')
        
        # 현재 작업 상태 ID 업데이트
        self.current_task_state_id = task_state_msg.task_state_id
        
        # 작업 상태에 따른 동작 수행
        if task_state_msg.task_state_id == 3:  # 픽업 장소로 이동
            self.get_logger().info('픽업 장소로 이동 상태 확인 - 카운트다운 시작')
            
            # GUI 카운트다운 서비스 호출
            if self.current_task:
                self.gui_client.start_countdown(self.current_task.robot_id, self.current_task.task_id, self.current_task.task_type_id)

            # TODO: 주행 주행 주행
            self.get_logger().info('TODO: 픽업 장소로 실제 내비게이션 시작')
            # 픽업 장소의 목표 Pose 생성 (LocationManager에서 정보 가져옴)
            pickup_location_info = self.location_manager.get_location_info(self.current_task.pickup_location_id)
            if pickup_location_info:
                # TODO: 필요하다면 location_info에 yaw 값 추가
                goal_pose = self.nav_client.create_goal_pose(pickup_location_info, yaw_radians=0.0) 
                self.nav_client.go_to_pose(goal_pose, lambda success, stage: self._navigation_completed_callback(success, 'pickup'))
            else:
                self.get_logger().error(f"픽업 장소 {self.current_task.pickup_location_id} 정보를 찾을 수 없습니다.")
                # TODO: 내비게이션 불가 시 에러 처리


            
        elif task_state_msg.task_state_id == 4:  # 픽업 대기 중
            self.get_logger().info('픽업 대기 처리 시작')
            
            # GUI에 픽업장소 이동 종료 이벤트 (order_info 포함)
            self.gui_client.send_gui_event(
                event_id=13,  # 픽업장소 이동 종료
                detail=self.order_info_string,  # 파싱 없이 원본 전달
                task_id=task_state_msg.task_id
            )
            
            # event_id=104 ([서랍 열기] 클릭) 대기
            self.get_logger().info('event_id=104 ([서랍 열기] 클릭) 대기 중...')
            
        elif task_state_msg.task_state_id == 5:  # 배송 중
            self.get_logger().info('배송 장소로 이동 상태 확인')
            
            # 배송 경로 계획
            delivery_route = self.location_manager.plan_route(self.current_floor_id, self.current_task.target_location_id)
            self.get_logger().info(f'배송 경로: {delivery_route}')
            

            # TODO: 배송 장소로 실제 내비게이션 시작
            self.get_logger().info('TODO: 배송 장소로 실제 내비게이션 시작')

            # 배송 장소의 목표 Pose 생성
            target_location_info = self.location_manager.get_location_info(self.current_task.target_location_id)
            if target_location_info:
                # TODO: 필요하다면 location_info에 yaw 값 추가
                goal_pose = self.nav_client.create_goal_pose(target_location_info, yaw_radians=3.14) 
                self.nav_client.go_to_pose(goal_pose, lambda success, stage: self._navigation_completed_callback(success, 'delivery'))
            else:
                self.get_logger().error(f"배송 장소 {self.current_task.target_location_id} 정보를 찾을 수 없습니다.")
                # TODO: 내비게이션 불가 시 에러 처리

            
        elif task_state_msg.task_state_id == 6:  # 배송 도착
            self.get_logger().info('배송 도착 처리 시작')
            
            # GUI에 배송장소 이동 종료 이벤트 (order_info 포함)
            self.gui_client.send_gui_event(
                event_id=15,  # 배송장소 이동 종료
                detail=self.order_info_string,  # 파싱 없이 원본 전달
                task_id=task_state_msg.task_id
            )
            
            # 배송 처리는 GUI Event (event_id=104, 105)로 진행됨
            self.get_logger().info('event_id=104 ([서랍 열기] 클릭) 대기 중...')
            
        elif task_state_msg.task_state_id == 7:  # 수령 완료
            self.get_logger().info('=== 배송 작업 완료 처리 시작 ===')
            
            # 1. 작업 변수들 초기화
            self.reset_task_variables()
            
            # 2. 로봇 상태 전환: 3(작업 수행 중) → 4(복귀 대기 중)
            self.change_robot_state(4)
            self.get_logger().info('복귀 대기 중... PerformReturn 액션 대기')
            
            # 3. PerformReturn 액션을 기다림 (별도 액션 서버에서 처리)
        
        else:
            self.get_logger().info(f'처리되지 않은 작업 상태: {task_state_msg.task_state_id}')


    def _navigation_completed_callback(self, success: bool, stage: str):
        """
        NavClient로부터 내비게이션 완료 결과를 받아 처리하는 콜백 함수.
        Args:
            success (bool): 내비게이션 성공 여부
            stage (str): 'pickup', 'delivery', 'return' 중 현재 내비게이션 단계
        """
        if success:
            self.get_logger().info(f'내비게이션 성공: {stage} 단계')
            if stage == 'pickup': 
                # TODO: 도착 후 위치 확인 (VS)
                current_location, location_name = self.vs_client.get_location_info()
                self.get_logger().info(f'현재 위치: {location_name} (ID: {current_location})')
                
                # 시뮬레이션: 즉시 픽업 장소 도착으로 처리
                self.simulate_arrival_at_pickup_location()
            elif stage == 'delivery':
                # 기존 배송 도착 시뮬레이션 로직 실행
                # TODO: 도착 후 위치 확인 (VS)
                current_location, location_name = self.vs_client.get_location_info()
                self.get_logger().info(f'현재 위치: {location_name} (ID: {current_location})')
                
                # 시뮬레이션: 즉시 픽업 장소 도착으로 처리
                self.simulate_arrival_at_delivery_location()
            elif stage == 'return':
                # 기존 복귀 도착 시뮬레이션 로직 실행

                # TODO: 내비게이션 시작 후 위치 확인 (VS)
                # current_location, location_name = self.vs_client.get_location_info()
                # self.get_logger().info(f'현재 위치: {location_name} (ID: {current_location})')

                self.simulate_arrival_at_return_location()
                self.get_logger().info("로봇 복귀 완료. 로봇 상태를 '사용 가능'으로 변경")
                self.rms_client.publish_robot_state(1) # 1: 작업 가능
        else:
            self.get_logger().error(f'내비게이션 실패: {stage} 단계')
            # TODO: 내비게이션 실패 시 처리 로직
            # - 로봇 상태 변경 (예: 오류 상태, 대기)
            # - 사용자/RMS에 알림
            # - 재시도 로직 등
            if stage == 'pickup' or stage == 'delivery':
                self.rms_client.publish_robot_state(1) # 일단 작업 가능 상태로 돌림 (임시)
                self.rms_client.cancel_task(self.current_task.task_id) # 해당 작업 취소 (예시)
            elif stage == 'return':
                self.rms_client.publish_robot_state(1) # 복귀 실패해도 일단 사용 가능으로


    
    def handle_gui_event(self, gui_event_msg):
        """GUI 이벤트 처리 (RGUI → RC)"""
        event_id = gui_event_msg.rgui_event_id
        self.get_logger().info(f'GUI 이벤트 처리: event_id={event_id}')
        
        # 실제 배송 작업 이벤트 ID 처리
        if event_id == 104:  # [서랍 열기] 클릭
            self.get_logger().info('[서랍 열기] 버튼 클릭됨')
            
            if self.current_task_state_id == 4:  # 픽업 대기 중
                self.get_logger().info('픽업 단계 - 서랍 열기 요청 처리')
                self.handle_drawer_open_request(gui_event_msg.task_id)
            elif self.current_task_state_id == 6:  # 배송 도착
                self.get_logger().info('배송 단계 - 서랍 열기 요청 처리')
                self.handle_drawer_open_request(gui_event_msg.task_id)
            else:
                self.get_logger().warn(f'예상하지 못한 상태에서 서랍 열기 요청: task_state_id={self.current_task_state_id}')
            
        elif event_id == 105:  # [적재 완료] 클릭 (픽업 전용)
            self.get_logger().info('[적재 완료] 버튼 클릭됨')
            
            if self.current_task_state_id == 4:  # 픽업 대기 중
                self.get_logger().info('픽업 단계 - 적재 완료 요청 처리')
                self.handle_loading_complete_request(gui_event_msg.task_id)
            else:
                self.get_logger().warn(f'픽업 대기 상태가 아닌데 적재 완료 요청: task_state_id={self.current_task_state_id}')
                
        elif event_id == 100:  # [수령 완료] 클릭 (배송 전용)
            self.get_logger().info('[수령 완료] 버튼 클릭됨')
            
            if self.current_task_state_id == 6:  # 배송 도착
                self.get_logger().info('배송 단계 - 수령 완료 요청 처리')
                self.handle_delivery_complete_request(gui_event_msg.task_id)
            else:
                self.get_logger().warn(f'배송 도착 상태가 아닌데 수령 완료 요청: task_state_id={self.current_task_state_id}')
            
        # TODO: 나중에 구현할 이벤트들
        # elif event_id == 13:  # 픽업장소 이동 종료 (RC → GUI)
        # elif event_id == 15:  # 배송장소 이동 종료 (RC → GUI)  
        # elif event_id == 16:  # 서랍 열림 (RC → GUI)
        # elif event_id == 27:  # 적재 이상 (RC → GUI)
        
        else:
            self.get_logger().info(f'알 수 없는 GUI 이벤트: {event_id}')
    
    def handle_drawer_open_request(self, task_id):
        """서랍 열기 요청 처리"""
        self.get_logger().info('서랍 열기 요청 처리')
        
        # 1. IOC로 서랍 열기
        if self.ioc_client.unlock_drawer():
            self.get_logger().info('서랍 열기 성공')
            
            # 2. GUI에 서랍 열림 알림
            self.gui_client.send_gui_event(
                event_id=16,  # 서랍 열림
                detail="서랍이 열렸습니다",
                task_id=task_id
            )
            
            # TODO: 문 닫힘 확인 및 적재 상태 체크
            
        else:
            self.get_logger().error('서랍 열기 실패')
    
    def handle_loading_complete_request(self, task_id):
        """적재 완료 요청 처리 (event_id=105)"""
        self.get_logger().info('[적재 완료] 요청 처리 시작')
        self.get_logger().info('📋 시나리오: 105 → 서랍 닫힘 확인 → 물품 확인')
        
        # 서랍 닫힘 확인 루프 시작
        self.check_door_closing_loop()
    
    def check_door_closing_loop(self):
        """서랍 닫힘 확인 루프 (is_opened=false가 될 때까지 반복)"""
        self.get_logger().info('🚪 서랍 닫힘 상태 확인 중...')
        
        # IOC 서랍 상태 확인 서비스 호출
        is_door_open = self.ioc_client.is_drawer_open()
        
        if is_door_open:
            # 서랍이 열려있음 → event_id=16 전송 + 계속 확인
            self.get_logger().info('🚪 서랍이 아직 열려있음 → event_id=16 전송')
            self.gui_client.send_gui_event(16, "서랍이 열려있습니다", self.current_task.task_id)
            
            # 0.5초 후 다시 확인 (루프)
            timer = threading.Timer(0.5, self.check_door_closing_loop)
            timer.start()
        else:
            # 서랍이 닫혀있음 → 물품 확인으로 이동
            self.get_logger().info('✅ 서랍이 닫혔음 → 물품 적재 상태 확인')
            self.check_item_loading()
    
    def check_item_loading(self):
        """물품 상태 확인 (픽업/배송 공용)"""
        self.get_logger().info('📦 물품 상태 확인 중...')
        
        # IOC 물품 상태 확인 서비스 호출
        has_item = self.ioc_client.has_item()
        
        if self.current_task_state_id == 4:  # 픽업 대기 중
            if has_item:
                # 물품 감지됨 → 픽업 완료 시퀀스 시작
                self.get_logger().info('✅ 물품 감지됨 → 픽업 완료 시퀀스 시작')
                self.complete_pickup_sequence()
            else:
                # 물품 미감지 → event_id=27 전송 + 105 대기
                self.get_logger().info('❌ 물품 미감지 → event_id=27 전송 (적재 이상)')
                self.gui_client.send_gui_event(27, "적재 이상 - 물품이 감지되지 않습니다", self.current_task.task_id)
                self.get_logger().info('⏳ event_id=105 ([적재 완료] 클릭) 대기 중...')
                # 다시 105를 기다림 (handle_gui_event에서 자동 처리)
                
        elif self.current_task_state_id == 6:  # 배송 도착
            if not has_item:
                # 물품 없음 → 수령 완료 → 배송 완료 시퀀스 시작
                self.get_logger().info('✅ 물품 수령 확인됨 → 배송 완료 시퀀스 시작')
                self.complete_delivery_sequence()
            else:
                # 물품 아직 있음 → 수령 대기
                self.get_logger().info('❌ 물품이 아직 있음 → event_id=27 전송 (수령 대기)')
                self.gui_client.send_gui_event(27, "수령 대기 - 물품을 가져가 주세요", self.current_task.task_id)
                self.get_logger().info('⏳ event_id=100 ([수령 완료] 클릭) 대기 중...')
                
    
    def complete_pickup_sequence(self):
        """픽업 완료 시퀀스 (시퀀스 다이어그램 순서대로)"""
        self.get_logger().info('🎯 픽업 완료 시퀀스 시작')
        
        # 1. 서랍 잠금 제어 요청 (locked=True)
        self.get_logger().info('1️⃣ 서랍 잠금 요청 중...')
        lock_success = self.ioc_client.lock_drawer()
        
        if not lock_success:
            self.get_logger().error('❌ 서랍 잠금 실패 - 픽업 완료 중단')
            return
        
        self.get_logger().info('✅ 서랍 잠금 성공')
        
        # 2. 출발 카운트다운 서비스 요청
        self.get_logger().info('2️⃣ 출발 카운트다운 요청 중...')
        countdown_success = self.gui_client.start_countdown(
            self.current_task.robot_id,
            self.current_task.task_id, 
            self.current_task.task_type_id
        )
        
        if not countdown_success:
            self.get_logger().error('❌ 출발 카운트다운 실패 - 픽업 완료 중단')
            return
        
        self.get_logger().info('✅ 출발 카운트다운 성공')
        
        # 3. 픽업 완료 이벤트 발행
        self.get_logger().info('3️⃣ 픽업 완료 이벤트 발행 중...')
        self.rms_client.publish_pickup_completed(self.current_task.task_id)
        self.get_logger().info('✅ 픽업 완료 이벤트 발행 완료')
        
        # 4. 작업 상태 변경 대기 (handle_task_state_change에서 자동 처리)
        self.get_logger().info('4️⃣ 작업 상태 변경 대기 중... (RMS가 task_state_id=5로 변경할 예정)')
        self.get_logger().info('🎉 픽업 완료 시퀀스 완료!')

    def handle_delivery_complete_request(self, task_id):
        """배송 완료 요청 처리 (수령 완료)"""
        self.get_logger().info('[배송 완료] 요청 처리 시작')
        self.get_logger().info('📋 시나리오: 100 → 서랍 닫힘 확인 → 물품 수령 확인')
        
        # 서랍 닫힘 확인 루프 시작 (픽업과 동일한 로직)
        self.check_door_closing_loop()

    def complete_delivery_sequence(self):
        """배송 완료 시퀀스"""
        self.get_logger().info('🎯 배송 완료 시퀀스 시작')
        
        if not self.current_task:
            self.get_logger().error('현재 작업이 없습니다')
            return
        
        # 1. 서랍 잠금
        self.get_logger().info('1️⃣ 서랍 잠금 요청 중...')
        if self.ioc_client.lock_drawer():
            self.get_logger().info('✅ 서랍 잠금 성공')
        else:
            self.get_logger().warn('⚠️ 서랍 잠금 실패')
        
        # 2. 감사 인사 화면 표시
        self.get_logger().info('2️⃣ 감사 인사 화면 표시 중...')
        self.gui_client.send_gui_event(
            event_id=18,  # 수령 완료 주문해주셔서 감사합니다
            detail="수령 완료 주문해주셔서 감사합니다",
            task_id=self.current_task.task_id
        )
        self.get_logger().info('✅ 감사 인사 화면 표시 완료')
        
        # 3. 배송 완료 이벤트 발행
        self.get_logger().info('3️⃣ 배송 완료 이벤트 발행 중...')
        self.rms_client.publish_delivery_completed(self.current_task.task_id)
        self.get_logger().info('✅ 배송 완료 이벤트 발행 완료')
        
        # 4. 작업 상태 변경 대기 (task_state_id=7로 변경될 예정)
        self.get_logger().info('4️⃣ 작업 상태 변경 대기 중... (RMS가 task_state_id=7로 변경할 예정)')
        self.get_logger().info('🎉 배송 완료 시퀀스 완료!')

    def complete_perform_task_action(self):
        """PerformTask Action 완료 처리"""
        self.get_logger().info('📋 PerformTask Action 완료 처리 중...')
        
        if self.current_action_goal_handle is None:
            self.get_logger().warn('Action Goal Handle이 없습니다')
            return
        
        # Action Result 생성 및 반환
        from roomie_msgs.action import PerformTask
        result = PerformTask.Result()
        result.robot_id = self.current_task.robot_id if self.current_task else self.robot_id
        result.task_id = self.current_task.task_id if self.current_task else 0
        result.success = True
        result.message = "배송 작업 완료"
        
        # Goal Handle을 통해 결과 반환
        self.current_action_goal_handle.succeed(result)
        self.get_logger().info(f'✅ PerformTask Action 완료: task_id={result.task_id}')

    def reset_task_variables(self):
        """작업 관련 변수들 초기화"""
        self.get_logger().info('🔄 작업 변수들 초기화 중...')
        
        # 작업 관련 변수 초기화
        self.current_task = None
        self.current_task_state_id = 0
        self.order_info_string = ""
        self.pickup_location_info = None
        self.target_location_info = None
        
        self.get_logger().info('✅ 작업 변수들 초기화 완료')

    def handle_return_task(self):
        self.get_logger().info('=== 복귀 작업 시작 ===')
        self.rms_client.publish_robot_state(5) # 5: 복귀중
        
        self.get_logger().info('GUI 복귀 카운트다운 시작 요청')
        self.gui_client.start_return_countdown()
        
        self.get_logger().info('실제 내비게이션 시작: 복귀 장소로 이동 (NavClient 사용)')
        return_location_id = 0 # LOB_WAITING (복귀 대기 장소 ID)
        return_location_info = self.location_manager.get_location_info(return_location_id)
        
        if not return_location_info:
            self.get_logger().error(f'복귀 장소({return_location_id}) 정보를 찾을 수 없습니다!')
            self.change_robot_state(1) # 복귀 실패 시 일단 작업 가능 상태로
            return

        # 복귀 장소의 목표 Pose 생성
        # TODO: 필요하다면 location_info에 yaw 값 추가 (예: 복귀 시 특정 방향을 바라보도록)
        goal_pose = self.nav_client.create_goal_pose(return_location_info, yaw_radians=1.57) 
        
        # NavClient를 통해 내비게이션 시작 및 완료 콜백 연결
        self.nav_client.go_to_pose(goal_pose, lambda success, stage: self._navigation_completed_callback(success, 'return'))




    def simulate_arrival_at_return_location(self):
        """복귀 장소 도착 시뮬레이션"""
        self.get_logger().info('복귀 장소 도착 시뮬레이션 시작')
        
        # 1. VS 위치 인식 서비스 요청
        current_location = self.vs_client.get_current_location()
        self.get_logger().info(f'VS 위치 인식 결과: location_id={current_location}')
        
        # 2. 로봇 상태 전환: 5(복귀 중) → 1(작업 가능)
        self.change_robot_state(1)
        self.get_logger().info('🎉 복귀 완료! 작업 가능 상태로 전환')
        
        self.get_logger().info('복귀 장소 도착 시뮬레이션 완료')

    def handle_unlock_door_request(self):
        """도어 잠금 해제 요청 처리 (RGUI → RC)"""
        self.get_logger().info('도어 잠금 해제 요청 처리')
        
        # IOC를 통한 서랍 잠금 해제
        success = self.ioc_client.unlock_drawer()
        
        if success:
            self.get_logger().info('도어 잠금 해제 성공')
        else:
            self.get_logger().warn('도어 잠금 해제 실패')
        
        return success

    def simulate_arrival_at_pickup_location(self):
        """픽업 장소 도착 시뮬레이션 (나중에 위치 보정하는 알고리즘 적용 필요)"""
        self.get_logger().info('픽업 장소 도착 시뮬레이션 시작')
        
        if not self.current_task:
            self.get_logger().error('현재 작업이 없습니다')
            return
            
        # 1. VS 위치 인식 서비스 요청
        current_location = self.vs_client.get_current_location()
        self.get_logger().info(f'VS 위치 인식 결과: location_id={current_location}')
        
        # 2. RMS에 픽업 장소 도착 이벤트 발행
        pickup_location_id = self.current_task.pickup_location_id
        self.rms_client.publish_arrival_event(pickup_location_id, self.current_task.task_id)
        self.get_logger().info(f'RMS에 픽업 장소 도착 이벤트 발행: location_id={pickup_location_id}, task_id={self.current_task.task_id}')
        
        self.get_logger().info('픽업 장소 도착 시뮬레이션 완료 - RMS가 task_state_id=4로 변경할 예정')

    def simulate_arrival_at_delivery_location(self):
        """배송 장소 도착 시뮬레이션"""
        self.get_logger().info('배송 장소 도착 시뮬레이션 시작')
        
        if not self.current_task:
            self.get_logger().error('현재 작업이 없습니다')
            return
            
        # 1. VS 위치 인식 서비스 요청
        current_location = self.vs_client.get_current_location()
        self.get_logger().info(f'VS 위치 인식 결과: location_id={current_location}')
        
        # 2. RMS에 배송 장소 도착 이벤트 발행
        target_location_id = self.current_task.target_location_id
        self.rms_client.publish_arrival_event(target_location_id, self.current_task.task_id)
        self.get_logger().info(f'RMS에 배송 장소 도착 이벤트 발행: location_id={target_location_id}, task_id={self.current_task.task_id}')
        
        self.get_logger().info('배송 장소 도착 시뮬레이션 완료 - RMS가 task_state_id=6으로 변경할 예정')


def main(args=None):
    rclpy.init(args=args)
    
    try:
        rc_node = RCNode()
        rclpy.spin(rc_node)
    except KeyboardInterrupt:
        pass
    finally:
        if 'rc_node' in locals():
            rc_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main() 