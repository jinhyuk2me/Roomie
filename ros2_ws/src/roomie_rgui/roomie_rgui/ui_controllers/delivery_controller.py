"""
DeliveryController - 배송 관련 화면들 (DELI_1~8)을 처리하는 컨트롤러
화면 전환은 외부 시스템에서 처리하고, 여기서는 사용자 입력에 대한 이벤트 발행만 수행
"""

from PyQt6.QtWidgets import QPushButton
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
        self.log_info("픽업 도착 화면 - 터치 대기")
        
        # 전체 화면 터치 이벤트 연결
        self.setup_touch_event("fullScreenTouchArea", self.on_pickup_arrival_touch)
    
    def on_pickup_arrival_touch(self):
        """픽업 도착 화면 터치 시"""
        self.log_info("📍 픽업 도착 화면이 터치되었습니다!")
        
        # 주문 확인 화면으로 전환
        self.screen_manager.show_screen("CHECKING_ORDER")
    
    # 📋 DELI_3: 주문 확인
    def setup_order_confirm_events(self):
        """주문 확인 화면"""
        self.log_info("주문 확인 화면 준비")
        
        # 확인 버튼 이벤트 연결
        self.setup_button_event("confirmButton", self.on_order_confirmed)
        # 뒤로가기 버튼 이벤트 연결
        self.setup_button_event("backButton", self.on_back_to_arrival)
    
    def on_order_confirmed(self):
        """확인 버튼 클릭 시"""
        self.log_info("📋 주문 확인 완료!")
        
        # 픽업 서랍 조작 화면으로 전환
        self.screen_manager.show_screen("PICKUP_DRAWER_CONTROL")
    
    def on_back_to_arrival(self):
        """뒤로가기 버튼 클릭 시"""
        self.log_info("⬅️ 픽업 도착 화면으로 되돌아가기")
        
        # 픽업 도착 화면으로 되돌아가기
        self.screen_manager.show_screen("PICKUP_ARRIVED")
    
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
        self.log_info("배송지 도착 화면 - 터치 대기")
        
        # 전체 화면 터치 이벤트 연결
        self.setup_touch_event("fullScreenTouchArea", self.on_delivery_arrival_touch)
    
    def on_delivery_arrival_touch(self):
        """배송지 도착 화면 터치 시"""
        self.log_info("🏠 배송지 도착 화면이 터치되었습니다!")
        
        # 배송 서랍 조작 화면으로 전환
        self.screen_manager.show_screen("DELIVERY_DRAWER_CONTROL")
    
    # 📦 DELI_7: 배송 서랍 조작
    def setup_delivery_drawer_events(self):
        """배송 서랍 조작 화면"""
        self.log_info("배송 서랍 조작 화면 준비")
        
        # 서랍 열기 버튼 이벤트 연결
        self.setup_button_event("openDrawerButton", self.on_delivery_drawer_open)
        # 수령 완료 버튼 이벤트 연결 (초기에는 비활성화 상태)
        self.setup_button_event("pickupCompleteButton", self.on_pickup_complete)
        # 뒤로가기 버튼 이벤트 연결
        self.setup_button_event("backButton", self.on_back_to_delivery_arrival)
    
    def on_delivery_drawer_open(self):
        """서랍 열기 버튼 클릭 시"""
        self.log_info("🔓 [배송 서랍 열기] 버튼이 클릭되었습니다")
        
        # 서랍 열기 이벤트 발행 (rgui_event_id: 106)
        self.publish_event(event_id=106, detail="delivery_drawer_open")
    
    def on_back_to_delivery_arrival(self):
        """뒤로가기 버튼 클릭 시"""
        self.log_info("⬅️ 배송 도착 화면으로 되돌아가기")
        
        # 배송 도착 화면으로 되돌아가기
        self.screen_manager.show_screen("DELIVERY_ARRIVED")
    
    def on_pickup_complete(self):
        """[수령 완료] 버튼 클릭 시"""
        self.log_info("✅ [수령 완료] 버튼이 클릭되었습니다")
        
        # 수령 완료 클릭 이벤트 발행 (rgui_event_id: 100)
        self.publish_event(event_id=100, detail="")
    
    def on_drawer_opened(self, detail=""):
        """서랍이 열렸을 때 호출되는 메서드"""
        self.log_info(f"🔓 서랍 열림 알림 수신: {detail}")
        
        # 현재 화면에 따라 버튼 활성화 처리
        current_screen = self.screen_manager.get_current_screen_name()
        
        if current_screen == "PICKUP_DRAWER_CONTROL":
            # 픽업 서랍 조작: 적재완료 버튼 활성화
            loading_button = self.widget.findChild(QPushButton, "loadingCompleteButton")
            if loading_button:
                loading_button.setEnabled(True)
                loading_button.setStyleSheet("background-color: #e74c3c; font-size: 18px; font-weight: bold;")
                self.log_info("✅ 적재완료 버튼이 활성화되었습니다")
                
        elif current_screen == "DELIVERY_DRAWER_CONTROL":
            # 배송 서랍 조작: 수령완료 버튼 활성화
            pickup_button = self.widget.findChild(QPushButton, "pickupCompleteButton")
            if pickup_button:
                pickup_button.setEnabled(True)
                pickup_button.setStyleSheet("background-color: #e74c3c; font-size: 18px; font-weight: bold;")
                self.log_info("✅ 수령완료 버튼이 활성화되었습니다")
    
    # 🎉 DELI_8: 감사 인사
    def setup_thank_you_events(self):
        """감사 인사 화면"""
        self.log_info("감사 인사 화면 - 외부 복귀 카운트다운 서비스 요청 대기")
        # 이 화면에서는 사용자 입력 없음, 외부에서 복귀 카운트다운 서비스 요청시 카운트다운 시작 