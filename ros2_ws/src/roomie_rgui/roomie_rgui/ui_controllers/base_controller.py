"""
BaseController - 모든 UI 컨트롤러의 공통 부모 클래스
"""

from PyQt6.QtWidgets import QPushButton, QLabel
import os


class BaseController:
    def __init__(self, widget, screen_manager, node, ui_filename):
        self.widget = widget
        self.screen_manager = screen_manager
        self.node = node
        self.ui_filename = os.path.basename(ui_filename)
        
        self.log_info(f"컨트롤러 초기화: {self.ui_filename}")
    
    # 🔧 위젯 찾기 헬퍼
    def find_widget(self, widget_name, widget_type=None):
        """UI에서 특정 위젯 찾기"""
        if widget_type:
            return self.widget.findChild(widget_type, widget_name)
        else:
            # 여러 타입 시도
            return (self.widget.findChild(QPushButton, widget_name) or 
                   self.widget.findChild(QLabel, widget_name))
    
    # 🖱️ 이벤트 연결 헬퍼들
    def setup_button_event(self, button_name, callback):
        """버튼 클릭 이벤트 연결"""
        button = self.find_widget(button_name, QPushButton)
        if button:
            button.clicked.connect(callback)
            self.log_info(f"버튼 이벤트 연결: {button_name}")
            return True
        else:
            self.log_warn(f"버튼을 찾을 수 없음: {button_name}")
            return False
    
    def setup_touch_event(self, area_name, callback):
        """터치 영역 이벤트 연결"""
        touch_area = self.find_widget(area_name, QPushButton)
        if touch_area:
            # 디버깅: 위젯 속성 확인
            self.log_info(f"터치 위젯 발견: {area_name}, 크기: {touch_area.size()}, 활성화: {touch_area.isEnabled()}")
            
            touch_area.clicked.connect(callback)
            
            # 디버깅: 테스트 클릭 이벤트도 연결
            touch_area.pressed.connect(lambda: self.log_info(f"🖱️ {area_name} 위젯이 눌렸습니다!"))
            touch_area.released.connect(lambda: self.log_info(f"🖱️ {area_name} 위젯이 릴리즈되었습니다!"))
            
            self.log_info(f"터치 이벤트 연결: {area_name}")
            return True
        else:
            self.log_warn(f"터치 영역을 찾을 수 없음: {area_name}")
            return False
    
    # 📡 ROS2 이벤트 발행
    def publish_event(self, event_id, detail=""):
        """ROS2 GUI 이벤트 발행"""
        self.node.publish_event(event_id, robot_id=98, detail=detail)
        self.log_info(f"이벤트 발행: ID={event_id}, detail={detail}")
    

    
    # 📝 로깅 헬퍼들
    def log_info(self, message):
        self.node.get_logger().info(f"[{self.__class__.__name__}] {message}")
    
    def log_warn(self, message):
        self.node.get_logger().warn(f"[{self.__class__.__name__}] {message}")
    
    def log_error(self, message):
        self.node.get_logger().error(f"[{self.__class__.__name__}] {message}")
    
    # 🎯 하위 클래스에서 구현해야 할 메서드
    def setup_events(self):
        """하위 클래스에서 구현: 이벤트 연결 로직"""
        pass 