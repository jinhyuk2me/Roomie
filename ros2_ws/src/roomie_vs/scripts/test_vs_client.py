#!/usr/bin/env python3
"""
Vision Service 인터페이스 테스트 클라이언트
rms_vs_interface.md에 정의된 모든 서비스 및 토픽 인터페이스를 테스트
"""

import rclpy
from rclpy.node import Node
import threading
import time

# ROS2 메시지 및 서비스 타입들
from roomie_msgs.srv import (
    SetVSMode, 
    ButtonStatus,
    ElevatorWidth,
    ElevatorStatus, 
    DoorStatus,
    SpaceAvailability,
    Location
)
from roomie_msgs.msg import TrackingEvent, Registered


class VSInterfaceTestClient(Node):
    def __init__(self):
        super().__init__('vs_interface_test_client')
        
        # 🔧 Service Clients (rms_vs_interface.md 기준)
        self.service_clients = {
            'set_vs_mode': self.create_client(SetVSMode, '/vs/command/set_vs_mode'),
            'elevator_width': self.create_client(ElevatorWidth, '/vs/command/elevator_width'), 
            'button_status': self.create_client(ButtonStatus, '/vs/command/button_status'),
            'elevator_status': self.create_client(ElevatorStatus, '/vs/command/elevator_status'),
            'door_status': self.create_client(DoorStatus, '/vs/command/door_status'),
            'space_availability': self.create_client(SpaceAvailability, '/vs/command/space_availability'),
            'location': self.create_client(Location, '/vs/command/location')
        }
        
        # 🔧 Topic Subscribers (VS → RC)
        self.tracking_event_sub = self.create_subscription(
            TrackingEvent, '/vs/tracking_event', self.on_tracking_event, 10)
        self.registered_sub = self.create_subscription(
            Registered, '/vs/registered', self.on_registered, 10)
        
        self.get_logger().info("🧪 VS 인터페이스 테스트 클라이언트 시작")
        self.show_menu()
    
    def on_tracking_event(self, msg):
        """추적 이벤트 수신"""
        self.get_logger().info(f"📡 추적 이벤트 수신: robot_id={msg.robot_id}, event_id={msg.tracking_event_id}, task_id={msg.task_id}")
    
    def on_registered(self, msg):
        """등록 완료 이벤트 수신"""
        self.get_logger().info(f"📡 등록 완료 수신: robot_id={msg.robot_id}")
    
    def check_service_availability(self):
        """모든 서비스 가용성 확인"""
        self.get_logger().info("🔍 VS 서비스 가용성 확인 중...")
        print("\n" + "="*70)
        print("📋 VS 서비스 인터페이스 구현 상태")
        print("="*70)
        
        for service_name, client in self.service_clients.items():
            try:
                if client.wait_for_service(timeout_sec=2.0):
                    print(f"✅ {service_name:20} | 구현됨")
                else:
                    print(f"❌ {service_name:20} | 미구현 또는 VS 노드 미실행")
            except Exception as e:
                print(f"❌ {service_name:20} | 에러: {e}")
        
        print("="*70)
        print("명령어를 입력하세요: ", end="")
    
    def test_set_vs_mode(self, mode_id=3):
        """VS 모드 설정 테스트"""
        client = self.service_clients['set_vs_mode']
        if not client.wait_for_service(timeout_sec=2.0):
            self.get_logger().error("❌ SetVSMode 서비스 없음")
            return
            
        request = SetVSMode.Request()
        request.robot_id = 1
        request.mode_id = mode_id
        
        self.get_logger().info(f"📞 VS 모드 설정 호출: mode_id={mode_id}")
        future = client.call_async(request)
        
        def handle_response():
            rclpy.spin_until_future_complete(self, future)
            if future.result():
                response = future.result()
                self.get_logger().info(f"✅ VS 모드 응답: robot_id={response.robot_id}, success={response.success}")
            else:
                self.get_logger().error("❌ VS 모드 설정 실패")
        
        threading.Thread(target=handle_response, daemon=True).start()
    
    def test_button_status(self):
        """버튼 상태 테스트"""
        client = self.service_clients['button_status']
        if not client.wait_for_service(timeout_sec=2.0):
            self.get_logger().error("❌ ButtonStatus 서비스 없음")
            return
            
        request = ButtonStatus.Request()
        request.robot_id = 1
        request.button_ids = [100, 101, 1, 2, 3]  # 하행, 상행, 1층, 2층, 3층
        
        self.get_logger().info(f"📞 버튼 상태 호출: button_ids={request.button_ids}")
        future = client.call_async(request)
        
        def handle_response():
            rclpy.spin_until_future_complete(self, future)
            if future.result():
                response = future.result()
                self.get_logger().info(f"✅ 버튼 상태 응답: {len(response.xs)}개 버튼")
                for i in range(len(response.xs)):
                    pressed_str = "눌림" if response.is_pressed[i] else "안눌림"
                    self.get_logger().info(f"   버튼 {request.button_ids[i]}: ({response.xs[i]:.3f}, {response.ys[i]:.3f}, {response.depths[i]:.3f}) - {pressed_str}")
            else:
                self.get_logger().error("❌ 버튼 상태 호출 실패")
        
        threading.Thread(target=handle_response, daemon=True).start()
    
    def test_elevator_width(self):
        """엘리베이터 너비 테스트"""
        client = self.service_clients['elevator_width']
        if not client.wait_for_service(timeout_sec=2.0):
            self.get_logger().error("❌ ElevatorWidth 서비스 없음")
            return
            
        request = ElevatorWidth.Request()
        request.robot_id = 1
        
        self.get_logger().info("📞 엘리베이터 너비 호출")
        future = client.call_async(request)
        
        def handle_response():
            rclpy.spin_until_future_complete(self, future)
            if future.result():
                response = future.result()
                self.get_logger().info(f"✅ 엘리베이터 너비 응답: left={response.left_boundary:.3f}, right={response.right_boundary:.3f}")
            else:
                self.get_logger().error("❌ 엘리베이터 너비 호출 실패")
        
        threading.Thread(target=handle_response, daemon=True).start()
    
    def test_elevator_status(self):
        """엘리베이터 상태 테스트"""
        client = self.service_clients['elevator_status']
        if not client.wait_for_service(timeout_sec=2.0):
            self.get_logger().error("❌ ElevatorStatus 서비스 없음")
            return
            
        request = ElevatorStatus.Request()
        request.robot_id = 1
        
        self.get_logger().info("📞 엘리베이터 상태 호출")
        future = client.call_async(request)
        
        def handle_response():
            rclpy.spin_until_future_complete(self, future)
            if future.result():
                response = future.result()
                direction_str = "상행" if response.direction == 0 else "하행"
                self.get_logger().info(f"✅ 엘리베이터 상태 응답: {direction_str}, {response.position}층")
            else:
                self.get_logger().error("❌ 엘리베이터 상태 호출 실패")
        
        threading.Thread(target=handle_response, daemon=True).start()
    
    def test_door_status(self):
        """문 상태 테스트"""
        client = self.service_clients['door_status']
        if not client.wait_for_service(timeout_sec=2.0):
            self.get_logger().error("❌ DoorStatus 서비스 없음")
            return
            
        request = DoorStatus.Request()
        request.robot_id = 1
        
        self.get_logger().info("📞 문 상태 호출")
        future = client.call_async(request)
        
        def handle_response():
            rclpy.spin_until_future_complete(self, future)
            if future.result():
                response = future.result()
                door_str = "열림" if response.door_opened else "닫힘"
                self.get_logger().info(f"✅ 문 상태 응답: {door_str}")
            else:
                self.get_logger().error("❌ 문 상태 호출 실패")
        
        threading.Thread(target=handle_response, daemon=True).start()
    
    def test_space_availability(self):
        """공간 가용성 테스트"""
        client = self.service_clients['space_availability']
        if not client.wait_for_service(timeout_sec=2.0):
            self.get_logger().error("❌ SpaceAvailability 서비스 없음")
            return
            
        request = SpaceAvailability.Request()
        request.robot_id = 1
        
        self.get_logger().info("📞 공간 가용성 호출")
        future = client.call_async(request)
        
        def handle_response():
            rclpy.spin_until_future_complete(self, future)
            if future.result():
                response = future.result()
                space_str = "확보됨" if response.space_availability else "확보 안됨"
                self.get_logger().info(f"✅ 공간 가용성 응답: {space_str}")
            else:
                self.get_logger().error("❌ 공간 가용성 호출 실패")
        
        threading.Thread(target=handle_response, daemon=True).start()
    
    def test_location(self):
        """위치 감지 테스트"""
        client = self.service_clients['location']
        if not client.wait_for_service(timeout_sec=2.0):
            self.get_logger().error("❌ Location 서비스 없음")
            return
            
        request = Location.Request()
        request.robot_id = 1
        
        self.get_logger().info("📞 위치 감지 호출")
        future = client.call_async(request)
        
        def handle_response():
            rclpy.spin_until_future_complete(self, future)
            if future.result():
                response = future.result()
                location_names = {
                    0: "LOB_WAITING", 1: "LOB_CALL", 2: "RES_PICKUP", 3: "RES_CALL",
                    4: "SUP_PICKUP", 5: "ELE_1", 6: "ELE_2", 101: "ROOM_101",
                    102: "ROOM_102", 201: "ROOM_201", 202: "ROOM_202"
                }
                location_name = location_names.get(response.location_id, f"UNKNOWN({response.location_id})")
                self.get_logger().info(f"✅ 위치 감지 응답: {location_name}")
            else:
                self.get_logger().error("❌ 위치 감지 호출 실패")
        
        threading.Thread(target=handle_response, daemon=True).start()
    
    def test_all_services(self):
        """모든 서비스 순차 테스트"""
        self.get_logger().info("🎯 모든 VS 서비스 순차 테스트 시작!")
        
        def run_all_tests():
            tests = [
                ("VS 모드 - 대기모드", lambda: self.test_set_vs_mode(0)),
                ("VS 모드 - 등록모드", lambda: self.test_set_vs_mode(1)),
                ("VS 모드 - 추적모드", lambda: self.test_set_vs_mode(2)),
                ("VS 모드 - 엘리베이터모드", lambda: self.test_set_vs_mode(3)),
                ("VS 모드 - 배송 시뮬레이션", lambda: self.test_set_vs_mode(100)),
                ("VS 모드 - 호출 시뮬레이션", lambda: self.test_set_vs_mode(101)),
                ("VS 모드 - 길안내 시뮬레이션", lambda: self.test_set_vs_mode(102)),
                ("VS 모드 - 복귀 시뮬레이션", lambda: self.test_set_vs_mode(103)),
                ("VS 모드 - 엘리베이터 시뮬레이션", lambda: self.test_set_vs_mode(104)),
                ("엘리베이터 너비", self.test_elevator_width),
                ("버튼 상태", self.test_button_status),
                ("엘리베이터 상태", self.test_elevator_status),
                ("문 상태", self.test_door_status),
                ("공간 가용성", self.test_space_availability),
                ("위치 감지", self.test_location),
            ]
            
            for i, (test_name, test_func) in enumerate(tests):
                self.get_logger().info(f"🧪 [{i+1}/{len(tests)}] {test_name} 테스트")
                test_func()
                time.sleep(2)  # 2초 간격
            
            self.get_logger().info("🎉 모든 테스트 완료!")
        
        threading.Thread(target=run_all_tests, daemon=True).start()
    
    def show_menu(self):
        """사용 가능한 명령어 표시"""
        print("\n" + "="*70)
        print("�� VS 인터페이스 테스트 클라이언트 (완전판)")
        print("="*70)
        print("📋 rms_vs_interface.md 기준 전체 인터페이스:")
        print()
        print("🔍 상태 확인:")
        print("  check : 모든 서비스 가용성 확인")
        print("  info  : 현재 노드 및 토픽 상태 확인")
        print()
        print("🔧 서비스 인터페이스 테스트 (RC → VS):")
        print("  1  : SetVSMode - 대기모드 (mode_id=0)")
        print("  1r : SetVSMode - 등록모드 (mode_id=1)")
        print("  1t : SetVSMode - 추적모드 (mode_id=2)")
        print("  1e : SetVSMode - 엘리베이터모드 (mode_id=3)")
        print("  1s : SetVSMode - 배송 시뮬레이션 (mode_id=100)")
        print("  1c : SetVSMode - 호출 시뮬레이션 (mode_id=101)")
        print("  1g : SetVSMode - 길안내 시뮬레이션 (mode_id=102)")
        print("  1b : SetVSMode - 복귀 시뮬레이션 (mode_id=103)")
        print("  1v : SetVSMode - 엘리베이터 시뮬레이션 (mode_id=104)")
        print("  2  : ElevatorWidth - 엘리베이터 너비 감지")
        print("  3  : ButtonStatus - 버튼 상태 감지")
        print("  4  : ElevatorStatus - 엘리베이터 상태 감지")
        print("  5  : DoorStatus - 문 상태 감지")
        print("  6  : SpaceAvailability - 공간 가용성 감지")
        print("  7  : Location - 위치 감지")
        print()
        print("📡 토픽 인터페이스 테스트 (VS → RC):")
        print("  t1 : TrackingEvent 발행 요청")
        print("  t2 : Registered 이벤트 발행 요청")
        print("  ts : 추적 시뮬레이션 시퀀스 요청")
        print()
        print("🎯 통합 테스트:")
        print("  all    : 모든 서비스 순차 테스트")
        print("  topics : 모든 토픽 테스트")
        print("  full   : 서비스 + 토픽 전체 테스트")
        print()
        print("🛠️ 기타:")
        print("  menu   : 이 메뉴 다시 표시")
        print("  quit   : 종료")
        print("="*70)
        print("💡 실시간 모니터링: /vs/tracking_event, /vs/registered")
        print("💡 VS 노드 키보드 제어: R(추적시뮬레이션), T(추적이벤트), G(등록완료)")
        print("="*70)
        print("명령어를 입력하세요: ", end="")
    
    def check_node_info(self):
        """현재 노드 및 토픽 상태 확인"""
        self.get_logger().info("📊 VS 노드 상태 확인 중...")
        print("\n" + "="*70)
        print("📊 현재 ROS2 환경 상태")
        print("="*70)
        
        # 노드 정보는 직접 출력하기 어려우니 안내만
        print("🔍 수동 확인 명령어:")
        print("  ros2 node list                    # 실행 중인 노드 확인")
        print("  ros2 service list | grep vs       # VS 서비스 확인")  
        print("  ros2 topic list | grep vs         # VS 토픽 확인")
        print("  ros2 topic echo /vs/tracking_event  # 추적 이벤트 실시간 확인")
        print("  ros2 topic echo /vs/registered     # 등록 이벤트 실시간 확인")
        print("="*70)
        print("명령어를 입력하세요: ", end="")
    
    def request_tracking_event(self):
        """단일 추적 이벤트 발행 요청"""
        self.get_logger().info("📡 단일 추적 이벤트 발행 요청")
        self.get_logger().info("💡 VS 노드에서 'T' 키를 눌러서 추적 이벤트를 발행하세요")
        self.get_logger().info("   또는 다음 명령어를 사용하세요:")
        self.get_logger().info("   ros2 topic pub /vs/tracking_event roomie_msgs/msg/TrackingEvent ...")
    
    def request_registered_event(self):
        """등록 완료 이벤트 발행 요청"""
        self.get_logger().info("📡 등록 완료 이벤트 발행 요청")
        self.get_logger().info("💡 VS 노드에서 'G' 키를 눌러서 등록 완료 이벤트를 발행하세요")
        self.get_logger().info("   또는 다음 명령어를 사용하세요:")
        self.get_logger().info("   ros2 topic pub /vs/registered roomie_msgs/msg/Registered ...")
    
    def request_tracking_simulation(self):
        """추적 시뮬레이션 시퀀스 요청"""
        self.get_logger().info("🎬 추적 시뮬레이션 시퀀스 요청")
        
        # 먼저 등록 모드로 설정
        self.test_set_vs_mode(1)  # 등록 모드
        
        self.get_logger().info("💡 VS 노드에서 'R' 키를 눌러서 완전한 추적 시뮬레이션을 실행하세요")
        self.get_logger().info("   시뮬레이션 순서: 등록완료 → maintain → slow_down → maintain → lost → resume")
    
    def test_all_topics(self):
        """모든 토픽 테스트"""
        self.get_logger().info("📡 모든 토픽 인터페이스 테스트 시작!")
        
        def run_topic_tests():
            self.get_logger().info("🧪 [1/3] 등록 모드 설정 (토픽 발행 준비)")
            self.test_set_vs_mode(1)  # 등록 모드
            
            import time
            time.sleep(2)
            
            self.get_logger().info("🧪 [2/3] 단일 추적 이벤트 요청")
            self.request_tracking_event()
            
            time.sleep(2)
            
            self.get_logger().info("🧪 [3/3] 등록 완료 이벤트 요청")
            self.request_registered_event()
            
            self.get_logger().info("🎉 토픽 테스트 완료!")
            self.get_logger().info("💡 실제 토픽 발행은 VS 노드에서 키보드로 제어하세요")
        
        threading.Thread(target=run_topic_tests, daemon=True).start()
    
    def test_full_interface(self):
        """서비스 + 토픽 전체 인터페이스 테스트"""
        self.get_logger().info("🎯 VS 전체 인터페이스 테스트 시작!")
        
        def run_full_tests():
            # 1. 서비스 테스트
            self.get_logger().info("🧪 [1단계] 모든 서비스 테스트")
            self.test_all_services()
            
            import time
            time.sleep(3)
            
            # 2. 토픽 테스트
            self.get_logger().info("🧪 [2단계] 모든 토픽 테스트")  
            self.test_all_topics()
            
            time.sleep(2)
            
            self.get_logger().info("🎉 전체 인터페이스 테스트 완료!")
            self.get_logger().info("📋 인터페이스 요약:")
            self.get_logger().info("   ✅ 서비스 7개 타입: SetVSMode(9가지모드), ElevatorWidth, ButtonStatus, ElevatorStatus, DoorStatus, SpaceAvailability, Location")
            self.get_logger().info("   ✅ 토픽 2개: TrackingEvent, Registered")
            self.get_logger().info("   ✅ 총 테스트 케이스: 15개 서비스 + 2개 토픽 = 17개")
            self.get_logger().info("   📋 모드: 기본 4개(대기,등록,추적,엘리베이터) + 시뮬레이션 5개(배송,호출,길안내,복귀,엘리베이터)")
        
        threading.Thread(target=run_full_tests, daemon=True).start()
    
    def run_interactive(self):
        """대화형 모드 실행"""
        while True:
            try:
                cmd = input().strip()
                
                if cmd == "quit":
                    self.get_logger().info("👋 VS 테스트 클라이언트 종료")
                    break
                elif cmd == "menu":
                    self.show_menu()
                elif cmd == "check":
                    self.check_service_availability()
                elif cmd == "info":
                    self.check_node_info()
                elif cmd == "all":
                    self.test_all_services()
                elif cmd == "topics":
                    self.test_all_topics()
                elif cmd == "full":
                    self.test_full_interface()
                elif cmd == "t1":
                    self.request_tracking_event()
                elif cmd == "t2":
                    self.request_registered_event()
                elif cmd == "ts":
                    self.request_tracking_simulation()
                elif cmd == "1":
                    self.test_set_vs_mode(0)  # 대기모드
                elif cmd == "1r":
                    self.test_set_vs_mode(1)  # 등록모드
                elif cmd == "1t":
                    self.test_set_vs_mode(2)  # 추적모드
                elif cmd == "1e":
                    self.test_set_vs_mode(3)  # 엘리베이터모드
                elif cmd == "1s":
                    self.test_set_vs_mode(100) # 배송 시뮬레이션
                elif cmd == "1c":
                    self.test_set_vs_mode(101) # 호출 시뮬레이션
                elif cmd == "1g":
                    self.test_set_vs_mode(102) # 길안내 시뮬레이션
                elif cmd == "1b":
                    self.test_set_vs_mode(103) # 복귀 시뮬레이션
                elif cmd == "1v":
                    self.test_set_vs_mode(104) # 엘리베이터 시뮬레이션
                elif cmd == "2":
                    self.test_elevator_width()
                elif cmd == "3":
                    self.test_button_status()
                elif cmd == "4":
                    self.test_elevator_status()
                elif cmd == "5":
                    self.test_door_status()
                elif cmd == "6":
                    self.test_space_availability()
                elif cmd == "7":
                    self.test_location()
                else:
                    print(f"❌ 알 수 없는 명령어: {cmd}")
                    print("'menu'를 입력하면 사용 가능한 명령어를 볼 수 있습니다.")
                
                print("명령어를 입력하세요: ", end="")
                
            except KeyboardInterrupt:
                self.get_logger().info("👋 Ctrl+C로 종료")
                break
            except Exception as e:
                self.get_logger().error(f"❌ 오류: {e}")


def main():
    rclpy.init()
    
    try:
        client = VSInterfaceTestClient()
        
        # ROS2 스핀을 백그라운드에서 실행
        spin_thread = threading.Thread(target=lambda: rclpy.spin(client), daemon=True)
        spin_thread.start()
        
        # 대화형 모드 실행
        client.run_interactive()
        
    except Exception as e:
        print(f"❌ 오류: {e}")
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main() 