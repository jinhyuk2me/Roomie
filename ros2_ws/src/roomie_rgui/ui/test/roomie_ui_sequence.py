#!/usr/bin/env python3
"""
Roomie UI 시퀀스 통합 실행 파일
모든 화면을 순차적으로 실행합니다.

실행 순서:
1. Touch Screen (시작 화면)
2. Pickup Moving (픽업 장소로 이동)
3. Pickup Arrival (픽업 도착)
4. Order Screen (주문 확인)  
5. Drawer Control (서랍 제어)
6. Departure Countdown (출발 카운트다운)
"""

import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtGui import QFont

class TouchScreen(QWidget):
    screen_completed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.connect_signals()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '..', 'touch_screen.ui')
        uic.loadUi(ui_file, self)
        # 스타일시트 강제 적용
        self.setStyleSheet(self.styleSheet())
        print("✅ Touch Screen 로드됨")
        
    def connect_signals(self):
        if hasattr(self, 'touchButton'):
            self.touchButton.clicked.connect(self.on_touch)
            
    def on_touch(self):
        print("👆 Touch Screen 터치됨!")
        QTimer.singleShot(1000, self.screen_completed.emit)

class OrderScreen(QWidget):
    screen_completed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.connect_signals()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '..', 'order_screen.ui')
        uic.loadUi(ui_file, self)
        # 스타일시트 강제 적용
        self.setStyleSheet(self.styleSheet())
        print("✅ Order Screen 로드됨")
        
    def connect_signals(self):
        if hasattr(self, 'confirmButton'):
            self.confirmButton.clicked.connect(self.on_confirm)
            
    def on_confirm(self):
        print("✅ 주문 확인됨!")
        QTimer.singleShot(500, self.screen_completed.emit)

class DrawerControlScreen(QWidget):
    screen_completed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.drawer_is_open = False
        self.load_ui()
        self.setup_initial_state()
        self.connect_signals()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '..', 'drawer_control.ui')
        uic.loadUi(ui_file, self)
        # 스타일시트 강제 적용
        self.setStyleSheet(self.styleSheet())
        print("✅ Drawer Control Screen 로드됨")
        
    def setup_initial_state(self):
        if hasattr(self, 'loadingCompleteButton'):
            self.loadingCompleteButton.setEnabled(False)
            self.loadingCompleteButton.setStyleSheet("background-color: #7f8c8d; font-size: 18px; font-weight: bold;")
        
    def connect_signals(self):
        if hasattr(self, 'openDrawerButton'):
            self.openDrawerButton.clicked.connect(self.on_open_drawer)
        
        if hasattr(self, 'loadingCompleteButton'):
            self.loadingCompleteButton.clicked.connect(self.on_loading_complete)
    
    def on_open_drawer(self):
        print("🔓 서랍열기 버튼 클릭!")
        if not self.drawer_is_open:
            QTimer.singleShot(2000, self.complete_drawer_opening)
    
    def complete_drawer_opening(self):
        print("✅ 서랍이 열렸습니다!")
        self.drawer_is_open = True
        
        if hasattr(self, 'instructionText'):
            self.instructionText.setText("서랍이 열렸습니다.\n물품을 넣고 적재완료를 눌러주세요.")
        
        if hasattr(self, 'openDrawerButton'):
            self.openDrawerButton.setText("서랍열림")
            self.openDrawerButton.setEnabled(False)
            self.openDrawerButton.setStyleSheet("background-color: #27ae60; font-size: 18px; font-weight: bold;")
        
        if hasattr(self, 'loadingCompleteButton'):
            self.loadingCompleteButton.setEnabled(True)
            self.loadingCompleteButton.setStyleSheet("background-color: #e74c3c; font-size: 18px; font-weight: bold;")
    
    def on_loading_complete(self):
        if not self.drawer_is_open:
            return
        
        print("📦 적재완료!")
        QTimer.singleShot(2000, self.complete_loading)
    
    def complete_loading(self):
        print("✅ 적재가 완료되었습니다!")
        
        if hasattr(self, 'instructionText'):
            self.instructionText.setText("적재가 완료되었습니다!\n배송을 시작합니다.")
        
        if hasattr(self, 'loadingCompleteButton'):
            self.loadingCompleteButton.setText("완료됨")
            self.loadingCompleteButton.setEnabled(False)
            self.loadingCompleteButton.setStyleSheet("background-color: #27ae60; font-size: 18px; font-weight: bold;")
        
        QTimer.singleShot(2000, self.screen_completed.emit)


