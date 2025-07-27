#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from roomie_msgs.srv import StartCountdown, ReturnCountdown, Location, ControlLock, ReadCardInfo, CheckDoorState, CheckItemLoaded
from roomie_msgs.msg import RobotGuiEvent
from std_srvs.srv import Trigger


class TestGuiNode(Node):
    """RC 테스트를 위한 더미 GUI + VS + IOC 노드"""
    
    def __init__(self):
        super().__init__('test_gui_node')
        
        # GUI 서비스 서버들
        self.start_countdown_server = self.create_service(
            StartCountdown, 
            '/robot_gui/start_countdown', 
            self.start_countdown_callback
        )
        
        self.return_countdown_server = self.create_service(
            ReturnCountdown, 
            '/robot_gui/start_return_countdown', 
            self.return_countdown_callback
        )
        
        self.unlock_door_server = self.create_service(
            Trigger,
            '/robot_gui/unlock_door',
            self.unlock_door_callback
        )
        
        # VS 서비스 서버
        self.vs_location_server = self.create_service(
            Location,
            '/vs/command/location',
            self.vs_location_callback
        )
        
        # IOC 서비스 서버들 추가
        self.ioc_control_lock_server = self.create_service(
            ControlLock,
            '/ioc/control_lock',
            self.ioc_control_lock_callback
        )
        
        self.ioc_read_card_server = self.create_service(
            ReadCardInfo,
            '/ioc/read_card_info',
            self.ioc_read_card_callback
        )
        
        self.ioc_check_door_server = self.create_service(
            CheckDoorState,
            '/ioc/check_door_state',
            self.ioc_check_door_callback
        )
        
        self.ioc_check_item_server = self.create_service(
            CheckItemLoaded,
            '/ioc/check_item_loaded',
            self.ioc_check_item_callback
        )
        
        # 시뮬레이션 상태들
        self.current_location_id = 2  # 2: RES_PICKUP (초기 위치)
        self.drawer_is_open = False    # 서랍 열림 상태  
        self.item_loaded = False       # 물품 적재 상태
        
        # GUI 이벤트 구독 (RC → GUI)
        self.gui_event_sub = self.create_subscription(
            RobotGuiEvent,
            '/robot_gui/event',
            self.gui_event_callback,
            10
        )
        
        # GUI 이벤트 발행 (GUI → RC) - 테스트용
        self.gui_event_pub = self.create_publisher(
            RobotGuiEvent,
            '/robot_gui/event',
            10
        )
        
        self.get_logger().info('🖥️  테스트 GUI + VS + IOC 노드 시작됨')
        self.get_logger().info('📡 GUI 서비스 서버들:')
        self.get_logger().info('   - /robot_gui/start_countdown')
        self.get_logger().info('   - /robot_gui/start_return_countdown')
        self.get_logger().info('   - /robot_gui/unlock_door')
        self.get_logger().info('📡 VS 서비스 서버:')
        self.get_logger().info('   - /vs/command/location')
        self.get_logger().info('🔧 IOC 서비스 서버들:')
        self.get_logger().info('   - /ioc/control_lock')
        self.get_logger().info('   - /ioc/read_card_info')
        self.get_logger().info('   - /ioc/check_door_state')
        self.get_logger().info('   - /ioc/check_item_loaded')
        self.get_logger().info('📺 토픽 구독: /robot_gui/event')
        self.get_logger().info(f'📍 시뮬레이션 현재 위치: {self.get_location_name(self.current_location_id)}')
        self.get_logger().info(f'🔒 서랍 상태: 열림={self.drawer_is_open}, 물품={self.item_loaded}')
        self.get_logger().info('🔄 물품 상태는 확인 서비스 호출시마다 자동 토글됩니다')
    
    def get_location_name(self, location_id):
        """위치 ID를 이름으로 변환"""
        location_names = {
            0: "LOB_WAITING",
            1: "LOB_CALL", 
            2: "RES_PICKUP",
            3: "RES_CALL",
            4: "SUP_PICKUP",
            5: "ELE_1",
            6: "ELE_2",
            101: "ROOM_101",
            102: "ROOM_102"
        }
        return location_names.get(location_id, f"UNKNOWN_{location_id}")
    
    def vs_location_callback(self, request, response):
        """VS 위치 서비스 응답 (시뮬레이션)"""
        self.get_logger().info('📍 [VS 서비스 호출됨] 현재 위치 요청!')
        self.get_logger().info(f'   - robot_id: {request.robot_id}')
        
        # 시뮬레이션 응답
        response.robot_id = request.robot_id
        response.location_id = self.current_location_id
        
        location_name = self.get_location_name(self.current_location_id)
        self.get_logger().info(f'   - 응답: location_id={self.current_location_id} ({location_name})')
        self.get_logger().info('✅ VS 위치 서비스 응답 완료')
        
        return response
    
    def ioc_control_lock_callback(self, request, response):
        """IOC 서랍 잠금 제어 서비스 응답"""
        action = "잠금" if request.locked else "해제"
        self.get_logger().info(f'🔧 [IOC 서비스 호출됨] 서랍 {action} 요청!')
        self.get_logger().info(f'   - robot_id: {request.robot_id}')
        self.get_logger().info(f'   - locked: {request.locked}')
        
        # 시뮬레이션: 서랍 상태 변경
        # old_state = self.drawer_is_locked # Removed
        # self.drawer_is_locked = request.locked # Removed
        
        # 서랍이 해제되면 열림 상태로, 잠금되면 닫힘 상태로
        if not request.locked:  # 해제
            self.drawer_is_open = True
        else:  # 잠금
            self.drawer_is_open = False
        
        response.robot_id = request.robot_id
        response.success = True
        
        # self.get_logger().info(f'   - 서랍 상태 변경: 잠금 {old_state} → {self.drawer_is_locked}') # Removed
        self.get_logger().info(f'   - 서랍 열림 상태: {self.drawer_is_open}')
        self.get_logger().info('✅ IOC 서랍 제어 서비스 응답 완료')
        
        return response
    
    def ioc_read_card_callback(self, request, response):
        """IOC 카드 인식 서비스 응답"""
        self.get_logger().info('💳 [IOC 서비스 호출됨] 카드 인식 요청!')
        self.get_logger().info(f'   - robot_id: {request.robot_id}')
        
        # 시뮬레이션: 현재 위치의 카드로 인식
        response.robot_id = request.robot_id
        response.success = True
        response.location_id = self.current_location_id
        
        location_name = self.get_location_name(self.current_location_id)
        self.get_logger().info(f'   - 인식된 카드: location_id={self.current_location_id} ({location_name})')
        self.get_logger().info('✅ IOC 카드 인식 서비스 응답 완료')
        
        return response
    
    def ioc_check_door_callback(self, request, response):
        """IOC 서랍 문 상태 확인 서비스 응답"""
        self.get_logger().info('🚪 [IOC 서비스 호출됨] 서랍 문 상태 확인!')
        self.get_logger().info(f'   - robot_id: {request.robot_id}')
        
        response.robot_id = request.robot_id
        response.is_opened = self.drawer_is_open
        
        status = "열림" if self.drawer_is_open else "닫힘"
        self.get_logger().info(f'   - 서랍 문 상태: {status}')
        self.get_logger().info('✅ IOC 서랍 문 상태 서비스 응답 완료')
        
        return response
    
    def ioc_check_item_callback(self, request, response):
        """IOC 물품 적재 상태 확인 서비스 응답 (자동 토글)"""
        self.get_logger().info('📦 [IOC 서비스 호출됨] 물품 적재 상태 확인!')
        self.get_logger().info(f'   - robot_id: {request.robot_id}')
        
        # 🔄 자동 토글: 호출할 때마다 상태 변경
        old_state = self.item_loaded
        self.item_loaded = not self.item_loaded  # 토글
        
        response.robot_id = request.robot_id
        response.item_loaded = self.item_loaded
        
        old_status = "적재됨" if old_state else "없음"
        new_status = "적재됨" if self.item_loaded else "없음"
        self.get_logger().info(f'   - 물품 상태 토글: {old_status} → {new_status}')
        self.get_logger().info(f'   - 응답값: item_loaded={self.item_loaded}')
        self.get_logger().info('✅ IOC 물품 상태 서비스 응답 완료 (자동 토글됨)')
        
        return response
    
    def set_item_loaded(self, loaded: bool):
        """물품 적재 상태 수동 변경 (테스트용)"""
        old_state = self.item_loaded
        self.item_loaded = loaded
        status = "적재됨" if loaded else "제거됨"
        self.get_logger().info(f'📦 물품 상태 변경: {old_state} → {loaded} ({status})')
    
    def start_countdown_callback(self, request, response):
        """출발 카운트다운 서비스 응답"""
        self.get_logger().info('🚀 [서비스 호출됨] 출발 카운트다운 시작!')
        self.get_logger().info(f'   - robot_id: {request.robot_id}')
        self.get_logger().info(f'   - task_id: {request.task_id}')
        self.get_logger().info(f'   - task_type_id: {request.task_type_id}')
        
        # 성공 응답
        response.robot_id = request.robot_id
        response.success = True
        response.reason = 0
        
        self.get_logger().info('✅ 카운트다운 서비스 응답 완료')
        return response
    
    def return_countdown_callback(self, request, response):
        """복귀 카운트다운 서비스 응답"""
        self.get_logger().info('🏠 [서비스 호출됨] 복귀 카운트다운 시작!')
        self.get_logger().info(f'   - robot_id: {request.robot_id}')
        
        # 성공 응답
        response.robot_id = request.robot_id
        response.success = True
        response.reason = 0
        
        self.get_logger().info('✅ 복귀 카운트다운 서비스 응답 완료')
        return response
    
    def unlock_door_callback(self, request, response):
        """도어 잠금 해제 서비스 응답"""
        self.get_logger().info('🔓 [서비스 호출됨] 도어 잠금 해제!')
        
        # 성공 응답
        response.success = True
        response.message = "도어 잠금 해제 성공"
        
        self.get_logger().info('✅ 도어 잠금 해제 서비스 응답 완료')
        return response
    
    def gui_event_callback(self, msg):
        """GUI 이벤트 수신 (RC → GUI)"""
        self.get_logger().info('📨 [이벤트 수신] RC → GUI')
        self.get_logger().info(f'   - robot_id: {msg.robot_id}')
        self.get_logger().info(f'   - event_id: {msg.rgui_event_id}')
        self.get_logger().info(f'   - task_id: {msg.task_id}')
        self.get_logger().info(f'   - detail: {msg.detail}')
        
        # 특정 이벤트에 대한 자동 응답 (테스트용)
        if msg.rgui_event_id == 13:  # 픽업장소 이동 종료
            self.get_logger().info('🎯 픽업장소 도착! 5초 후 [서랍 열기] 버튼 클릭 시뮬레이션')
            # 실제로는 사용자가 클릭하지만, 테스트를 위해 자동으로
            import threading
            threading.Timer(5.0, self.simulate_drawer_open_click, [msg.task_id]).start()
        
        elif msg.rgui_event_id == 15:  # 배송장소 이동 종료  
            self.get_logger().info('🏁 배송장소 도착! 배송 시나리오 시뮬레이션 시작')
            import threading
            threading.Timer(5.0, self.simulate_delivery_scenario, [msg.task_id]).start()
    
    def simulate_drawer_open_click(self, task_id):
        """[서랍 열기] 버튼 클릭 시뮬레이션 (픽업용)"""
        self.get_logger().info('👆 [픽업 시뮬레이션] 1단계: 서랍 열기 버튼 클릭!')
        
        event_msg = RobotGuiEvent()
        event_msg.robot_id = 1
        event_msg.rgui_event_id = 104  # [서랍 열기] 클릭
        event_msg.task_id = task_id
        event_msg.timestamp = self.get_clock().now().to_msg()
        event_msg.detail = "픽업 - 사용자 서랍 열기 요청"
        
        self.gui_event_pub.publish(event_msg)
        self.get_logger().info('📤 이벤트 104 (픽업용 서랍 열기) 전송 완료')
        
        # 픽업의 경우 5초 후 적재 완료 버튼 클릭 시뮬레이션
        self.get_logger().info('⏱️ 5초 후 [적재 완료] 버튼 클릭 시뮬레이션 예정')
        import threading
        threading.Timer(5.0, self.simulate_loading_complete_click, [task_id]).start()

    def simulate_delivery_scenario(self, task_id):
        """배송 시나리오 시뮬레이션 (서랍 열기 → 수령 완료)"""
        self.get_logger().info('🚚 [배송 시뮬레이션] 1단계: 서랍 열기 버튼 클릭!')
        
        # 1단계: 서랍 열기 (event_id=104)
        event_msg = RobotGuiEvent()
        event_msg.robot_id = 1
        event_msg.rgui_event_id = 104  # [서랍 열기] 클릭
        event_msg.task_id = task_id
        event_msg.timestamp = self.get_clock().now().to_msg()
        event_msg.detail = "배송 - 사용자 서랍 열기 요청"
        
        self.gui_event_pub.publish(event_msg)
        self.get_logger().info('📤 이벤트 104 (배송용 서랍 열기) 전송 완료')
        
        # 2단계: 7초 후 수령 완료 (event_id=100)
        self.get_logger().info('⏱️ 7초 후 [수령 완료] 버튼 클릭 시뮬레이션 예정')
        import threading
        threading.Timer(7.0, self.simulate_pickup_complete_click, [task_id]).start()

    def simulate_pickup_complete_click(self, task_id):
        """[수령 완료] 버튼 클릭 시뮬레이션 (배송용)"""
        self.get_logger().info('📦 [배송 시뮬레이션] 2단계: 수령 완료 버튼 클릭!')
        
        # 배송 시뮬레이션: 사용자가 물품을 가져감
        self.get_logger().info('📦 물품 제거 시뮬레이션 (사용자가 가져감)')
        self.set_item_loaded(False)
        
        event_msg = RobotGuiEvent()
        event_msg.robot_id = 1
        event_msg.rgui_event_id = 100  # [수령 완료] 클릭
        event_msg.task_id = task_id
        event_msg.timestamp = self.get_clock().now().to_msg()
        event_msg.detail = "배송 - 사용자 수령 완료"
        
        self.gui_event_pub.publish(event_msg)
        self.get_logger().info('📤 이벤트 100 (수령 완료) 전송 완료')
        
        # 배송 완료 후 복귀 위치로 변경
        self.get_logger().info('🏠 배송 완료! 복귀 위치로 변경')
        self.change_location(0)  # LOB_WAITING으로 복귀
    
    def change_location(self, new_location_id):
        """현재 위치 변경 (시뮬레이션)"""
        old_location = self.current_location_id
        old_name = self.get_location_name(old_location)
        new_name = self.get_location_name(new_location_id)
        
        self.current_location_id = new_location_id
        
        self.get_logger().info(f'📍 위치 변경: {old_name}({old_location}) → {new_name}({new_location_id})')
    
    def simulate_loading_complete_click(self, task_id):
        """[적재 완료] 버튼 클릭 시뮬레이션"""
        self.get_logger().info('📦 [픽업 시뮬레이션] 2단계: 적재 완료 버튼 클릭!')
        
        event_msg = RobotGuiEvent()
        event_msg.robot_id = 1
        event_msg.rgui_event_id = 105  # [적재 완료] 클릭
        event_msg.task_id = task_id
        event_msg.timestamp = self.get_clock().now().to_msg()
        event_msg.detail = "픽업 - 사용자 적재 완료 확인"
        
        self.gui_event_pub.publish(event_msg)
        self.get_logger().info('📤 이벤트 105 (적재 완료) 전송 완료')
        
        # 픽업 완료 후 배송 장소로 위치 변경
        self.get_logger().info('🚚 픽업 완료! 배송 장소로 위치 변경')
        self.change_location(101)  # ROOM_101로 이동


def main(args=None):
    rclpy.init(args=args)
    node = TestGuiNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main() 