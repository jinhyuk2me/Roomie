import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QGroupBox, QListWidget, QListWidgetItem
)
from PyQt6.QtCore import QTimer, pyqtSignal
import requests
import websocket
import threading
import json
from PyQt6.QtCore import Qt

class SGUI(QMainWindow):
    """직원용 GUI (SGUI) - 배송 작업 준비 및 관리"""

    # PyQt Signals for thread-safe GUI updates
    log_signal = pyqtSignal(str)
    task_update_signal = pyqtSignal()

    API_BASE_URL = "http://localhost:8000/api/gui"
    WS_URL = "ws://localhost:8000/api/gui/ws/staff/staff_01"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("👨‍🍳 직원용 GUI (SGUI)")
        self.setGeometry(650, 100, 400, 500)

        # 신호 연결 (스레드 안전성을 위해)
        self.log_signal.connect(self._update_log)
        self.task_update_signal.connect(self.load_tasks)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.create_task_list_group()
        self.create_log_group()

        main_layout.addWidget(self.task_list_group)
        main_layout.addWidget(self.log_group)

        # GUI 초기화 완료 후 WebSocket 연결
        QTimer.singleShot(100, self.connect_websocket)

    def create_task_list_group(self):
        """작업 목록 그룹 생성"""
        self.task_list_group = QGroupBox("대기 중인 작업 목록")
        layout = QVBoxLayout()
        
        # 상단 버튼들
        button_layout = QHBoxLayout()
        self.refresh_button = QPushButton("새로고침")
        self.refresh_button.clicked.connect(self.load_tasks)
        
        self.ready_button = QPushButton("선택한 작업 준비완료")
        self.ready_button.clicked.connect(self.on_ready_button_clicked)
        self.ready_button.setEnabled(False)  # 초기에는 비활성화
        
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.ready_button)
        
        # 작업 목록
        self.task_list = QListWidget()
        self.task_list.itemDoubleClicked.connect(self.on_task_ready)
        self.task_list.itemSelectionChanged.connect(self.on_task_selection_changed)

        layout.addLayout(button_layout)
        layout.addWidget(QLabel("작업을 선택하고 '준비완료' 버튼을 클릭하거나 더블클릭하세요"))
        layout.addWidget(self.task_list)
        self.task_list_group.setLayout(layout)

    def create_log_group(self):
        """로그 그룹 생성"""
        self.log_group = QGroupBox("로그")
        layout = QVBoxLayout()
        self.log_text_edit = QTextEdit()
        self.log_text_edit.setReadOnly(True)
        layout.addWidget(self.log_text_edit)
        self.log_group.setLayout(layout)
        
    def log(self, message):
        """스레드 안전한 로그 출력"""
        self.log_signal.emit(message)
        
    def _update_log(self, message):
        """실제 GUI 업데이트 (메인 스레드에서만 호출됨)"""
        self.log_text_edit.append(message)
        
    def load_tasks(self):
        """서버에서 대기 중인 작업 목록을 불러옵니다."""
        try:
            url = f"{self.API_BASE_URL}/get_tasks"
            params = {"task_status": "접수됨"}
            self.log(f"[DEBUG] API 요청: {url} with params: {params}")
            
            response = requests.get(url, params=params)
            self.log(f"[DEBUG] 응답 상태 코드: {response.status_code}")
            
            response.raise_for_status()
            response_data = response.json()
            self.log(f"[DEBUG] 응답 데이터: {response_data}")
            
            tasks = response_data.get('tasks', [])
            self.log(f"[DEBUG] 파싱된 작업 수: {len(tasks)}")
            
            self.task_list.clear()
            for task in tasks:
                self.log(f"[DEBUG] 작업 데이터: {task}")
                item_text = f"작업 ID: {task['task_id']} | 목적지: {task['destination']}"
                list_item = QListWidgetItem(item_text)
                # PyQt6에서는 Qt.ItemDataRole.UserRole을 사용
                list_item.setData(Qt.ItemDataRole.UserRole, task['task_id']) # 작업 ID 저장
                self.task_list.addItem(list_item)
            self.log(f"[INFO] {len(tasks)}개의 작업을 불러왔습니다.")
        except requests.exceptions.RequestException as e:
            self.log(f"[ERROR] 작업 목록 로딩 실패: {e}")
        except Exception as e:
            self.log(f"[ERROR] 예상치 못한 오류: {e}")
            import traceback
            self.log(f"[ERROR] 상세 오류: {traceback.format_exc()}")

    def on_task_ready(self, item):
        """작업 준비 완료 버튼 클릭 시 호출됩니다."""
        task_id = item.data(Qt.ItemDataRole.UserRole)
        try:
            # 새로운 API 요청 형식에 맞춰 업데이트
            request_data = {
                "payload": {
                    "task_id": task_id,
                    "new_status": "준비 완료"
                }
            }
            
            response = requests.post(
                f"{self.API_BASE_URL}/change_task_status",
                json=request_data
            )
            response.raise_for_status()
            
            response_data = response.json()
            # payload.success가 True인 경우 성공으로 처리
            if response_data.get("payload", {}).get("success", False):
                self.log(f"[INFO] 작업 {task_id}를 '준비 완료' 상태로 변경했습니다.")
                self.load_tasks() # 목록 새로고침
            else:
                # payload.message 또는 최상위 message 확인
                error_msg = response_data.get("payload", {}).get("message") or response_data.get('message', '알 수 없는 오류')
                self.log(f"[ERROR] 상태 변경 실패: {error_msg}")
                
        except requests.exceptions.RequestException as e:
            self.log(f"[ERROR] 상태 변경 요청 실패: {e}")
        except Exception as e:
            self.log(f"[ERROR] 예상치 못한 오류: {e}")
            import traceback
            self.log(f"[ERROR] 상세 오류: {traceback.format_exc()}")

    def on_task_selection_changed(self):
        """작업 선택이 변경될 때 호출됩니다."""
        selected_items = self.task_list.selectedItems()
        self.ready_button.setEnabled(len(selected_items) > 0)

    def on_ready_button_clicked(self):
        """준비완료 버튼 클릭 시 호출됩니다."""
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            self.log("[WARN] 먼저 작업을 선택해주세요.")
            return
        
        selected_item = selected_items[0]
        self.on_task_ready(selected_item)

    def connect_websocket(self):
        """WebSocket 연결"""
        try:
            self.ws = websocket.WebSocketApp(
                self.WS_URL,
                on_message=self.on_ws_message,
                on_error=self.on_ws_error,
                on_close=self.on_ws_close,
                on_open=self.on_ws_open
            )
            ws_thread = threading.Thread(target=self.ws.run_forever)
            ws_thread.daemon = True
            ws_thread.start()
            self.log("[INIT] WebSocket 연결 시도 중...")
        except Exception as e:
            self.log(f"[ERROR] WebSocket 연결 실패: {e}")

    def on_ws_open(self, ws):
        self.log("[WS] 연결되었습니다.")

    def on_ws_message(self, ws, message):
        try:
            data = json.loads(message)
            event_type = data.get('type', '')
            event_action = data.get('action', '')
            
            if event_type == 'event':
                if event_action == 'food_order_creation':
                    payload = data.get('payload', {})
                    self.log(f"[WS] 새 음식 주문 생성: Task ID {payload.get('task_id', 'N/A')}")
                    self.log(f"    위치: {payload.get('location', 'N/A')}")
                    self.log(f"    주문 내역: {len(payload.get('order_details', []))}개 아이템")
                    # 신호를 통해 스레드 안전하게 GUI 업데이트
                    self.task_update_signal.emit()
                    
                elif event_action == 'supply_order_creation':
                    payload = data.get('payload', {})
                    self.log(f"[WS] 새 비품 주문 생성: Task ID {payload.get('task_id', 'N/A')}")
                    self.log(f"    위치: {payload.get('location', 'N/A')}")
                    self.log(f"    비품 내역: {len(payload.get('order_details', []))}개 아이템")
                    self.task_update_signal.emit()
                    
                elif event_action == 'food_pickup_arrival':
                    payload = data.get('payload', {})
                    self.log(f"[WS] 로봇이 픽업 장소에 도착했습니다!")
                    self.log(f"    Task ID: {payload.get('task_id', 'N/A')}")
                    self.log(f"    Robot ID: {payload.get('robot_id', 'N/A')}")
                    
                elif event_action == 'supply_pickup_arrival':
                    payload = data.get('payload', {})
                    self.log(f"[WS] 로봇이 비품 픽업 장소에 도착했습니다!")
                    self.log(f"    Task ID: {payload.get('task_id', 'N/A')}")
                    self.log(f"    Robot ID: {payload.get('robot_id', 'N/A')}")
                    
                else:
                    self.log(f"[WS] 알 수 없는 이벤트: {event_action}")
            else:
                self.log(f"[WS] 알 수 없는 메시지 타입: {event_type}")
                
        except Exception as e:
            self.log(f"[WS] 메시지 처리 오류: {e}")
            import traceback
            self.log(f"[WS] 상세 오류: {traceback.format_exc()}")

    def on_ws_error(self, ws, error):
        self.log(f"[WS] 에러: {error}")

    def on_ws_close(self, ws, close_status_code, close_msg):
        self.log("[WS] 연결이 종료되었습니다.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SGUI()
    gui.show()
    sys.exit(app.exec())
