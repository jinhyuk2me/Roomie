"""
DeliveryController - 배송 관련 화면들 (DELI_1~8)을 처리하는 컨트롤러
화면 전환은 외부 시스템에서 처리하고, 여기서는 사용자 입력에 대한 이벤트 발행만 수행
"""

from .base_controller import BaseController


class DeliveryController(BaseController):
    def __init__(self, widget, screen_manager, node, ui_filename):
        super().__init__(widget, screen_manager, node, ui_filename)
        # 화면별 이벤트는 화면이 활성화될 때만 설정
    
    def on_screen_activated(self):
        """화면이 활성화될 때 호출됨 (ScreenManager에서)"""
        self.setup_events()
    
    def setup_events(self):
        """현재 활성화된 화면의 이벤트만 설정"""
        if "DELI_1" in self.ui_filename:
            self.setup_pickup_moving_events()
        elif "DELI_2" in self.ui_filename:
            self.setup_pickup_arrival_events()
        elif "DELI_3" in self.ui_filename:
            self.setup_order_confirm_events()
        elif "DELI_4" in self.ui_filename:
            self.setup_pickup_drawer_events()
        elif "DELI_5" in self.ui_filename:
            self.setup_delivery_moving_events()
        elif "DELI_6" in self.ui_filename:
            self.setup_delivery_arrival_events()
        elif "DELI_7" in self.ui_filename:
            self.setup_delivery_drawer_events()
        elif "DELI_8" in self.ui_filename:
            self.setup_thank_you_events()
    
    # 🚚 DELI_1: 픽업 이동중
    def setup_pickup_moving_events(self):
        """픽업 장소로 이동중 화면"""
        self.log_info("픽업 이동중 화면 - 외부 시스템 대기")
        # 이 화면에서는 사용자 입력 없음, 외부 시스템에서 화면 전환
    
    # 📍 DELI_2: 픽업 도착
    def setup_pickup_arrival_events(self):
        """픽업 장소 도착 화면"""
        self.log_info("픽업 도착 화면 - 외부 시스템 대기")
        # 이 화면에서는 사용자 입력 없음, 외부 시스템에서 화면 전환
    
    # 📋 DELI_3: 주문 확인
    def setup_order_confirm_events(self):
        """주문 확인 화면"""
        self.log_info("주문 확인 화면 준비")
        # 주문 확인 후 자동으로 다음 화면으로 (외부 시스템에서 처리)
    
    # 🔧 DELI_4: 픽업 서랍 조작
    def setup_pickup_drawer_events(self):
        """픽업 서랍 조작 화면"""
        self.log_info("픽업 서랍 조작 화면 준비")
        
        # [서랍 열기] 버튼
        self.setup_button_event("openDrawerButton", self.on_request_drawer_open)
        # [적재 완료] 버튼  
        self.setup_button_event("loadingCompleteButton", self.on_loading_complete)
    
    def on_request_drawer_open(self):
        """[서랍 열기] 버튼 클릭 시"""
        self.log_info("🔓 [서랍 열기] 버튼이 클릭되었습니다")
        
        # 서랍 열기 클릭 이벤트 발행 (rgui_event_id: 104)
        self.publish_event(event_id=104, detail="")
    
    def on_loading_complete(self):
        """[적재 완료] 버튼 클릭 시"""
        self.log_info("📦 [적재 완료] 버튼이 클릭되었습니다")
        
        # 적재 완료 클릭 이벤트 발행 (rgui_event_id: 105)
        self.publish_event(event_id=105, detail="")
    
    # 🚛 DELI_5: 배송 이동중
    def setup_delivery_moving_events(self):
        """배송지로 이동중 화면"""
        self.log_info("배송 이동중 화면 - 외부 시스템 대기")
        # 이 화면에서는 사용자 입력 없음, 외부 시스템에서 화면 전환
    
    # 🏠 DELI_6: 배송지 도착
    def setup_delivery_arrival_events(self):
        """배송지 도착 화면"""
        self.log_info("배송지 도착 화면 - 외부 시스템 대기")
        # 이 화면에서는 사용자 입력 없음, 외부 시스템에서 화면 전환
    
    # 📦 DELI_7: 배송 서랍 조작
    def setup_delivery_drawer_events(self):
        """배송 서랍 조작 화면"""
        self.log_info("배송 서랍 조작 화면 준비")
        
        # [수령 완료] 버튼
        self.setup_button_event("pickupCompleteButton", self.on_pickup_complete)
    
    def on_pickup_complete(self):
        """[수령 완료] 버튼 클릭 시"""
        self.log_info("✅ [수령 완료] 버튼이 클릭되었습니다")
        
        # 수령 완료 클릭 이벤트 발행 (rgui_event_id: 100)
        self.publish_event(event_id=100, detail="")
    
    # 🎉 DELI_8: 감사 인사
    def setup_thank_you_events(self):
        """감사 인사 화면"""
        self.log_info("감사 인사 화면 - 외부 시스템 대기")
        # 이 화면에서는 사용자 입력 없음, 일정 시간 후 외부 시스템에서 화면 전환 