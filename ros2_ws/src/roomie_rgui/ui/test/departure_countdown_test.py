#!/usr/bin/env python3
"""
Countdown Screen 단독 실행 파일
5초 카운트다운 화면
"""

import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtGui import QFont

class CountdownScreen(QWidget):
    countdown_finished = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.countdown_value = 5
        self.load_ui()
        self.connect_signals()
        self.start_countdown()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '..', 'departure_countdown.ui')
        try:
            uic.loadUi(ui_file, self)
            print(f"✅ UI 파일 로드 성공: {ui_file}")
        except FileNotFoundError:
            print(f"❌ UI 파일을 찾을 수 없습니다: {ui_file}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ UI 파일 로드 중 오류: {e}")
            sys.exit(1)
    
    def connect_signals(self):
        self.countdown_finished.connect(self.handle_countdown_finished)
        print("✅ 시그널 연결 완료")
    
    def start_countdown(self):
        """카운트다운 시작"""
        print("⏰ 5초 카운트다운을 시작합니다!")
        
        # 초기 숫자 설정
        if hasattr(self, 'countdownNumber'):
            self.countdownNumber.setText(str(self.countdown_value))
        
        # 카운트다운 타이머 설정
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.countdown_timer.start(1000)  # 1초마다
        
        print(f"🔢 카운트다운: {self.countdown_value}")
    
    def update_countdown(self):
        """카운트다운 업데이트"""
        self.countdown_value -= 1
        
        if hasattr(self, 'countdownNumber'):
            self.countdownNumber.setText(str(self.countdown_value))
        
        print(f"🔢 카운트다운: {self.countdown_value}")
        
        # 카운트다운 완료 체크
        if self.countdown_value <= 0:
            self.countdown_timer.stop()
            self.countdown_finished.emit()
    
    def handle_countdown_finished(self):
        """카운트다운 완료 처리"""
        print("🎉 카운트다운 완료!")
        print("🚀 로봇이 출발합니다!")
        
        # UI 업데이트
        if hasattr(self, 'countdownTitle'):
            self.countdownTitle.setText("출발합니다!")
        
        if hasattr(self, 'countdownSubtitle'):
            self.countdownSubtitle.setText("배송을 시작합니다.")
        
        if hasattr(self, 'countdownNumber'):
            self.countdownNumber.setText("🚀")
            self.countdownNumber.setStyleSheet("""
                font-size: 96px; 
                font-weight: bold; 
                color: #1abc9c; 
                border: 4px solid #1abc9c; 
                border-radius: 75px;
            """)
        
        print("💡 시퀀스 완료! 로봇이 배송을 시작했습니다.")
        
        # 3초 후 재시작 알림
        QTimer.singleShot(3000, self.show_restart_message)
    
    def show_restart_message(self):
        """재시작 메시지"""
        print("🔄 시퀀스가 완료되었습니다.")
        print("💡 실제 시스템에서는 이제 다음 주문을 기다립니다.")
        
        if hasattr(self, 'countdownTitle'):
            self.countdownTitle.setText("배송 시작됨")
        
        if hasattr(self, 'countdownSubtitle'):
            self.countdownSubtitle.setText("다음 주문을 기다립니다.")
    
    def closeEvent(self, event):
        """앱 종료 시 정리"""
        if hasattr(self, 'countdown_timer') and self.countdown_timer.isActive():
            self.countdown_timer.stop()
        print("👋 애플리케이션을 종료합니다.")
        event.accept()

def main():
    app = QApplication(sys.argv)
    font = QFont("Malgun Gothic", 12)
    app.setFont(font)
    
    print("🚀 Countdown Screen 애플리케이션 시작")
    print("⏰ 5초 카운트다운 화면입니다.")
    
    try:
        screen = CountdownScreen()
        screen.show()
        print("✅ 화면이 표시되었습니다.")
        print("⏰ 자동으로 카운트다운이 시작됩니다!")
        sys.exit(app.exec())
    except Exception as e:
        print(f"❌ 애플리케이션 실행 중 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()