import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QPushButton, QTextEdit, QGroupBox, QListWidget, QListWidgetItem,
    QComboBox, QSpinBox, QDoubleSpinBox, QTabWidget
)
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
import requests
import websocket
import threading
import json

class GGUI(QMainWindow):
    """고객용 GUI (GGUI) - 음식 및 비품 주문, 호출"""

    # PyQt Signals for thread-safe GUI updates
    log_signal = pyqtSignal(str)
    
    API_BASE_URL = "http://localhost:8000/api/gui"
    WS_URL_TEMPLATE = "ws://localhost:8000/api/gui/ws/guest/{location_name}"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("🍽️ 고객용 GUI (GGUI)")
        self.setGeometry(1100, 100, 500, 700)

        # 신호 연결 (스레드 안전성을 위해)
        self.log_signal.connect(self._update_log)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 위치 선택
        self.create_location_group()
        
        # 탭 위젯 생성
        self.tab_widget = QTabWidget()
        
        # 음식 주문 탭
        self.food_tab = QWidget()
        self.create_food_order_tab()
        self.tab_widget.addTab(self.food_tab, "🍽️ 음식 주문")
        
        # 비품 주문 탭
        self.supply_tab = QWidget()
        self.create_supply_order_tab()
        self.tab_widget.addTab(self.supply_tab, "🧴 비품 주문")
        
        # 호출 탭
        self.call_tab = QWidget()
        self.create_call_tab()
        self.tab_widget.addTab(self.call_tab, "📞 직원 호출")

        # 로그 그룹
        self.create_log_group()

        main_layout.addWidget(self.location_group)
        main_layout.addWidget(self.tab_widget)
        main_layout.addWidget(self.log_group)
        
        self.ws_thread = None
        self.food_cart = []
        self.supply_cart = []
        self.current_location = "ROOM_101"  # 기본값
        
        self.load_data()

    def create_location_group(self):
        """위치 선택 그룹 생성"""
        self.location_group = QGroupBox("현재 위치")
        layout = QHBoxLayout()
        
        self.location_combo = QComboBox()
        self.location_combo.addItems(["ROOM_101", "ROOM_102", "ROOM_201", "ROOM_202"])
        self.location_combo.currentTextChanged.connect(self.on_location_changed)
        
        layout.addWidget(QLabel("위치:"))
        layout.addWidget(self.location_combo)
        self.location_group.setLayout(layout)

    def create_food_order_tab(self):
        """음식 주문 탭 생성"""
        layout = QVBoxLayout(self.food_tab)
        
        # 메뉴 선택
        menu_group = QGroupBox("음식 메뉴")
        menu_layout = QVBoxLayout()
        
        self.food_menu_list = QListWidget()
        self.food_menu_list.itemDoubleClicked.connect(self.add_food_to_cart)
        
        cart_controls_layout = QHBoxLayout()
        self.food_quantity_spinbox = QSpinBox()
        self.food_quantity_spinbox.setRange(1, 10)
        add_food_button = QPushButton("카트에 담기")
        add_food_button.clicked.connect(self.add_food_to_cart_button)
        
        cart_controls_layout.addWidget(QLabel("수량:"))
        cart_controls_layout.addWidget(self.food_quantity_spinbox)
        cart_controls_layout.addWidget(add_food_button)

        menu_layout.addWidget(self.food_menu_list)
        menu_layout.addLayout(cart_controls_layout)
        menu_group.setLayout(menu_layout)
        
        # 장바구니
        cart_group = QGroupBox("음식 장바구니")
        cart_layout = QVBoxLayout()
        self.food_cart_list = QListWidget()
        
        order_button = QPushButton("음식 주문하기")
        order_button.clicked.connect(self.place_food_order)
        
        cart_layout.addWidget(self.food_cart_list)
        cart_layout.addWidget(order_button)
        cart_group.setLayout(cart_layout)
        
        layout.addWidget(menu_group)
        layout.addWidget(cart_group)

    def create_supply_order_tab(self):
        """비품 주문 탭 생성"""
        layout = QVBoxLayout(self.supply_tab)
        
        # 비품 선택
        supply_group = QGroupBox("비품 목록")
        supply_layout = QVBoxLayout()
        
        self.supply_menu_list = QListWidget()
        self.supply_menu_list.itemDoubleClicked.connect(self.add_supply_to_cart)
        
        supply_controls_layout = QHBoxLayout()
        self.supply_quantity_spinbox = QSpinBox()
        self.supply_quantity_spinbox.setRange(1, 10)
        add_supply_button = QPushButton("카트에 담기")
        add_supply_button.clicked.connect(self.add_supply_to_cart_button)
        
        supply_controls_layout.addWidget(QLabel("수량:"))
        supply_controls_layout.addWidget(self.supply_quantity_spinbox)
        supply_controls_layout.addWidget(add_supply_button)

        supply_layout.addWidget(self.supply_menu_list)
        supply_layout.addLayout(supply_controls_layout)
        supply_group.setLayout(supply_layout)
        
        # 장바구니
        supply_cart_group = QGroupBox("비품 장바구니")
        supply_cart_layout = QVBoxLayout()
        self.supply_cart_list = QListWidget()
        
        supply_order_button = QPushButton("비품 주문하기")
        supply_order_button.clicked.connect(self.place_supply_order)
        
        supply_cart_layout.addWidget(self.supply_cart_list)
        supply_cart_layout.addWidget(supply_order_button)
        supply_cart_group.setLayout(supply_cart_layout)
        
        layout.addWidget(supply_group)
        layout.addWidget(supply_cart_group)

    def create_call_tab(self):
        """호출 탭 생성"""
        layout = QVBoxLayout(self.call_tab)
        
        call_group = QGroupBox("직원 호출")
        call_layout = QVBoxLayout()
        
        call_info = QLabel("직원을 호출하여 도움을 요청할 수 있습니다.")
        call_button = QPushButton("직원 호출하기")
        call_button.clicked.connect(self.request_staff_call)
        
        call_layout.addWidget(call_info)
        call_layout.addWidget(call_button)
        call_group.setLayout(call_layout)
        
        layout.addWidget(call_group)

    def create_log_group(self):
        """로그 그룹 생성"""
        self.log_group = QGroupBox("알림 및 로그")
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

    def on_location_changed(self, location_name):
        """위치 변경 시 호출"""
        self.current_location = location_name
        self.log(f"[INFO] 위치가 {location_name}로 변경되었습니다.")
        self.connect_websocket(location_name)
        # 위치가 변경되면 메뉴를 다시 로드
        self.load_data()

    def load_data(self):
        """서버에서 메뉴와 위치 정보를 불러옵니다."""
        try:
            # 현재 선택된 위치
            location_name = self.location_combo.currentText()
            
            # 메뉴 로드 (GGUI용 API 사용, location_name 포함)
            response_menu = requests.post(f"{self.API_BASE_URL}/get_food_menu_ggui", json={
                "type": "request",
                "action": "get_food_menu",
                "payload": {"location_name": location_name}
            })
            response_menu.raise_for_status()
            menu_data = response_menu.json()
            print(f"[DEBUG] 서버 응답: {menu_data}")  # 디버깅용
            
            # GGUI API 응답 구조에 맞게 수정
            menu_items = menu_data.get('payload', {}).get('food_items', [])
            self.food_menu_list.clear()
            for item in menu_items:
                list_item = QListWidgetItem(f"{item['food_name']} - {item['price']}원")
                list_item.setData(Qt.ItemDataRole.UserRole, item)
                self.food_menu_list.addItem(list_item)
            self.log(f"[INFO] 메뉴를 성공적으로 불러왔습니다. ({len(menu_items)}개 항목)")
            
            # 비품 메뉴 로드 (GGUI용 API 사용, location_name 포함)
            response_supply = requests.post(f"{self.API_BASE_URL}/get_supply_menu_ggui", json={
                "type": "request",
                "action": "get_supply_menu",
                "payload": {"location_name": location_name}
            })
            response_supply.raise_for_status()
            supply_data = response_supply.json()
            
            supply_items = supply_data.get('payload', {}).get('supply_items', [])
            self.supply_menu_list.clear()
            for item in supply_items:
                list_item = QListWidgetItem(f"{item['supply_name']}")
                list_item.setData(Qt.ItemDataRole.UserRole, item)
                self.supply_menu_list.addItem(list_item)
            self.log(f"[INFO] 비품을 성공적으로 불러왔습니다. ({len(supply_items)}개 항목)")

        except requests.exceptions.RequestException as e:
            self.log(f"[ERROR] 메뉴/위치 로딩 실패: {e}")
        except Exception as e:
            self.log(f"[ERROR] 메뉴 처리 중 오류: {e}")
            import traceback
            self.log(f"[ERROR] 상세 오류: {traceback.format_exc()}")
            
    def add_food_to_cart(self, item):
        menu_item_data = item.data(Qt.ItemDataRole.UserRole)
        quantity = self.food_quantity_spinbox.value()
        # GGUI API 응답 구조에 맞게 수정
        cart_item = {
            'name': menu_item_data['food_name'],
            'price': menu_item_data['price'],
            'quantity': quantity
        }
        self.food_cart.append(cart_item)
        self.update_food_cart_display()

    def add_food_to_cart_button(self):
        selected_items = self.food_menu_list.selectedItems()
        if not selected_items:
            self.log("[WARN] 메뉴를 먼저 선택해주세요.")
            return
        self.add_food_to_cart(selected_items[0])

    def update_food_cart_display(self):
        self.food_cart_list.clear()
        for item in self.food_cart:
            self.food_cart_list.addItem(f"{item['name']} x{item['quantity']}")
            
    def place_food_order(self):
        if not self.food_cart:
            self.log("[WARN] 장바구니가 비어있습니다.")
            return
        
        location_name = self.location_combo.currentText()
        order_details = {"items": [{"name": item['name'], "quantity": item['quantity']} for item in self.food_cart]}
        
        payload = {
            "location_name": location_name,
            "task_type_name": "음식배송",
            "order_details": order_details
        }
        
        try:
            self.log(f"[DEBUG] 주문 요청 전송: {payload}")
            response = requests.post(f"{self.API_BASE_URL}/create_delivery_task_ggui", json={
                "type": "request",
                "action": "create_delivery_task",
                "payload": payload
            })
            self.log(f"[DEBUG] 응답 상태: {response.status_code}")
            response.raise_for_status()
            
            response_data = response.json()
            self.log(f"[DEBUG] 응답 데이터: {response_data}")
            
            # GGUI API 응답 구조에 맞게 수정
            task_info = response_data.get('payload', {})
            if task_info.get('success', False):
                self.log(f"[SUCCESS] 음식 주문이 성공적으로 생성되었습니다!")
                self.log(f"         작업 이름: {task_info.get('task_name')}")
                self.log(f"         예상 시간: {task_info.get('estimated_time', 30)}분")
                self.log(f"         생성 시간: {task_info.get('task_creation_time', 'N/A')}")
                self.food_cart.clear()
                self.update_food_cart_display()
                self.connect_websocket(location_name)
            else:
                self.log(f"[ERROR] 주문 실패: {task_info.get('error_message', '알 수 없는 오류')}")
                
        except requests.exceptions.RequestException as e:
            self.log(f"[ERROR] 주문 생성 요청 실패: {e}")
            import traceback
            self.log(f"[ERROR] 상세 오류: {traceback.format_exc()}")
        except Exception as e:
            self.log(f"[ERROR] 예상치 못한 오류: {e}")
            import traceback
            self.log(f"[ERROR] 상세 오류: {traceback.format_exc()}")

    def add_supply_to_cart(self, item):
        menu_item_data = item.data(Qt.ItemDataRole.UserRole)
        quantity = self.supply_quantity_spinbox.value()
        # GGUI API 응답 구조에 맞게 수정
        cart_item = {
            'name': menu_item_data['supply_name'],
            'quantity': quantity
        }
        self.supply_cart.append(cart_item)
        self.update_supply_cart_display()

    def add_supply_to_cart_button(self):
        selected_items = self.supply_menu_list.selectedItems()
        if not selected_items:
            self.log("[WARN] 메뉴를 먼저 선택해주세요.")
            return
        self.add_supply_to_cart(selected_items[0])

    def update_supply_cart_display(self):
        self.supply_cart_list.clear()
        for item in self.supply_cart:
            self.supply_cart_list.addItem(f"{item['name']} x{item['quantity']}")
            
    def place_supply_order(self):
        if not self.supply_cart:
            self.log("[WARN] 장바구니가 비어있습니다.")
            return
        
        location_name = self.location_combo.currentText()
        order_details = {"items": [{"name": item['name'], "quantity": item['quantity']} for item in self.supply_cart]}
        
        payload = {
            "location_name": location_name,
            "task_type_name": "비품배송",
            "order_details": order_details
        }
        
        try:
            self.log(f"[DEBUG] 비품 주문 요청 전송: {payload}")
            response = requests.post(f"{self.API_BASE_URL}/create_delivery_task_ggui", json={
                "type": "request",
                "action": "create_delivery_task",
                "payload": payload
            })
            self.log(f"[DEBUG] 응답 상태: {response.status_code}")
            response.raise_for_status()
            
            response_data = response.json()
            self.log(f"[DEBUG] 응답 데이터: {response_data}")
            
            # GGUI API 응답 구조에 맞게 수정
            task_info = response_data.get('payload', {})
            if task_info.get('success', False):
                self.log(f"[SUCCESS] 공급품 주문이 성공적으로 생성되었습니다!")
                self.log(f"         작업 이름: {task_info.get('task_name')}")
                self.log(f"         예상 시간: {task_info.get('estimated_time', 30)}분")
                self.log(f"         생성 시간: {task_info.get('task_creation_time', 'N/A')}")
                self.supply_cart.clear()
                self.update_supply_cart_display()
                self.connect_websocket(location_name)
            else:
                self.log(f"[ERROR] 주문 실패: {task_info.get('error_message', '알 수 없는 오류')}")
                
        except requests.exceptions.RequestException as e:
            self.log(f"[ERROR] 비품 주문 생성 요청 실패: {e}")
            import traceback
            self.log(f"[ERROR] 상세 오류: {traceback.format_exc()}")
        except Exception as e:
            self.log(f"[ERROR] 예상치 못한 오류: {e}")
            import traceback
            self.log(f"[ERROR] 상세 오류: {traceback.format_exc()}")

    def request_staff_call(self):
        location_name = self.location_combo.currentText()
        payload = {
            "location": location_name,
            "task_type": 2  # 호출 작업 타입
        }
        try:
            response = requests.post(f"{self.API_BASE_URL}/create_call_task", json={
                "type": "request",
                "action": "create_call_task",
                "payload": payload
            })
            response.raise_for_status()
            task_info = response.json().get('payload', {})
            self.log(f"[INFO] 직원 호출 작업이 성공적으로 생성되었습니다. (작업 이름: {task_info.get('task_name')})")
            self.connect_websocket(location_name)
        except requests.exceptions.RequestException as e:
            self.log(f"[ERROR] 직원 호출 작업 생성 실패: {e}")

    def connect_websocket(self, location_name):
        if self.ws_thread and self.ws_thread.is_alive():
            self.ws.close()
        
        ws_url = self.WS_URL_TEMPLATE.format(location_name=location_name)
        self.ws = websocket.WebSocketApp(
            ws_url,
            on_message=self.on_ws_message,
            on_error=self.on_ws_error,
            on_close=self.on_ws_close,
            on_open=self.on_ws_open
        )
        self.ws_thread = threading.Thread(target=self.ws.run_forever)
        self.ws_thread.daemon = True
        self.ws_thread.start()

    def on_ws_open(self, ws):
        self.log("[WS] 알림 수신을 위해 연결되었습니다.")

    def on_ws_message(self, ws, message):
        try:
            data = json.loads(message)
            event_type = data.get('type', '')
            event_action = data.get('action', '')
            
            if event_type == 'event':
                if event_action == 'call_request_acceptance':
                    payload = data.get('payload', {})
                    self.log(f"[WS] 🎉 호출 요청이 수락되었습니다!")
                    self.log(f"    작업명: {payload.get('task_name', 'N/A')}")
                    self.log(f"    예상 대기시간: {payload.get('estimated_wait_time', 'N/A')}분")
                    
                elif event_action == 'robot_arrival_completion':
                    payload = data.get('payload', {})
                    self.log(f"[WS] 🤖 로봇이 도착했습니다!")
                    self.log(f"    작업명: {payload.get('task_name', 'N/A')}")
                    self.log(f"    위치: {payload.get('location_name', 'N/A')}")
                    
                elif event_action == 'delivery_completion':
                    payload = data.get('payload', {})
                    self.log(f"[WS] 📦 배송이 완료되었습니다!")
                    self.log(f"    작업명: {payload.get('task_name', 'N/A')}")
                    self.log(f"    배송지: {payload.get('request_location', 'N/A')}")
                    
                elif event_action == 'task_timeout_return':
                    payload = data.get('payload', {})
                    self.log(f"[WS] ⏰ 시간 초과로 로봇이 복귀합니다.")
                    self.log(f"    작업명: {payload.get('task_name', 'N/A')}")
                    self.log(f"    위치: {payload.get('location_name', 'N/A')}")
                    
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
    gui = GGUI()
    gui.show()
    sys.exit(app.exec())