class PickupMovingScreen(QWidget):
    screen_completed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        QTimer.singleShot(3000, self.screen_completed.emit)  # 3초 후 자동 완료
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '..', 'pickup_moving_screen.ui')
        uic.loadUi(ui_file, self)
        # 스타일시트 강제 적용
        self.setStyleSheet(self.styleSheet())
        print("✅ Pickup Moving Screen 로드됨")

class PickupArrivalScreen(QWidget):
    screen_completed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.load_ui()
        self.connect_signals()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '..', 'pickup_arrival_screen.ui')
        uic.loadUi(ui_file, self)
        # 스타일시트 강제 적용
        self.setStyleSheet(self.styleSheet())
        print("✅ Pickup Arrival Screen 로드됨")
        
    def connect_signals(self):
        if hasattr(self, 'fullScreenTouchArea'):
            self.fullScreenTouchArea.clicked.connect(self.on_touch)
            
    def on_touch(self):
        print("👆 도착 화면 터치됨!")
        QTimer.singleShot(1000, self.screen_completed.emit)

class DepartureCountdownScreen(QWidget):
    screen_completed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.countdown_value = 5
        self.countdown_timer = None
        self.load_ui()
        # 카운트다운은 showEvent에서 시작
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '..', 'departure_countdown.ui')
        uic.loadUi(ui_file, self)
        # 스타일시트 강제 적용
        self.setStyleSheet(self.styleSheet())
        print("✅ Departure Countdown Screen 로드됨")
    
    def showEvent(self, event):
        """화면이 표시될 때 카운트다운 시작"""
        super().showEvent(event)
        if self.countdown_timer is None or not self.countdown_timer.isActive():
            self.start_countdown()
    
    def start_countdown(self):
        print("⏰ 출발 카운트다운 시작!")
        
        # 카운트다운 값 리셋
        self.countdown_value = 5
        
        if hasattr(self, 'countdownNumber'):
            self.countdownNumber.setText(str(self.countdown_value))
        
        if hasattr(self, 'countdownTitle'):
            self.countdownTitle.setText("5초후에 출발하겠습니다.")
        
        if self.countdown_timer:
            self.countdown_timer.stop()
        
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.countdown_timer.start(1000)
    
    def update_countdown(self):
        self.countdown_value -= 1
        
        if hasattr(self, 'countdownNumber'):
            self.countdownNumber.setText(str(self.countdown_value))
        
        print(f"🔢 출발 카운트다운: {self.countdown_value}")
        
        if self.countdown_value <= 0:
            self.countdown_timer.stop()
            print("🚀 출발 완료!")
            
            if hasattr(self, 'countdownTitle'):
                self.countdownTitle.setText("출발합니다!")
            
            if hasattr(self, 'countdownNumber'):
                self.countdownNumber.setText("🚀")
            
            QTimer.singleShot(2000, self.screen_completed.emit)

