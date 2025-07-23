#!/usr/bin/env python3
"""
Order Display Screen 단독 실행 파일
주문정보 상세 화면 (직원이 확인하는 화면)
"""

import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtGui import QFont

class OrderDisplayScreen(QWidget):
    order_confirmed = pyqtSignal()
    back_pressed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.setup_order_data()
        self.connect_signals()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '/home/jinhyuk2me/project_ws/Roomie/ros2_ws/src/roomie_rgui/sandbox/screen/order_screen.ui')
        try:
            uic.loadUi(ui_file, self)
            print(f"✅ UI 파일 로드 성공: {ui_file}")
        except FileNotFoundError:
            print(f"❌ UI 파일을 찾을 수 없습니다: {ui_file}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ UI 파일 로드 중 오류: {e}")
            sys.exit(1)
    
    def setup_order_data(self):
        """주문 데이터 설정"""
        # 샘플 주문 데이터 표시
        if hasattr(self, 'roomNumber'):
            self.roomNumber.setText("202호")
        if hasattr(self, 'menuItems'):
            self.menuItems.setText("스파게티 1개\n피자 1개")
        
        print("📝 주문 정보가 표시되었습니다:")
        print("   - 호실: 202호")
        print("   - 메뉴: 스파게티 1개, 피자 1개")
        
    def connect_signals(self):
        if hasattr(self, 'confirmButton'):
            self.confirmButton.clicked.connect(self.on_confirm)
            print("✅ 확인 버튼 시그널 연결됨")
        
        if hasattr(self, 'backButton'):
            self.backButton.clicked.connect(self.on_back)
            print("✅ 뒤로가기 버튼 시그널 연결됨")
        
        self.order_confirmed.connect(self.handle_order_confirm)
        self.back_pressed.connect(self.handle_back)
        print("✅ 모든 시그널 연결 완료")
    
    def on_confirm(self):
        print("✅ 확인 버튼이 클릭되었습니다!")
        print("📦 직원이 주문 내용을 확인했습니다.")
        self.order_confirmed.emit()
    
    def on_back(self):
        print("⬅️ 뒤로가기 버튼이 클릭되었습니다!")
        self.back_pressed.emit()
    
    def handle_order_confirm(self):
        print("✨ 주문 확인이 완료되었습니다!")
        print("🍽️ 이제 직원이 음식을 서랍에 넣을 차례입니다.")
        
        # 버튼 상태 변경
        if hasattr(self, 'confirmButton'):
            self.confirmButton.setText("확인됨")
            self.confirmButton.setEnabled(False)
            self.confirmButton.setStyleSheet("background-color: #27ae60; font-size: 18px; font-weight: bold;")
        
        print("💡 다음 화면: 서랍 조작")
        
        # 3초 후 자동으로 다음 단계 안내
        QTimer.singleShot(3000, self.show_next_step)
    
    def show_next_step(self):
        print("🔄 3초 후 서랍 조작 화면으로 전환 가능합니다.")
    
    def handle_back(self):
        print("🔙 이전 화면으로 돌아갑니다.")

def main():
    app = QApplication(sys.argv)
    font = QFont("Malgun Gothic", 12)
    app.setFont(font)
    
    print("🚀 Order Display Screen 애플리케이션 시작")
    print("👨‍🍳 직원용 주문 확인 화면입니다.")
    
    try:
        screen = OrderDisplayScreen()
        screen.show()
        print("✅ 화면이 표시되었습니다.")
        print("📝 주문 내용을 확인하고 '확인' 버튼을 클릭하세요!")
        sys.exit(app.exec())
    except Exception as e:
        print(f"❌ 애플리케이션 실행 중 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()