#!/usr/bin/env python3
"""
Pickup Moving Screen 단독 실행 파일
"""

import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtGui import QFont

class PickupMovingScreen(QWidget):
    pickup_arrived = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.setup_animations()
        self.connect_signals()
        self.start_simulation()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), 'pickup_moving_screen.ui')
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
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animate)
        self.animation_timer.start(1000)  # 1초마다 애니메이션
        
    def connect_signals(self):
        self.pickup_arrived.connect(self.on_pickup_arrived)
        print("✅ 시그널 연결 완료")
    
    def start_simulation(self):
        print("🚚 픽업 장소로 이동 시뮬레이션 시작")
        print("⏰ 8초 후 자동으로 도착합니다.")
        QTimer.singleShot(8000, self.simulate_arrival)
    
    def animate(self):
        print("🎬 이동 중 애니메이션...")
    
    def simulate_arrival(self):
        print("🏪 픽업 장소 도착!")
        self.pickup_arrived.emit()
    
    def on_pickup_arrived(self):
        print("✅ 픽업 장소에 도착했습니다!")
        if hasattr(self, 'mainMessage'):
            self.mainMessage.setText("픽업 장소에 도착했습니다!")
        print("💡 다음 화면: 도착 완료")

def main():
    app = QApplication(sys.argv)
    font = QFont("Malgun Gothic", 12)
    app.setFont(font)
    
    print("🚀 Pickup Moving Screen 애플리케이션 시작")
    
    try:
        screen = PickupMovingScreen()
        screen.show()
        print("✅ 화면이 표시되었습니다.")
        sys.exit(app.exec())
    except Exception as e:
        print(f"❌ 애플리케이션 실행 중 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()