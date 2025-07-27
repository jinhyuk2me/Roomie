#!/usr/bin/env python3
"""
Robot GUI 테스트 클라이언트
외부 시스템(RC)을 시뮬레이션하여 Robot GUI와 ROS2 통신으로 상호작용
"""

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
import threading
import time
from roomie_msgs.msg import RobotGuiEvent
from roomie_msgs.action import StartCountdown, ReturnCountdown


class TestServiceClient(Node):
    def __init__(self):
        super().__init__('test_service_client')
        
        # Publisher - Robot GUI로 이벤트 발행
        self.event_pub = self.create_publisher(RobotGuiEvent, '/robot_gui/event', 10)
        
        # Action Clients
        self.departure_cli = ActionClient(self, StartCountdown, '/robot_gui/action/start_countdown')
        self.return_cli = ActionClient(self, ReturnCountdown, '/robot_gui/action/return_countdown')
        
        self.get_logger().info("🧪 Robot GUI 테스트 클라이언트 시작")
        self.show_menu()
    
    def publish_event(self, event_id: int, robot_id: int = 98, task_id: int = 1, detail: str = ""):
        """Robot GUI로 이벤트 발행"""
        from builtin_interfaces.msg import Time
        from rclpy.clock import Clock
        
        msg = RobotGuiEvent()
        msg.robot_id = robot_id
        msg.task_id = task_id
        msg.rgui_event_id = event_id
        msg.detail = detail
        msg.timestamp = Clock().now().to_msg()
        
        self.event_pub.publish(msg)
        self.get_logger().info(f"📤 이벤트 발행: ID={event_id}, detail='{detail}'")
    
    def call_departure_countdown(self):
        """출발 카운트다운 액션 호출"""
        if not self.departure_cli.wait_for_server(timeout_sec=2.0):
            self.get_logger().error("❌ 출발 카운트다운 액션 서버를 찾을 수 없습니다")
            return
        
        goal = StartCountdown.Goal()
        goal.robot_id = 98
        goal.task_id = 1
        goal.task_type_id = 0  # 음식배송
        
        self.get_logger().info("📞 카운트다운 액션 호출 중...")
        
        def feedback_callback(feedback):
            self.get_logger().info(f"⏰ 액션 피드백: 남은 시간 {feedback.feedback.remaining_time}초")
        
        def done_callback(future):
            result = future.result().result
            self.get_logger().info(f"✅ 카운트다운 완료: success={result.success}, robot_id={result.robot_id}")
        
        send_goal_future = self.departure_cli.send_goal_async(goal, feedback_callback=feedback_callback)
        send_goal_future.add_done_callback(lambda future: future.result().get_result_async().add_done_callback(done_callback))
    
    def call_return_countdown(self):
        """복귀 카운트다운 액션 호출"""
        if not self.return_cli.wait_for_server(timeout_sec=2.0):
            self.get_logger().error("❌ 복귀 카운트다운 액션 서버를 찾을 수 없습니다")
            return
        
        goal = ReturnCountdown.Goal()
        goal.robot_id = 98
        
        self.get_logger().info("📞 복귀 카운트다운 액션 호출 중...")
        
        def feedback_callback(feedback):
            self.get_logger().info(f"⏰ 액션 피드백: 남은 시간 {feedback.feedback.remaining_time}초")
        
        def done_callback(future):
            result = future.result().result
            self.get_logger().info(f"✅ 복귀 카운트다운 완료: success={result.success}, robot_id={result.robot_id}")
        
        send_goal_future = self.return_cli.send_goal_async(goal, feedback_callback=feedback_callback)
        send_goal_future.add_done_callback(lambda future: future.result().get_result_async().add_done_callback(done_callback))
    
    def show_menu(self):
        """사용 가능한 명령어 표시"""
        print("\n" + "="*60)
        print("🧪 Robot GUI 테스트 클라이언트")
        print("="*60)
        print("📋 사용 가능한 명령어:")
        print()
        print("🔧 액션 호출:")
        print("  1  : 출발 카운트다운 액션 호출")
        print("  2  : 복귀 카운트다운 액션 호출")
        print()
        print("📡 이벤트 발행 (RC → Robot GUI):")
        print("  12 : 픽업장소 이동 시작")
        print("  13 : 픽업장소 이동 종료 (도착)")
        print("  14 : 배송장소 이동 시작") 
        print("  15 : 배송장소 도착 완료")
        print("  16 : 서랍 열림")
        print("  19 : 충전 시작")
        print("  20 : 충전 종료")
        print("  24 : 배송 수령 완료")
        print("  25 : 배송 수령 미완료")
        print()
        print("🎯 시나리오 자동 실행:")
        print("  auto : 전체 배송 시나리오 자동 실행")
        print("  menu : 이 메뉴 다시 표시")
        print("  quit : 종료")
        print("="*60)
        print("명령어를 입력하세요: ", end="")
    
    def run_auto_scenario(self):
        """전체 배송 시나리오 자동 실행"""
        self.get_logger().info("🎬 자동 시나리오 시작!")
        
        scenarios = [
            (12, "픽업장소 이동 시작", ""),
            (13, "픽업장소 이동 종료", ""),
            (16, "서랍 열림 (주문 확인)", ""),
            (16, "서랍 열림 (픽업 서랍)", ""),
            (14, "배송장소 이동 시작", ""),
            (15, "배송장소 도착 완료", ""),
            (16, "서랍 열림 (배송)", ""),
            (24, "배송 수령 완료", ""),
        ]
        
        def auto_runner():
            for i, (event_id, desc, detail) in enumerate(scenarios):
                time.sleep(3)  # 3초 간격
                self.get_logger().info(f"🎬 [{i+1}/{len(scenarios)}] {desc}")
                self.publish_event(event_id, detail=detail)
            
            self.get_logger().info("🎉 자동 시나리오 완료!")
        
        threading.Thread(target=auto_runner, daemon=True).start()
    
    def run_interactive(self):
        """대화형 모드 실행"""
        while True:
            try:
                cmd = input().strip()
                
                if cmd == "quit":
                    self.get_logger().info("👋 테스트 클라이언트 종료")
                    break
                elif cmd == "menu":
                    self.show_menu()
                elif cmd == "auto":
                    self.run_auto_scenario()
                elif cmd == "1":
                    self.call_departure_countdown()
                elif cmd == "2":
                    self.call_return_countdown()
                elif cmd in ["12", "13", "14", "15", "16", "19", "20", "24", "25"]:
                    event_id = int(cmd)
                    # 13번(픽업장소 이동 종료) 이벤트는 주문 내역 detail 포함
                    if event_id == 13:
                        import json
                        import random
                        
                        # 랜덤 메뉴 목록
                        menu_list = [
                            "스파게티", "피자", "햄버거", "치킨", "샐러드", 
                            "파스타", "스테이크", "초밥", "라면", "김치찌개",
                            "된장찌개", "비빔밥", "불고기", "갈비찜", "삼겹살"
                        ]
                        
                        # 랜덤으로 1~4개 메뉴 선택
                        num_items = random.randint(1, 4)
                        random_items = []
                        
                        for _ in range(num_items):
                            menu_name = random.choice(menu_list)
                            quantity = random.randint(1, 3)  # 1~3개
                            random_items.append({
                                "name": menu_name,
                                "quantity": quantity
                            })
                        
                        detail = json.dumps({
                            "room_number": str(random.randint(101, 999)),  # 101~999호 랜덤
                            "items": random_items
                        }, ensure_ascii=False)
                        
                        self.get_logger().info(f"🎲 랜덤 주문 내역 생성: {len(random_items)}개 메뉴")
                        room_num = json.loads(detail)["room_number"]
                        self.get_logger().info(f"   🏠 호실: {room_num}호")
                        for item in random_items:
                            self.get_logger().info(f"   - {item['name']} {item['quantity']}개")
                        
                        self.publish_event(event_id, detail=detail)
                    else:
                        self.publish_event(event_id)
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
        client = TestServiceClient()
        
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