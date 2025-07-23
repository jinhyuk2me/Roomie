#!/usr/bin/env python3
"""
Arrival Complete Screen 단독 실행 파일
"""

import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtGui import QFont

class ArrivalCompleteScreen(QWidget):
    screen_touched = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.setup_animations()
        self.connect_signals()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '/home/jinhyuk2me/project_ws/Roomie/ros2_ws/src/roomie_rgui/sandbox/pickup_arrival_screen.ui')
        try:
            uic.loadUi(ui_file, self)
            print(f"✅ UI 파일 로드 성공: {ui_file}")
        except FileNotFoundError:
            print(f"❌ UI 파일을 찾을 수 없습니다: {ui_file}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ UI 파일 로드 중 오류: {e}")
            sys.exit(1)
    
    def setup_animations(self):
        self.pulse_timer = QTimer()
        self.pulse_timer.timeout.connect(self.pulse_effect)
        self.pulse_timer.start(2000)  # 2초마다 펄스
        
    def connect_signals(self):
        if hasattr(self, 'fullScreenTouchArea'):
            self.fullScreenTouchArea.clicked.connect(self.on_screen_touch)
            print("✅ 전체 화면 터치 영역 시그널 연결됨")
        self.screen_touched.connect(self.handle_screen_touch)
        print("✅ 시그널 연결 완료")
    
    def pulse_effect(self):
        print("🔵 펄스 효과 실행")
    
    def on_screen_touch(self):
        print("🖱️ 화면이 터치되었습니다!")
        self.show_touch_feedback()
        self.screen_touched.emit()
    
    def show_touch_feedback(self):
        # 시각적 피드백
        original_style = self.fullScreenTouchArea.styleSheet()
        feedback_style = "background-color: rgba(0, 206, 209, 0.1);"
        self.fullScreenTouchArea.setStyleSheet(feedback_style)
        QTimer.singleShot(200, lambda: self.fullScreenTouchArea.setStyleSheet(original_style))
    
    def handle_screen_touch(self):
        print("✨ 터치 이벤트가 처리되었습니다!")
        if hasattr(self, 'arrivalTitle'):
            self.arrivalTitle.setText("픽업 준비 중...")
        if hasattr(self, 'touchMessage'):
            self.touchMessage.setText("음식을 준비하고 있습니다.")
        print("💡 다음 화면: 주문정보 상세")

def main():
    app = QApplication(sys.argv)
    font = QFont("Malgun Gothic", 12)
    app.setFont(font)
    
    print("🚀 Arrival Complete Screen 애플리케이션 시작")
    
    try:
        screen = ArrivalCompleteScreen()
        screen.show()
        print("✅ 화면이 표시되었습니다. 화면을 터치해보세요!")
        sys.exit(app.exec())
    except Exception as e:
        print(f"❌ 애플리케이션 실행 중 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()