# screen_manager.py

from PyQt6.QtWidgets import QStackedWidget
from .ui_loader import load_ui

# 컨트롤러 import
from .ui_controllers import BaseController, CommonController, DeliveryController


class ScreenManager(QStackedWidget):
    def __init__(self, node):
        super().__init__()
        self.node = node
        self.setWindowTitle("Roomie RGUI")
        
        # 스타일 설정
        self.setStyleSheet("""
            QStackedWidget {
                background-color: #3a4a5c;
            }
            QWidget {
                background-color: #3a4a5c;
            }
        """)

        # 현재 화면 정보
        self.current_screen_name = None
        
        # 화면별 위젯과 컨트롤러 저장
        self.screen_widgets = {}
        self.screen_controllers = {}
        self.screen_indices = {}

        # UI 경로 매핑
        self.ui_paths = {
            # 공통 화면
            "TOUCH_SCREEN": "ui/common/TOUCH_SCREEN.ui",
            "COUNTDOWN": "ui/countdown/COUNTDOWN.ui",
            
            # 배송 화면들
            "PICKUP_MOVING": "ui/delivery/DELI_1_PICKUP_MOVING.ui",
            "PICKUP_ARRIVED": "ui/delivery/DELI_2_PICKUP_ARRIVAL.ui", 
            "CHECKING_ORDER": "ui/delivery/DELI_3_CHECKING_ORDER.ui",
            "PICKUP_DRAWER_CONTROL": "ui/delivery/DELI_4_PICKUP_DRAWER_CONTROL.ui",
            "DELIVERY_MOVING": "ui/delivery/DELI_5_DELIVERY_MOVING.ui",
            "DELIVERY_ARRIVED": "ui/delivery/DELI_6_DELIVERY_ARRIVAL.ui",
            "DELIVERY_DRAWER_CONTROL": "ui/delivery/DELI_7_DELIVERY_DRAWER_CONTROL.ui",
            "THANK_YOU": "ui/delivery/DELI_8_THANK_YOU.ui",
        }

        # 컨트롤러 팩토리 매핑
        self.controller_map = {
            "TOUCH_SCREEN": CommonController,
            "COUNTDOWN": CommonController,
            "PICKUP_MOVING": DeliveryController,
            "PICKUP_ARRIVED": DeliveryController,
            "CHECKING_ORDER": DeliveryController,
            "PICKUP_DRAWER_CONTROL": DeliveryController,
            "DELIVERY_MOVING": DeliveryController,
            "DELIVERY_ARRIVED": DeliveryController,
            "DELIVERY_DRAWER_CONTROL": DeliveryController,
            "THANK_YOU": DeliveryController,
        }



        # 모든 화면 미리 로드
        self.preload_all_screens()
        
        # 초기 화면 표시
        self.show_screen("TOUCH_SCREEN")
        self.show()

    def preload_all_screens(self):
        """모든 화면을 미리 로드하고 스택에 추가"""
        self.node.get_logger().info("모든 화면을 미리 로드 중...")
        
        for screen_name, ui_path in self.ui_paths.items():
            widget = self.create_screen_widget(screen_name, ui_path)
            if widget:
                index = self.addWidget(widget)
                self.screen_widgets[screen_name] = widget
                self.screen_indices[screen_name] = index
                self.node.get_logger().info(f"{screen_name} 로드 완료 (index: {index})")
        
        self.node.get_logger().info(f"총 {len(self.screen_widgets)}개 화면 로드 완료!")

    def create_screen_widget(self, screen_name, ui_path):
        """개별 화면 위젯 생성"""
        try:
            from PyQt6.QtWidgets import QWidget
            widget = QWidget()
            
            # UI 로드
            load_ui(widget, ui_path)
            
            # 컨트롤러 생성
            controller_class = self.controller_map.get(screen_name)
            if controller_class:
                controller = controller_class(
                    widget=widget,
                    screen_manager=self,
                    node=self.node,
                    ui_filename=ui_path
                )
                self.screen_controllers[screen_name] = controller
                self.node.get_logger().info(f"컨트롤러 생성: {controller_class.__name__} for {screen_name}")
            
            return widget
            
        except Exception as e:
            self.node.get_logger().error(f"화면 생성 실패 {screen_name}: {e}")
            return None

    def show_screen(self, screen_name):
        """지정된 화면으로 전환"""
        if screen_name not in self.screen_indices:
            self.node.get_logger().warn(f"존재하지 않는 화면: {screen_name}")
            return False
        
        index = self.screen_indices[screen_name]
        self.setCurrentIndex(index)
        self.current_screen_name = screen_name
        self.node.get_logger().info(f"📺 화면 전환: {screen_name} (index: {index})")
        
        # 화면 전환 시 해당 컨트롤러의 이벤트 활성화
        controller = self.screen_controllers.get(screen_name)
        if controller and hasattr(controller, 'on_screen_activated'):
            controller.on_screen_activated()
            self.node.get_logger().info(f"🎯 {screen_name} 컨트롤러 이벤트 활성화")
        
        return True

    def get_current_screen_name(self):
        """현재 표시 중인 화면 이름 반환"""
        return self.current_screen_name

    def get_screen_controller(self, screen_name):
        """특정 화면의 컨트롤러 반환"""
        return self.screen_controllers.get(screen_name)