class RoomieUISequence(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.current_screen_index = 0
        # QStackedWidget 배경 스타일 설정
        self.setStyleSheet("""
            QStackedWidget {
                background-color: #3a4a5c;
            }
            QWidget {
                background-color: #3a4a5c;
            }
        """)
        self.setup_screens()
        self.setup_sequence()
        
    def setup_screens(self):
        """모든 화면 생성 및 추가"""
        print("🚀 Roomie UI 시퀀스 시작!")
        print("=" * 50)
        
        # 화면들 생성 (올바른 순서)
        self.touch_screen = TouchScreen()
        self.pickup_moving_screen = PickupMovingScreen()
        self.pickup_arrival_screen = PickupArrivalScreen()
        self.order_screen = OrderScreen()
        self.drawer_control_screen = DrawerControlScreen()
        self.departure_countdown_screen = DepartureCountdownScreen()
        
        # 스택에 추가 (올바른 순서)
        self.addWidget(self.touch_screen)
        self.addWidget(self.pickup_moving_screen)
        self.addWidget(self.pickup_arrival_screen)
        self.addWidget(self.order_screen)
        self.addWidget(self.drawer_control_screen)
        self.addWidget(self.departure_countdown_screen)
        
        # 화면 이름들 (올바른 순서)
        self.screen_names = [
            "Touch Screen",
            "Pickup Moving",
            "Pickup Arrival", 
            "Order Screen",
            "Drawer Control",
            "Departure Countdown"
        ]
        
    def setup_sequence(self):
        """화면 전환 시퀀스 설정"""
        # 각 화면의 완료 시그널을 다음 화면으로 연결 (올바른 순서)
        self.touch_screen.screen_completed.connect(self.next_screen)
        self.pickup_moving_screen.screen_completed.connect(self.next_screen)
        self.pickup_arrival_screen.screen_completed.connect(self.next_screen)
        self.order_screen.screen_completed.connect(self.next_screen)
        self.drawer_control_screen.screen_completed.connect(self.next_screen)
        self.departure_countdown_screen.screen_completed.connect(self.sequence_complete)
        
        # 첫 번째 화면 표시
        self.show_current_screen()
        
    def show_current_screen(self):
        """현재 화면 표시"""
        screen_name = self.screen_names[self.current_screen_index]
        print(f"📺 [{self.current_screen_index + 1}/6] {screen_name} 표시")
        print("-" * 30)
        self.setCurrentIndex(self.current_screen_index)
        
    def next_screen(self):
        """다음 화면으로 전환"""
        current_screen = self.screen_names[self.current_screen_index]
        print(f"✅ {current_screen} 완료!")
        print("")
        
        self.current_screen_index += 1
        
        if self.current_screen_index < len(self.screen_names):
            self.show_current_screen()
    
    def replaceWidget(self, index, new_widget):
        """특정 인덱스의 위젯 교체"""
        old_widget = self.widget(index)
        self.removeWidget(old_widget)
        self.insertWidget(index, new_widget)
        
    def sequence_complete(self):
        """전체 시퀀스 완료"""
        print("🎉 모든 화면 시퀀스가 완료되었습니다!")
        print("=" * 50)
        print("💡 5초 후 처음부터 다시 시작합니다...")
        
        # 5초 후 처음부터 다시 시작
        QTimer.singleShot(5000, self.restart_sequence)
        
    def restart_sequence(self):
        """시퀀스 재시작"""
        print("🔄 시퀀스를 처음부터 다시 시작합니다!")
        print("=" * 50)
        
        self.current_screen_index = 0
        
        # 화면들 재생성 (올바른 순서) - departure_countdown_screen은 재사용
        self.touch_screen = TouchScreen()
        self.pickup_moving_screen = PickupMovingScreen()
        self.pickup_arrival_screen = PickupArrivalScreen()
        self.order_screen = OrderScreen()
        self.drawer_control_screen = DrawerControlScreen()
        
        # departure_countdown_screen의 타이머 정리
        if hasattr(self.departure_countdown_screen, 'countdown_timer') and self.departure_countdown_screen.countdown_timer:
            self.departure_countdown_screen.countdown_timer.stop()
        self.departure_countdown_screen.countdown_timer = None
        
        # 위젯 교체 (올바른 순서) - departure_countdown_screen은 재사용
        self.replaceWidget(0, self.touch_screen)
        self.replaceWidget(1, self.pickup_moving_screen)
        self.replaceWidget(2, self.pickup_arrival_screen)
        self.replaceWidget(3, self.order_screen)
        self.replaceWidget(4, self.drawer_control_screen)
        
        # 시그널 재연결 (올바른 순서)
        self.touch_screen.screen_completed.connect(self.next_screen)
        self.pickup_moving_screen.screen_completed.connect(self.next_screen)
        self.pickup_arrival_screen.screen_completed.connect(self.next_screen)
        self.order_screen.screen_completed.connect(self.next_screen)
        self.drawer_control_screen.screen_completed.connect(self.next_screen)
        
        self.show_current_screen()

def main():
    app = QApplication(sys.argv)
    font = QFont("Malgun Gothic", 12)
    app.setFont(font)
    
    print("🏠 Roomie UI 시퀀스 애플리케이션 시작")
    print("🎬 모든 화면을 순차적으로 실행합니다")
    print("")
    
    try:
        sequence = RoomieUISequence()
        sequence.showFullScreen()  # 전체화면으로 표시
        print("✅ 애플리케이션이 시작되었습니다!")
        print("💡 ESC 키를 누르면 종료됩니다.")
        print("")
        
        sys.exit(app.exec())
    except Exception as e:
        print(f"❌ 애플리케이션 실행 중 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 