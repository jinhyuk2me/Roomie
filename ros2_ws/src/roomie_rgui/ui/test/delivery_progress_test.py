#!/usr/bin/env python3
"""
Delivery Progress Screen 단독 실행 파일
배송중입니다 화면
"""

import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, QPropertyAnimation, QRect, QEasingCurve, pyqtSignal
from PyQt6.QtGui import QFont

class DeliveryProgressScreen(QWidget):
    delivery_completed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.setup_animations()
        self.connect_signals()
        self.start_delivery_simulation()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '/home/jinhyuk2me/project_ws/Roomie/ros2_ws/src/roomie_rgui/sandbox/screen/delivery_progress.ui')
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
        # 로딩 점 애니메이션 타이머
        self.loading_timer = QTimer()
        self.loading_timer.timeout.connect(self.animate_loading_dots)
        self.loading_index = 0
        
        # 진행률 바 애니메이션
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        
        # 배송 트럭 애니메이션
        if hasattr(self, 'deliveryIcon'):
            self.delivery_animation = QPropertyAnimation(self.deliveryIcon, b"geometry")
            self.delivery_animation.setDuration(3000)
            self.delivery_animation.setEasingCurve(QEasingCurve.Type.InOutSine)
        
        # 로딩 점들 리스트
        self.loading_dots = []
        for i in range(1, 6):
            dot_name = f'loadingDot{i}'
            if hasattr(self, dot_name):
                self.loading_dots.append(getattr(self, dot_name))
    
    def connect_signals(self):
        """시그널 연결"""
        self.delivery_completed.connect(self.on_delivery_completed)
        print("✅ 시그널 연결 완료")
    
    def start_delivery_simulation(self):
        """배송 시뮬레이션 시작"""
        print("🚚 배송 시뮬레이션을 시작합니다!")
        
        # 애니메이션 시작
        self.loading_timer.start(400)  # 400ms 간격
        self.progress_timer.start(200)  # 200ms 간격
        self.animate_delivery_truck()
        
        print("📦 목적지로 배송 중...")
        print("⏰ 15초 후 배송 완료 예정")
        
        # 15초 후 배송 완료
        QTimer.singleShot(15000, self.complete_delivery)
    
    def animate_loading_dots(self):
        """로딩 점들 순차 애니메이션"""
        if not self.loading_dots:
            return
        
        # 모든 점을 기본 투명도로
        for dot in self.loading_dots:
            dot.setStyleSheet("background-color: rgba(0, 206, 209, 0.3); border-radius: 8px;")
        
        # 현재 점만 밝게
        if self.loading_index < len(self.loading_dots):
            current_dot = self.loading_dots[self.loading_index]
            current_dot.setStyleSheet("background-color: #00CED1; border-radius: 8px;")
        
        # 다음 점으로 이동
        self.loading_index = (self.loading_index + 1) % len(self.loading_dots)
    
    def update_progress(self):
        """진행률 바 업데이트"""
        if not hasattr(self, 'progressBar'):
            return
        
        # 진행률 증가 (15초 동안 100% 달성을 위해 0.33%씩)
        self.progress_value += 0.33
        
        # 진행률 바의 width 업데이트 (최대 500px)
        new_width = int((self.progress_value / 100) * 500)
        if new_width > 500:
            new_width = 500
            self.progress_value = 100
        
        current_rect = self.progressBar.geometry()
        new_rect = QRect(current_rect.x(), current_rect.y(), new_width, current_rect.height())
        self.progressBar.setGeometry(new_rect)
        
        # 진행률에 따른 상태 메시지 업데이트
        if hasattr(self, 'statusText'):
            if self.progress_value < 30:
                self.statusText.setText("목적지로 이동 중...")
            elif self.progress_value < 70:
                self.statusText.setText("배송 진행 중...")
            elif self.progress_value < 95:
                self.statusText.setText("곧 도착합니다...")
            else:
                self.statusText.setText("목적지 근처 도착!")
        
        # 100% 달성 시 타이머 중지
        if self.progress_value >= 100:
            self.progress_timer.stop()
            print("📊 진행률 100% 달성")
    
    def animate_delivery_truck(self):
        """배송 트럭 좌우 이동 애니메이션"""
        if not hasattr(self, 'delivery_animation') or not hasattr(self, 'deliveryIcon'):
            return
        
        # 트럭이 좌우로 살짝 이동하는 효과
        original_rect = QRect(960, 300, 80, 80)
        moved_rect = QRect(980, 300, 80, 80)
        
        self.delivery_animation.setStartValue(original_rect)
        self.delivery_animation.setEndValue(moved_rect)
        self.delivery_animation.finished.connect(self.delivery_truck_return)
        self.delivery_animation.start()
    
    def delivery_truck_return(self):
        """배송 트럭 원래 위치로"""
        original_rect = QRect(960, 300, 80, 80)
        moved_rect = QRect(980, 300, 80, 80)
        
        self.delivery_animation.setStartValue(moved_rect)
        self.delivery_animation.setEndValue(original_rect)
        self.delivery_animation.finished.connect(self.animate_delivery_truck)
        self.delivery_animation.start()
    
    def complete_delivery(self):
        """배송 완료"""
        print("🎉 배송 완료!")
        self.delivery_completed.emit()
    
    def on_delivery_completed(self):
        """배송 완료 처리"""
        print("✅ 목적지에 도착했습니다!")
        
        # 애니메이션 중지
        self.stop_animations()
        
        # 메시지 변경
        if hasattr(self, 'mainMessage'):
            self.mainMessage.setText("배송 완료!")
        
        if hasattr(self, 'statusText'):
            self.statusText.setText("목적지에 도착했습니다.")
        
        # 트럭 아이콘을 체크마크로 변경
        if hasattr(self, 'deliveryIcon'):
            self.deliveryIcon.setText("✅")
        
        print("💡 다음 단계: 고객 픽업 또는 서랍 열기")
        
        # 3초 후 완료 메시지
        QTimer.singleShot(3000, self.show_completion_message)
    
    def show_completion_message(self):
        """완료 메시지 표시"""
        print("🎯 배송 임무 완료!")
        print("👤 이제 고객이 물품을 수령할 차례입니다.")
        
        if hasattr(self, 'mainMessage'):
            self.mainMessage.setText("수령 대기중")
        
        if hasattr(self, 'statusText'):
            self.statusText.setText("고객의 수령을 기다립니다.")
    
    def stop_animations(self):
        """모든 애니메이션 중지"""
        if hasattr(self, 'loading_timer'):
            self.loading_timer.stop()
        if hasattr(self, 'progress_timer'):
            self.progress_timer.stop()
        if hasattr(self, 'delivery_animation'):
            self.delivery_animation.stop()
        
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
    
    print("🚀 Delivery Progress Screen 애플리케이션 시작")
    print("🚚 배송중입니다 화면입니다.")
    
    try:
        screen = DeliveryProgressScreen()
        screen.show()
        print("✅ 화면이 표시되었습니다.")
        print("🎬 로딩 애니메이션, 진행률 바, 트럭 이동이 실행됩니다.")
        print("⏰ 15초 후 자동으로 배송 완료 상태로 전환됩니다.")
        sys.exit(app.exec())
    except Exception as e:
        print(f"❌ 애플리케이션 실행 중 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()