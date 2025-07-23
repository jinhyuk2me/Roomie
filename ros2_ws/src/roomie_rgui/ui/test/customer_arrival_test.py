#!/usr/bin/env python3
"""
Customer Arrival Screen 단독 실행 파일
고객 도착 알림 및 서랍 조작 화면
"""

import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtGui import QFont

class CustomerArrivalScreen(QWidget):
    drawer_opened = pyqtSignal()
    pickup_completed = pyqtSignal()
    back_pressed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.drawer_is_open = False
        self.pickup_is_complete = False
        self.load_ui()
        self.setup_initial_state()
        self.connect_signals()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '/home/jinhyuk2me/project_ws/Roomie/ros2_ws/src/roomie_rgui/sandbox/screen/customer_arrival.ui')
        try:
            uic.loadUi(ui_file, self)
            print(f"✅ UI 파일 로드 성공: {ui_file}")
        except FileNotFoundError:
            print(f"❌ UI 파일을 찾을 수 없습니다: {ui_file}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ UI 파일 로드 중 오류: {e}")
            sys.exit(1)
    
    def setup_initial_state(self):
        """초기 상태 설정"""
        print("📦 고객 도착 알림 화면 초기화")
        print("🍽️ 주문하신 음식이 도착했습니다!")
        print("🔧 먼저 '서랍열기' 버튼을 클릭하세요.")
        
        # 수령완료 버튼 비활성화
        if hasattr(self, 'pickupCompleteButton'):
            self.pickupCompleteButton.setEnabled(False)
            self.pickupCompleteButton.setStyleSheet("background-color: #7f8c8d; font-size: 18px; font-weight: bold;")
        
    def connect_signals(self):
        """시그널 연결"""
        if hasattr(self, 'openDrawerButton'):
            self.openDrawerButton.clicked.connect(self.on_open_drawer)
            print("✅ 서랍열기 버튼 시그널 연결됨")
        
        if hasattr(self, 'pickupCompleteButton'):
            self.pickupCompleteButton.clicked.connect(self.on_pickup_complete)
            print("✅ 수령완료 버튼 시그널 연결됨")
        
        if hasattr(self, 'backButton'):
            self.backButton.clicked.connect(self.on_back)
            print("✅ 뒤로가기 버튼 시그널 연결됨")
        
        self.drawer_opened.connect(self.handle_drawer_opened)
        self.pickup_completed.connect(self.handle_pickup_completed)
        self.back_pressed.connect(self.handle_back)
        print("✅ 모든 시그널 연결 완료")
    
    def on_open_drawer(self):
        """서랍열기 버튼 클릭"""
        print("🔓 서랍열기 버튼이 클릭되었습니다!")
        
        if not self.drawer_is_open:
            print("📂 서랍을 여는 중...")
            # 서랍 열림 애니메이션 효과
            self.animate_drawer_opening()
            # 2초 후 서랍 열림 완료
            QTimer.singleShot(2000, self.complete_drawer_opening)
        else:
            print("⚠️ 서랍이 이미 열려있습니다.")
    
    def animate_drawer_opening(self):
        """서랍 열림 애니메이션 효과"""
        if hasattr(self, 'drawerTop'):
            # 상단 서랍이 열리는 시각적 효과
            self.drawerTop.setStyleSheet("background-color: #e74c3c; border-radius: 8px;")
        
        if hasattr(self, 'openDrawerButton'):
            self.openDrawerButton.setText("여는 중...")
            self.openDrawerButton.setEnabled(False)
    
    def complete_drawer_opening(self):
        """서랍 열림 완료"""
        print("✅ 서랍이 열렸습니다!")
        self.drawer_is_open = True
        self.drawer_opened.emit()
    
    def on_pickup_complete(self):
        """수령완료 버튼 클릭"""
        if not self.drawer_is_open:
            print("⚠️ 먼저 서랍을 열어주세요!")
            return
        
        print("📦 수령완료 버튼이 클릭되었습니다!")
        print("🔒 서랍을 닫는 중...")
        
        # 서랍 닫힘 애니메이션
        if hasattr(self, 'drawerTop'):
            self.drawerTop.setStyleSheet("background-color: #27ae60; border-radius: 8px;")
        
        if hasattr(self, 'pickupCompleteButton'):
            self.pickupCompleteButton.setText("처리 중...")
            self.pickupCompleteButton.setEnabled(False)
        
        # 2초 후 수령 완료
        QTimer.singleShot(2000, self.complete_pickup)
    
    def complete_pickup(self):
        """수령 완료"""
        print("✅ 수령이 완료되었습니다!")
        self.pickup_is_complete = True
        self.pickup_completed.emit()
    
    def on_back(self):
        """뒤로가기 버튼 클릭"""
        print("⬅️ 뒤로가기 버튼이 클릭되었습니다!")
        self.back_pressed.emit()
    
    def handle_drawer_opened(self):
        """서랍 열림 처리"""
        print("✨ 서랍 열림이 완료되었습니다!")
        
        # UI 상태 업데이트
        if hasattr(self, 'infoTitle'):
            self.infoTitle.setText("서랍이 열렸습니다!\n물건을 꺼내주세요.")
        
        if hasattr(self, 'openDrawerButton'):
            self.openDrawerButton.setText("서랍열림")
            self.openDrawerButton.setStyleSheet("background-color: #27ae60; font-size: 18px; font-weight: bold;")
        
        if hasattr(self, 'pickupCompleteButton'):
            self.pickupCompleteButton.setEnabled(True)
            self.pickupCompleteButton.setStyleSheet("background-color: #e74c3c; font-size: 18px; font-weight: bold;")
        
        print("🍽️ 이제 음식을 꺼내고 '수령완료' 버튼을 클릭하세요!")
    
    def handle_pickup_completed(self):
        """수령 완료 처리"""
        print("✨ 모든 수령 작업이 완료되었습니다!")
        
        # UI 상태 업데이트
        if hasattr(self, 'mainMessage'):
            self.mainMessage.setText("수령이 완료되었습니다!\n감사합니다.")
        
        if hasattr(self, 'infoTitle'):
            self.infoTitle.setText("수령 완료!")
        
        if hasattr(self, 'infoSubtitle'):
            self.infoSubtitle.setText("맛있게 드세요!")
        
        if hasattr(self, 'pickupCompleteButton'):
            self.pickupCompleteButton.setText("완료됨")
            self.pickupCompleteButton.setStyleSheet("background-color: #27ae60; font-size: 18px; font-weight: bold;")
        
        print("🎉 고객 수령 완료!")
        print("🚀 이제 로봇이 복귀할 차례입니다.")
        
        # 3초 후 완료 메시지
        QTimer.singleShot(3000, self.show_completion_message)
    
    def show_completion_message(self):
        """완료 메시지 표시"""
        print("🎯 배송 및 수령 임무 완료!")
        print("🔄 로봇이 대기 위치로 복귀합니다.")
    
    def handle_back(self):
        """뒤로가기 처리"""
        print("🔙 이전 화면으로 돌아갑니다.")

def main():
    app = QApplication(sys.argv)
    font = QFont("Malgun Gothic", 12)
    app.setFont(font)
    
    print("🚀 Customer Arrival Screen 애플리케이션 시작")
    print("👤 고객 도착 알림 및 서랍 조작 화면입니다.")
    
    try:
        screen = CustomerArrivalScreen()
        screen.show()
        print("✅ 화면이 표시되었습니다.")
        print("🔧 '서랍열기' → 물건 수령 → '수령완료' 순서로 진행하세요!")
        sys.exit(app.exec())
    except Exception as e:
        print(f"❌ 애플리케이션 실행 중 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()