#!/usr/bin/env python3
"""
Thank You Screen 단독 실행 파일
감사 인사 및 로봇 얼굴 화면
"""

import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, QPropertyAnimation, QRect, QEasingCurve, pyqtSignal
from PyQt6.QtGui import QFont
import random

class ThankYouScreen(QWidget):
    animation_finished = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.setup_animations()
        self.connect_signals()
        self.start_animations()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '/home/jinhyuk2me/project_ws/Roomie/ros2_ws/src/roomie_rgui/sandbox/screen/thank_you.ui')
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
        """애니메이션 설정"""
        # 눈 깜빡임 타이머
        self.blink_timer = QTimer()
        self.blink_timer.timeout.connect(self.blink_eyes)
        
        # 하트 펄스 타이머
        self.heart_timer = QTimer()
        self.heart_timer.timeout.connect(self.animate_hearts)
        
        # 별 반짝임 타이머
        self.star_timer = QTimer()
        self.star_timer.timeout.connect(self.animate_stars)
        
        # 볼 애니메이션 타이머
        self.cheek_timer = QTimer()
        self.cheek_timer.timeout.connect(self.animate_cheeks)
        
        # 메시지 페이드 애니메이션
        if hasattr(self, 'mainMessage'):
            self.message_animation = QPropertyAnimation(self.mainMessage, b"geometry")
            self.message_animation.setDuration(1500)
            self.message_animation.setEasingCurve(QEasingCurve.Type.OutBounce)
        
        print("🎬 애니메이션 설정 완료")
    
    def connect_signals(self):
        """시그널 연결"""
        self.animation_finished.connect(self.on_animation_finished)
        print("✅ 시그널 연결 완료")
    
    def start_animations(self):
        """모든 애니메이션 시작"""
        print("🎉 감사 인사 화면 애니메이션 시작!")
        
        # 각 애니메이션을 다른 간격으로 시작
        self.blink_timer.start(3000)  # 3초마다 눈 깜빡임
        self.heart_timer.start(1500)  # 1.5초마다 하트 펄스
        self.star_timer.start(2000)   # 2초마다 별 반짝임
        self.cheek_timer.start(4000)  # 4초마다 볼 색깔 변화
        
        # 메시지 등장 애니메이션
        self.animate_message_entrance()
        
        print("😊 로봇이 감사 인사를 전하고 있습니다!")
        
        # 10초 후 애니메이션 완료
        QTimer.singleShot(10000, self.finish_animations)
    
    def blink_eyes(self):
        """눈 깜빡임 애니메이션"""
        if hasattr(self, 'leftEyeHighlight') and hasattr(self, 'rightEyeHighlight'):
            # 눈을 감기 (하이라이트를 크게)
            self.leftEyeHighlight.setStyleSheet("background-color: #3a4a5c; border-radius: 30px;")
            self.rightEyeHighlight.setStyleSheet("background-color: #3a4a5c; border-radius: 30px;")
            
            # 150ms 후 눈 뜨기
            QTimer.singleShot(150, self.open_eyes)
        
        print("😉 로봇이 눈을 깜빡입니다")
    
    def open_eyes(self):
        """눈 뜨기"""
        if hasattr(self, 'leftEyeHighlight') and hasattr(self, 'rightEyeHighlight'):
            self.leftEyeHighlight.setStyleSheet("background-color: #3a4a5c; border-radius: 20px;")
            self.rightEyeHighlight.setStyleSheet("background-color: #3a4a5c; border-radius: 20px;")
    
    def animate_hearts(self):
        """하트 펄스 애니메이션"""
        hearts = ['heartIcon1', 'heartIcon2', 'heartIcon3', 'heartIcon4']
        heart_emojis = ['💕', '💖', '💗', '💝', '💘', '💞']
        
        for heart_name in hearts:
            if hasattr(self, heart_name):
                heart = getattr(self, heart_name)
                # 랜덤 하트 이모지로 변경
                new_emoji = random.choice(heart_emojis)
                heart.setText(new_emoji)
                
                # 크기 펄스 효과
                original_size = "font-size: 24px;"
                pulse_size = "font-size: 32px;"
                heart.setStyleSheet(pulse_size)
                
                # 200ms 후 원래 크기로
                QTimer.singleShot(200, lambda h=heart: h.setStyleSheet(original_size))
        
        print("💖 하트들이 펄스 애니메이션 중입니다")
    
    def animate_stars(self):
        """별 반짝임 애니메이션"""
        stars = ['starIcon1', 'starIcon2']
        star_emojis = ['✨', '⭐', '🌟', '💫']
        
        for star_name in stars:
            if hasattr(self, star_name):
                star = getattr(self, star_name)
                # 랜덤 별 이모지로 변경
                new_emoji = random.choice(star_emojis)
                star.setText(new_emoji)
                
                # 투명도 효과
                star.setStyleSheet("font-size: 18px; color: white;")
                QTimer.singleShot(500, lambda s=star: s.setStyleSheet("font-size: 18px; color: rgba(255, 255, 255, 0.5);"))
        
        print("✨ 별들이 반짝입니다")
    
    def animate_cheeks(self):
        """볼 색깔 변화 애니메이션"""
        cheek_colors = ["#e74c3c", "#f39c12", "#e67e22", "#d35400"]
        
        if hasattr(self, 'leftCheek') and hasattr(self, 'rightCheek'):
            new_color = random.choice(cheek_colors)
            self.leftCheek.setStyleSheet(f"background-color: {new_color}; border-radius: 15px;")
            self.rightCheek.setStyleSheet(f"background-color: {new_color}; border-radius: 15px;")
        
        print("😊 로봇의 볼이 색깔을 바꿉니다")
    
    def animate_message_entrance(self):
        """메시지 등장 애니메이션"""
        if not hasattr(self, 'message_animation') or not hasattr(self, 'mainMessage'):
            return
        
        # 초기 위치 (화면 아래에서 시작)
        start_rect = QRect(660, 800, 600, 120)
        end_rect = QRect(660, 550, 600, 120)
        
        self.mainMessage.setGeometry(start_rect)
        self.message_animation.setStartValue(start_rect)
        self.message_animation.setEndValue(end_rect)
        self.message_animation.start()
        
        print("📝 메시지가 화면에 등장합니다")
    
    def finish_animations(self):
        """애니메이션 완료"""
        print("🎬 모든 애니메이션이 완료되었습니다!")
        self.animation_finished.emit()
    
    def on_animation_finished(self):
        """애니메이션 완료 처리"""
        print("✨ 감사 인사가 완료되었습니다!")
        
        # 최종 메시지 변경
        if hasattr(self, 'subMessage'):
            self.subMessage.setText("행복한 하루 되세요! 🌈")
        
        print("🤖 로봇이 행복해합니다!")
        print("💡 실제 시스템에서는 이제 대기 화면으로 돌아갑니다.")
        
        # 5초 후 재시작 알림
        QTimer.singleShot(5000, self.show_restart_message)
    
    def show_restart_message(self):
        """재시작 메시지"""
        print("🔄 감사 인사 완료!")
        print("💡 다음 주문을 위해 시스템이 준비됩니다.")
    
    def stop_animations(self):
        """모든 애니메이션 중지"""
        timers = ['blink_timer', 'heart_timer', 'star_timer', 'cheek_timer']
        for timer_name in timers:
            if hasattr(self, timer_name):
                timer = getattr(self, timer_name)
                if timer.isActive():
                    timer.stop()
        
        if hasattr(self, 'message_animation'):
            self.message_animation.stop()
        
        print("⏹️ 모든 애니메이션 중지")
    
    def closeEvent(self, event):
        """앱 종료 시 정리"""
        self.stop_animations()
        print("👋 애플리케이션을 종료합니다.")
        event.accept()

def main():
    app = QApplication(sys.argv)
    font = QFont("Malgun Gothic", 12)
    app.setFont(font)
    
    print("🚀 Thank You Screen 애플리케이션 시작")
    print("😊 감사 인사 및 로봇 얼굴 화면입니다.")
    
    try:
        screen = ThankYouScreen()
        screen.show()
        print("✅ 화면이 표시되었습니다.")
        print("🎬 귀여운 로봇이 감사 인사를 전합니다!")
        sys.exit(app.exec())
    except Exception as e:
        print(f"❌ 애플리케이션 실행 중 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()