"""
CommonController - 공통 화면들 (TOUCH_SCREEN, COUNTDOWN 등)을 처리하는 컨트롤러
"""

from .base_controller import BaseController


class CommonController(BaseController):
    def __init__(self, widget, screen_manager, node, ui_filename):
        super().__init__(widget, screen_manager, node, ui_filename)
        self.setup_events()
    
    def setup_events(self):
        """이벤트 연결 설정"""
        if "TOUCH_SCREEN.ui" in self.ui_filename:
            self.setup_touch_screen_events()
        elif "COUNTDOWN.ui" in self.ui_filename:
            self.setup_countdown_events()
    
    def setup_touch_screen_events(self):
        """Touch Screen 이벤트 설정"""
        self.log_info("Touch Screen 이벤트 설정 중...")
        
        # 사용자 점유 상태 이벤트 발행 (사용자가 화면을 터치하면)
        success = self.setup_touch_event("touchButton", self.on_user_occupied)
        
        if success:
            self.log_info("Touch Screen 준비 완료")
        else:
            self.log_warn("Touch Screen touchButton을 찾을 수 없음")
    
    def setup_countdown_events(self):
        """카운트다운 화면 이벤트 설정"""
        self.log_info("카운트다운 화면 준비 완료")
        # 카운트다운은 외부 시스템에서 서비스 호출로 시작됨
        # UI에서 별도 버튼 이벤트는 없음
    
    def on_user_occupied(self):
        """사용자가 화면을 터치했을 때 - 점유 상태 알림"""
        self.log_info("👤 사용자가 화면을 터치했습니다")
        
        # 사용자 점유 상태 이벤트 발행 (rgui_event_id: 102)
        self.publish_event(event_id=102, detail="OCCUPIED") 