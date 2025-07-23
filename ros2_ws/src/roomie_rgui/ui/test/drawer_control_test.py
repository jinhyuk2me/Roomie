#!/usr/bin/env python3
"""
Drawer Control Screen 단독 실행 파일
서랍열기 + 적재완료 통합 화면
"""

import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QTimer, pyqtSignal
from PyQt6.QtGui import QFont

class DrawerControlScreen(QWidget):
    drawer_opened = pyqtSignal()
    loading_completed = pyqtSignal()
    back_pressed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.drawer_is_open = False
        self.load_ui()
        self.setup_initial_state()
        self.connect_signals()
        
    def load_ui(self):
        ui_file = os.path.join(os.path.dirname(__file__), '..', 'drawer_control.ui')
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
        # 적재완료 버튼 비활성화
        if hasattr(self, 'loadingCompleteButton'):
            self.loadingCompleteButton.setEnabled(False)
            self.loadingCompleteButton.setStyleSheet("background-color: #7f8c8d; font-size: 18px; font-weight: bold;")
        
        print("📦 서랍 조작 화면 초기화 완료")
        print("🔧 먼저 '서랍열기' 버튼을 클릭하세요.")
        
    def connect_signals(self):
        if hasattr(self, 'openDrawerButton'):
            self.openDrawerButton.clicked.connect(self.on_open_drawer)
            print("✅ 서랍열기 버튼 시그널 연결됨")
        
        if hasattr(self, 'loadingCompleteButton'):
            self.loadingCompleteButton.clicked.connect(self.on_loading_complete)
            print("✅ 적재완료 버튼 시그널 연결됨")
        
        if hasattr(self, 'backButton'):
            self.backButton.clicked.connect(self.on_back)
            print("✅ 뒤로가기 버튼 시그널 연결됨")
        
        self.drawer_opened.connect(self.handle_drawer_opened)
        self.loading_completed.connect(self.handle_loading_completed)
        self.back_pressed.connect(self.handle_back)
        print("✅ 모든 시그널 연결 완료")
    
    def on_open_drawer(self):
        print("🔓 서랍열기 버튼이 클릭되었습니다!")
        if not self.drawer_is_open:
            print("📂 서랍을 여는 중...")
            # 2초 후 서랍 열림 완료
            QTimer.singleShot(2000, self.complete_drawer_opening)
        else:
            print("⚠️ 서랍이 이미 열려있습니다.")
    
    def complete_drawer_opening(self):
        print("✅ 서랍이 열렸습니다!")
        self.drawer_is_open = True
        self.drawer_opened.emit()
    
    def on_loading_complete(self):
        if not self.drawer_is_open:
            print("⚠️ 먼저 서랍을 열어주세요!")
            return
        
        print("📦 적재완료 버튼이 클릭되었습니다!")
        print("🔒 서랍을 닫는 중...")
        # 2초 후 적재 완료
        QTimer.singleShot(2000, self.complete_loading)
    
    def complete_loading(self):
        print("✅ 적재가 완료되었습니다!")
        self.loading_completed.emit()
    
    def on_back(self):
        print("⬅️ 뒤로가기 버튼이 클릭되었습니다!")
        self.back_pressed.emit()
    
    def handle_drawer_opened(self):
        print("✨ 서랍 열기가 완료되었습니다!")
        
        # UI 상태 업데이트
        if hasattr(self, 'instructionText'):
            self.instructionText.setText("서랍이 열렸습니다.\n물품을 넣고 적재완료를 눌러주세요.")
        
        if hasattr(self, 'openDrawerButton'):
            self.openDrawerButton.setText("서랍열림")
            self.openDrawerButton.setEnabled(False)
            self.openDrawerButton.setStyleSheet("background-color: #27ae60; font-size: 18px; font-weight: bold;")
        
        if hasattr(self, 'loadingCompleteButton'):
            self.loadingCompleteButton.setEnabled(True)
            self.loadingCompleteButton.setStyleSheet("background-color: #e74c3c; font-size: 18px; font-weight: bold;")
        
        print("🍽️ 이제 음식을 서랍에 넣고 '적재완료' 버튼을 클릭하세요!")
    
    def handle_loading_completed(self):
        print("✨ 모든 적재 작업이 완료되었습니다!")
        
        # UI 상태 업데이트
        if hasattr(self, 'instructionText'):
            self.instructionText.setText("적재가 완료되었습니다!\n배송을 시작합니다.")
        
        if hasattr(self, 'loadingCompleteButton'):
            self.loadingCompleteButton.setText("완료됨")
            self.loadingCompleteButton.setEnabled(False)
            self.loadingCompleteButton.setStyleSheet("background-color: #27ae60; font-size: 18px; font-weight: bold;")
        
        print("🚀 이제 로봇이 배송을 시작할 준비가 되었습니다!")
        print("💡 다음 화면: 5초 카운트다운")
    
    def handle_back(self):
        print("🔙 이전 화면으로 돌아갑니다.")

def main():
    app = QApplication(sys.argv)
    font = QFont("Malgun Gothic", 12)
    app.setFont(font)
    
    print("🚀 Drawer Control Screen 애플리케이션 시작")
    print("📦 서랍 조작 화면입니다.")
    
    try:
        screen = DrawerControlScreen()
        screen.show()
        print("✅ 화면이 표시되었습니다.")
        print("🔧 '서랍열기' → 물품 적재 → '적재완료' 순서로 진행하세요!")
        sys.exit(app.exec())
    except Exception as e:
        print(f"❌ 애플리케이션 실행 중 오류: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()