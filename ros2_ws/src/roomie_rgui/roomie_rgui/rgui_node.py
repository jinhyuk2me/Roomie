import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from PyQt6.QtWidgets import QApplication
import threading
from roomie_msgs.msg import RobotGuiEvent
from roomie_msgs.srv import UnlockDoor
from roomie_msgs.action import StartCountdown, ReturnCountdown

from .screen_manager import ScreenManager
from .service_client import call_service
from .task_state import DeliveryState

class RobotGuiNode(Node):
    def __init__(self, app):
        super().__init__('robot_gui_node')
        self.app = app
        self.screen = ScreenManager(self)

        # Publisher
        self.event_pub = self.create_publisher(RobotGuiEvent, '/robot_gui/event', 10)
        
        # Subscriber
        self.event_sub = self.create_subscription(RobotGuiEvent, '/robot_gui/event', self.on_robot_event, 10)

        # Service Client
        self.unlock_door_cli = self.create_client(UnlockDoor, '/robot_gui/unlock_door')
        
        # Action Servers
        self.departure_action_srv = ActionServer(
            self, 
            StartCountdown, 
            '/robot_gui/action/start_countdown', 
            self.handle_start_departure_countdown
        )
        self.return_action_srv = ActionServer(
            self, 
            ReturnCountdown, 
            '/robot_gui/action/return_countdown', 
            self.handle_start_return_countdown
        )
        
        # 내부 카운트다운 관련 변수 (기존 호환성용)
        self.countdown_timer = None
        self.countdown_remaining = 0
        self.countdown_action_text = ""
        self.is_delivery_countdown = False

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

    def handle_start_departure_countdown(self, goal_handle):
        """출발 카운트다운 시작 요청 처리 (액션)"""
        goal = goal_handle.request
        self.get_logger().info(f"출발 카운트다운 액션 요청: robot_id={goal.robot_id}, task_id={goal.task_id}, task_type_id={goal.task_type_id}")
        
        # 카운트다운 화면으로 전환
        self.screen.show_screen("COUNTDOWN")
        
        # 현재 화면 상태에 따라 카운트다운 행동 텍스트 결정
        current_screen = self.screen.get_current_screen_name()
        if goal.task_type_id in [0, 1]:  # 배송 작업
            if current_screen in ["TOUCH_SCREEN", "COUNTDOWN", None]:
                action_text = "픽업장소로 이동"
            elif current_screen in ["PICKUP_DRAWER_CONTROL", "CHECKING_ORDER", "PICKUP_ARRIVED"]:
                action_text = "배송지로 이동"
            else:
                action_text = "픽업장소로 이동"  # 기본값
        elif goal.task_type_id == 2:  # 호출
            action_text = "호출장소로 이동"
        elif goal.task_type_id == 3:  # 길안내
            action_text = "길안내 시작"
        else:
            action_text = "이동"
        
        self.get_logger().info(f"⏰ 카운트다운 시작: 5초 ({action_text})")
        
        # 액션에서 직접 카운트다운 처리 (5초)
        import time
        from roomie_msgs.action import StartCountdown
        
        for remaining in range(5, 0, -1):
            # 화면 업데이트
            self.update_countdown_display_direct(remaining, action_text)
            
            # 피드백 발송
            feedback = StartCountdown.Feedback()
            feedback.remaining_time = remaining
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f"📤 액션 피드백 발송: remaining_time={remaining}")
            
            # 1초 대기
            time.sleep(1.0)
        
        # 카운트다운 완료
        self.get_logger().info("🎉 카운트다운 완료!")
        
        # 화면 전환
        self.handle_countdown_completed_direct(goal.task_type_id)
        
        # 결과 반환
        result = StartCountdown.Result()
        result.robot_id = goal.robot_id
        result.success = True
        
        goal_handle.succeed()
        self.get_logger().info(f"📤 액션 완료: success=True, robot_id={result.robot_id}")
        
        return result
    
    def update_countdown_display_direct(self, remaining_time, action_text):
        """카운트다운 화면 직접 업데이트"""
        try:
            countdown_widget = self.screen.screen_widgets.get("COUNTDOWN")
            if not countdown_widget:
                self.get_logger().warn("COUNTDOWN 화면 위젯을 찾을 수 없음")
                return
            
            from PyQt6.QtWidgets import QLabel
            
            # countdownNumber 라벨 업데이트
            countdown_label = countdown_widget.findChild(QLabel, "countdownNumber")
            if countdown_label:
                countdown_label.setText(str(remaining_time))
                
            # countdownTitle 라벨 업데이트
            title_label = countdown_widget.findChild(QLabel, "countdownTitle")
            if title_label:
                title_label.setText(f"{remaining_time}초후에 {action_text}합니다.")
                
        except Exception as e:
            self.get_logger().error(f"카운트다운 화면 업데이트 실패: {e}")
    
    def handle_countdown_completed_direct(self, task_type_id):
        """카운트다운 완료 후 화면 전환 처리"""
        if task_type_id in [0, 1]:  # 배송 작업
            self.get_logger().info("🚚 픽업 출발 카운트다운 완료 - 픽업장소 이동중 화면으로 전환")
            self.screen.show_screen("PICKUP_MOVING")
        elif task_type_id == 2:  # 호출
            self.get_logger().info("📞 호출 작업 카운트다운 완료")
            self.screen.show_screen("TOUCH_SCREEN")
        elif task_type_id == 3:  # 길안내
            self.get_logger().info("🗺️ 길안내 작업 카운트다운 완료")
            self.screen.show_screen("TOUCH_SCREEN")
        else:
            self.get_logger().warn(f"알 수 없는 task_type_id: {task_type_id}")
            self.screen.show_screen("TOUCH_SCREEN")
    
    def start_delivery_countdown(self):
        """배송 출발 카운트다운 시작 (내부 호출용)"""
        # 배송 출발 카운트다운 플래그 설정
        self.is_delivery_countdown = True
        

        
        # 카운트다운 데이터 먼저 설정 (화면 전환 전에)
        self.countdown_remaining = 5
        self.countdown_action_text = "배송지로 출발"
        
        # 카운트다운 화면으로 전환
        self.screen.show_screen("COUNTDOWN")
        
        # 화면 전환 직후 바로 텍스트 업데이트
        self.update_countdown_text()
        
        # 카운트다운 타이머 시작
        self.start_countdown_timer()
        
        self.get_logger().info("🚛 배송 출발 카운트다운 시작 (5초)")
    
    def update_countdown_text(self):
        """카운트다운 화면의 텍스트 업데이트"""
        try:
            # 현재 COUNTDOWN 화면의 위젯 가져오기
            countdown_widget = self.screen.screen_widgets.get("COUNTDOWN")
            if not countdown_widget:
                self.get_logger().warn("COUNTDOWN 화면 위젯을 찾을 수 없음")
                return
            
            from PyQt6.QtWidgets import QLabel
            
            # countdownTitle 라벨 업데이트 (완전한 텍스트로)
            title_label = countdown_widget.findChild(QLabel, "countdownTitle")
            if title_label:
                title_text = f"{self.countdown_remaining}초후에 {self.countdown_action_text}합니다."
                title_label.setText(title_text)
                self.get_logger().info(f"📝 카운트다운 countdownTitle 업데이트: {title_text}")
            else:
                self.get_logger().warn("countdownTitle 라벨을 찾을 수 없음")
            
            # countdownNumber 라벨 업데이트
            countdown_label = countdown_widget.findChild(QLabel, "countdownNumber")
            if countdown_label:
                countdown_label.setText(str(self.countdown_remaining))
                self.get_logger().info(f"📝 카운트다운 countdownNumber 업데이트: {self.countdown_remaining}")
            else:
                self.get_logger().warn("countdownNumber 라벨을 찾을 수 없음")
                
        except Exception as e:
            self.get_logger().error(f"카운트다운 텍스트 업데이트 실패: {e}")

    def start_countdown_timer(self):
        """카운트다운 타이머 시작"""
        if self.countdown_remaining > 0:
            # 1초 후에 on_countdown_tick 호출
            self.countdown_timer = threading.Timer(1.0, self.on_countdown_tick)
            self.countdown_timer.start()
    
    def on_countdown_tick(self):
        """카운트다운 타이머 틱 (1초마다 호출) - 내부 카운트다운용"""
        self.countdown_remaining -= 1
        self.get_logger().info(f"⏰ 내부 카운트다운: {self.countdown_remaining}초 남음")
        
        if self.countdown_remaining > 0:
            # 남은 시간 표시 업데이트
            self.update_countdown_display()
            # 다음 타이머 시작
            self.start_countdown_timer()
        else:
            # 카운트다운 완료
            self.get_logger().info("🎉 내부 카운트다운 완료!")
            
            # 내부 카운트다운 완료 후 화면 전환
            self.handle_internal_countdown_completed()
            
    def update_countdown_display(self):
        """카운트다운 화면의 시간 표시 업데이트"""
        try:
            # 현재 COUNTDOWN 화면의 위젯 가져오기
            countdown_widget = self.screen.screen_widgets.get("COUNTDOWN")
            if not countdown_widget:
                self.get_logger().warn("COUNTDOWN 화면 위젯을 찾을 수 없음")
                return
            
            # countdownNumber 라벨 찾기
            from PyQt6.QtWidgets import QLabel
            countdown_label = countdown_widget.findChild(QLabel, "countdownNumber")
            if countdown_label:
                # 숫자 업데이트
                countdown_label.setText(str(self.countdown_remaining))
                self.get_logger().debug(f"🔢 카운트다운 화면 업데이트: {self.countdown_remaining}")
            else:
                self.get_logger().warn("countdownNumber 라벨을 찾을 수 없음")
                
            # countdownTitle 라벨도 업데이트 (상황에 맞는 텍스트)
            title_label = countdown_widget.findChild(QLabel, "countdownTitle")
            if title_label:
                title_label.setText(f"{self.countdown_remaining}초후에 {self.countdown_action_text}합니다.")
                
        except Exception as e:
            self.get_logger().error(f"카운트다운 화면 업데이트 실패: {e}")
    
    def handle_internal_countdown_completed(self):
        """내부 카운트다운 완료 후 처리 (start_delivery_countdown용)"""
        if self.is_delivery_countdown:
            # 배송 출발 카운트다운 완료
            self.get_logger().info("🚛 배송 출발 카운트다운 완료 - 배송장소 이동중 화면으로 전환")
            self.screen.show_screen("DELIVERY_MOVING")
            # 플래그 초기화
            self.is_delivery_countdown = False
        else:
            self.get_logger().info("내부 카운트다운 완료 - 기본 화면으로 전환")
            self.screen.show_screen("TOUCH_SCREEN")
        
        # 변수 초기화
        self.countdown_action_text = ""
        self.get_logger().info("📤 내부 카운트다운 완료 처리: success=True")
    
    def handle_start_return_countdown(self, goal_handle):
        """복귀 카운트다운 시작 요청 처리 (액션)"""
        goal = goal_handle.request
        self.get_logger().info(f"🏠 복귀 카운트다운 액션 요청: robot_id={goal.robot_id}")
        
        # 카운트다운 화면으로 전환
        self.screen.show_screen("COUNTDOWN")
        
        action_text = "대기장소로 복귀"
        self.get_logger().info(f"⏰ 복귀 카운트다운 시작: 10초 ({action_text})")
        
        # 액션에서 직접 카운트다운 처리 (10초)
        import time
        from roomie_msgs.action import ReturnCountdown
        
        for remaining in range(10, 0, -1):
            # 화면 업데이트
            self.update_countdown_display_direct(remaining, action_text)
            
            # 피드백 발송
            feedback = ReturnCountdown.Feedback()
            feedback.remaining_time = remaining
            goal_handle.publish_feedback(feedback)
            self.get_logger().info(f"📤 복귀 액션 피드백 발송: remaining_time={remaining}")
            
            # 1초 대기
            time.sleep(1.0)
        
        # 카운트다운 완료
        self.get_logger().info("🎉 복귀 카운트다운 완료!")
        
        # 화면 전환
        self.get_logger().info("🏠 복귀 카운트다운 완료 - 대기장소 복귀 화면으로 전환")
        self.screen.show_screen("RETURN_TO_BASE")
        
        # 결과 반환
        result = ReturnCountdown.Result()
        result.robot_id = goal.robot_id
        result.success = True
        
        goal_handle.succeed()
        self.get_logger().info(f"📤 복귀 액션 완료: success=True, robot_id={result.robot_id}")
        
        return result

    def on_robot_event(self, msg):
        """RC로부터 받은 이벤트 처리"""
        event_id = msg.rgui_event_id
        self.get_logger().info(f"🔔 이벤트 수신: ID={event_id}, robot_id={msg.robot_id}, detail={msg.detail}")
        
        # 이벤트 ID에 따른 화면 전환 (순서대로)
        if event_id == 12:  # 픽업장소 이동 시작
            self.screen.show_screen("PICKUP_MOVING")
        elif event_id == 13:  # 픽업장소 이동 종료
            # 주문 내역이 detail에 있으면 파싱해서 화면에 전달
            import json
            items = []
            room_number = "202"  # 기본값
            if msg.detail:
                try:
                    data = json.loads(msg.detail)
                    items = data.get("items", [])
                    room_number = data.get("room_number", "202")
                except Exception as e:
                    self.get_logger().warn(f"주문 내역 detail 파싱 실패: {e}")
            self.screen.show_screen("PICKUP_ARRIVED")
            if items:
                # 주문 내역을 화면에 표시
                delivery_controller = self.screen.get_screen_controller("CHECKING_ORDER")
                if delivery_controller and hasattr(delivery_controller, 'show_pickup_order'):
                    delivery_controller.show_pickup_order(items, room_number)
                else:
                    self.get_logger().info(f"주문 내역: {items}, 호실: {room_number}호")
        elif event_id == 14:  # 배송장소 이동 시작
            self.screen.show_screen("DELIVERY_MOVING")
        elif event_id == 15:  # 배송장소 도착 완료
            self.screen.show_screen("DELIVERY_ARRIVED")
        elif event_id == 16:  # 서랍 열림
            # 현재 화면에 따라 다음 화면으로
            current = self.screen.get_current_screen_name()
            if current == "PICKUP_ARRIVED":
                self.screen.show_screen("CHECKING_ORDER")
            elif current == "CHECKING_ORDER":
                self.screen.show_screen("PICKUP_DRAWER_CONTROL")
            elif current == "DELIVERY_ARRIVED":
                self.screen.show_screen("DELIVERY_DRAWER_CONTROL")
            elif current == "PICKUP_DRAWER_CONTROL":
                # 픽업 서랍 조작 화면에서 서랍이 열렸을 때 적재완료 버튼 활성화
                self.screen.notify_drawer_opened(msg.detail)
            elif current == "DELIVERY_DRAWER_CONTROL":
                # 배송 서랍 조작 화면에서 서랍이 열렸을 때 수령완료 버튼 활성화
                self.screen.notify_drawer_opened(msg.detail)
        elif event_id == 24:  # 배송 수령 완료
            self.screen.show_screen("THANK_YOU")
        elif event_id == 25:  # 배송 수령 미완료
            # 감사 화면 후 초기 화면으로
            self.screen.show_screen("TOUCH_SCREEN")
        elif event_id == 104:  # 서랍 열기 버튼 클릭
            self.get_logger().info("🔓 서랍 열기 버튼 클릭됨 - 서랍 열림 이벤트 발행")
            # 서랍 열림을 알리는 이벤트 발행 (event_id=16)
            event_msg = RobotGuiEvent()
            event_msg.robot_id = 98  # 기본 로봇 ID
            event_msg.rgui_event_id = 16
            event_msg.detail = "drawer_opened"
            self.event_pub.publish(event_msg)
        elif event_id == 105:  # 적재 완료 버튼 클릭
            self.get_logger().info("📦 적재 완료 버튼 클릭됨 - 배송 출발 카운트다운 시작")
            # 배송 출발 카운트다운 시작
            self.start_delivery_countdown()
        elif event_id == 106:  # 배송 서랍 열기 버튼 클릭
            self.get_logger().info("🔓 배송 서랍 열기 버튼 클릭됨 - 서랍 열림 이벤트 발행")
            # 서랍 열림을 알리는 이벤트 발행 (event_id=16)
            event_msg = RobotGuiEvent()
            event_msg.robot_id = 98  # 기본 로봇 ID
            event_msg.rgui_event_id = 16
            event_msg.detail = "delivery_drawer_opened"
            self.event_pub.publish(event_msg)
            
            # 수령완료 버튼 활성화 (UI 업데이트 필요시)
            # TODO: 필요한 경우 UI 컨트롤러에 신호 전송
        elif event_id == 100:  # 수령 완료 버튼 클릭
            self.get_logger().info("✅ 수령 완료 버튼 클릭됨 - 감사 화면으로 전환")
            # 감사 화면으로 전환
            self.screen.show_screen("THANK_YOU")
        elif event_id == 19:  # 충전 시작
            self.get_logger().info("🔋 충전 시작 이벤트 수신 - 충전 화면으로 전환")
            # 복귀중 화면에서 충전중 화면으로 전환
            self.screen.show_screen("CHARGING")
        elif event_id == 20:  # 충전 종료
            self.get_logger().info("🔋 충전 완료 이벤트 수신 - 초기 화면으로 전환")
            # 충전 완료 후 초기 화면으로 전환
            self.screen.show_screen("TOUCH_SCREEN")
        else:
            self.get_logger().warn(f"처리되지 않은 이벤트 ID: {event_id}")

    def request_unlock_door(self, robot_id: int, task_id: int):
        """도어 잠금 해제 요청"""
        req = UnlockDoor.Request()
        req.robot_id = robot_id
        req.task_id = task_id
        call_service(self, self.unlock_door_cli, req)


def main():
    rclpy.init()
    app = QApplication(sys.argv)
    node = RobotGuiNode(app)
    
    # ROS2 스핀을 백그라운드에서 실행
    import threading
    def spin_ros():
        rclpy.spin(node)
    
    ros_thread = threading.Thread(target=spin_ros, daemon=True)
    ros_thread.start()
    
    # GUI 메인루프 실행
    try:
        sys.exit(app.exec())
    finally:
        rclpy.shutdown()
