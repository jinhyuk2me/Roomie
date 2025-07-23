#!/usr/bin/env python3
"""
Touch Screen 단독 실행 파일
"""

import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, QPropertyAnimation, QRect, pyqtSignal
from PyQt6.QtGui import QFont

class TouchScreen(QWidget):
    touch_activated = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.setup_animations()
        self.connect_signals()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), 'touch_screen.ui')
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
        self.pulse_timer.timeout.connect(self.pulse_animation)
        self.pulse_timer.start(2000)
        
    def connect_signals(self):
        if hasattr(self, 'touchButton'):
            self.touchButton.clicked.connect(self.on_touch)
            print("✅ 터치 버튼 시그널 연결됨")
        self.touch_activated.connect(self.handle_touch_event)
    
    def pulse_animation(self):
        print("🔵 펄스 애니메이션 실행")
    
    def on_touch(self):
        print("🖱️ 터치 버튼이 클릭되었습니다!")
        self.touch_activated.emit()
    
    def handle_touch_event(self):
        print("✨ 터치 이벤트가 처리되었습니다!")
        print("💡 다음 화면: 픽업 장소로 이동중")

def main():
    app = QApplication(sys.argv)
    font = QFont("Malgun Gothic", 12)
    app.setFont(font)
    
    print("🚀 Touch Screen 애플리케이션 시작")
    
    try:
        screen = TouchScreen()
        screen.show()
        print("✅ 화면이 표시되었습니다. 터치 버튼을 클릭해보세요!")
        sys.exit(app.exec())
    except Exception as e:
        print(f"❌ 애플리케이션 실행 중 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()