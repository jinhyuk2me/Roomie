import tkinter as tk
from tkinter import ttk, messagebox
import asyncio
import websockets
import requests
import json
import threading
from datetime import datetime
from config import RMS_WS_URL, RMS_HTTP_URL, FOOD_TYPES

class StaffGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ROOMIE")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")
        
        # 데이터 저장
        self.orders = {}  # task_id: order_data
        self.ready_orders = {}  # 준비완료된 주문들
        self.selected_order = None
        
        # WebSocket 연결 상태
        self.websocket = None
        self.ws_connected = False
        
        self.setup_ui()
        self.start_websocket_connection()
    
    def setup_ui(self):
        # 메인 프레임
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 헤더
        header_frame = tk.Frame(main_frame, bg="#2c3e50")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = tk.Label(header_frame, text="ROOMIE", font=("Arial", 24, "bold"), 
                              fg="white", bg="#2c3e50")
        title_label.pack(side=tk.LEFT)
        
        restaurant_label = tk.Label(header_frame, text="Restaurant", font=("Arial", 16), 
                                   fg="#3498db", bg="#2c3e50")
        restaurant_label.pack(side=tk.RIGHT)
        
        # 탭 노트북
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # 신청품목 탭
        self.orders_frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.orders_frame, text="신청품목")
        
        # 준비완료 탭  
        self.ready_frame = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.ready_frame, text="준비완료")
        
        self.setup_orders_tab()
        self.setup_ready_tab()
    
    def setup_orders_tab(self):
        # 왼쪽 주문 목록
        left_frame = tk.Frame(self.orders_frame, bg="#34495e", width=250)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        left_frame.pack_propagate(False)
        
        # 주문 목록 헤더
        orders_header = tk.Label(left_frame, text="신청품목", font=("Arial", 14, "bold"),
                                fg="white", bg="#34495e")
        orders_header.pack(pady=10)
        
        # 주문 리스트박스
        self.orders_listbox = tk.Listbox(left_frame, font=("Arial", 10), 
                                        bg="white", selectmode=tk.SINGLE)
        self.orders_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        self.orders_listbox.bind('<<ListboxSelect>>', self.on_order_select)
        
        # 오른쪽 상세정보
        right_frame = tk.Frame(self.orders_frame, bg="white")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 주문 번호 표시
        self.order_title = tk.Label(right_frame, text="주문 #", font=("Arial", 18, "bold"),
                                   bg="white")
        self.order_title.pack(pady=20)
        
        # 주문정보 섹션
        order_info_frame = tk.Frame(right_frame, bg="white")
        order_info_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(order_info_frame, text="주문정보", font=("Arial", 12, "bold"),
                bg="white").pack(anchor=tk.W)
        
        # 구분선
        separator1 = tk.Frame(order_info_frame, height=1, bg="#bdc3c7")
        separator1.pack(fill=tk.X, pady=5)
        
        self.order_details_frame = tk.Frame(order_info_frame, bg="white")
        self.order_details_frame.pack(fill=tk.X, pady=10)
        
        # 배송정보 섹션
        delivery_info_frame = tk.Frame(right_frame, bg="white")
        delivery_info_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(delivery_info_frame, text="배송정보", font=("Arial", 12, "bold"),
                bg="white").pack(anchor=tk.W)
        
        # 구분선
        separator2 = tk.Frame(delivery_info_frame, height=1, bg="#bdc3c7")
        separator2.pack(fill=tk.X, pady=5)
        
        self.delivery_info_frame = tk.Frame(delivery_info_frame, bg="white")
        self.delivery_info_frame.pack(fill=tk.X, pady=10)
        
        # 준비완료 버튼
        self.ready_button = tk.Button(right_frame, text="준비완료", 
                                     font=("Arial", 14, "bold"), bg="#3498db", 
                                     fg="white", pady=10, command=self.mark_ready)
        self.ready_button.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)
        
        self.clear_order_details()
    
    def setup_ready_tab(self):
        # 준비완료된 주문들 표시
        self.ready_listbox = tk.Listbox(self.ready_frame, font=("Arial", 12))
        self.ready_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def clear_order_details(self):
        self.order_title.config(text="주문을 선택하세요")
        
        # 기존 위젯들 제거
        for widget in self.order_details_frame.winfo_children():
            widget.destroy()
        for widget in self.delivery_info_frame.winfo_children():
            widget.destroy()
            
        self.ready_button.config(state="disabled")
    
    def display_order_details(self, order_data):
        self.clear_order_details()
        
        task_id = order_data['task_id']
        self.order_title.config(text=f"주문 #{task_id}")
        
        # 주문 항목들 표시
        items = order_data['order_details']['items']
        total_amount = 0
        
        for item in items:
            item_frame = tk.Frame(self.order_details_frame, bg="white")
            item_frame.pack(fill=tk.X, pady=2)
            
            name_label = tk.Label(item_frame, text=item['name'], 
                                 font=("Arial", 11), bg="white")
            name_label.pack(side=tk.LEFT)
            
            quantity_label = tk.Label(item_frame, text=str(item['quantity']), 
                                     font=("Arial", 11), bg="white")
            quantity_label.pack(side=tk.RIGHT, padx=(0, 80))
            
            price_label = tk.Label(item_frame, text=f"{item['price']:,}원", 
                                  font=("Arial", 11), bg="white")
            price_label.pack(side=tk.RIGHT)
            
            total_amount += item['price'] * item['quantity']
        
        # 총액 표시
        total_frame = tk.Frame(self.order_details_frame, bg="white")
        total_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(total_frame, text=f"총 {len(items)}개", font=("Arial", 11, "bold"), 
                bg="white").pack(side=tk.RIGHT, padx=(0, 80))
        tk.Label(total_frame, text=f"{total_amount:,}원", font=("Arial", 11, "bold"), 
                bg="white").pack(side=tk.RIGHT)
        
        # 배송정보 표시
        room_frame = tk.Frame(self.delivery_info_frame, bg="white")
        room_frame.pack(fill=tk.X, pady=2)
        tk.Label(room_frame, text="호실", font=("Arial", 11), bg="white").pack(side=tk.LEFT)
        tk.Label(room_frame, text=order_data['request_location'], 
                font=("Arial", 11), bg="white").pack(side=tk.RIGHT)
        
        # 현재 시간으로 주문 시간 표시 (실제로는 서버에서 받아야 함)
        time_frame = tk.Frame(self.delivery_info_frame, bg="white")
        time_frame.pack(fill=tk.X, pady=2)
        tk.Label(time_frame, text="주문 일시", font=("Arial", 11), bg="white").pack(side=tk.LEFT)
        current_time = datetime.now().strftime("%Y.%m.%d %H:%M")
        tk.Label(time_frame, text=current_time, font=("Arial", 11), bg="white").pack(side=tk.RIGHT)
        
        self.ready_button.config(state="normal")
    
    def on_order_select(self, event):
        selection = self.orders_listbox.curselection()
        if selection:
            index = selection[0]
            order_text = self.orders_listbox.get(index)
            # 주문 번호 추출 (주문 #TASK_001 11:42 형식에서)
            task_id = order_text.split()[1].replace('#', '')
            if task_id in self.orders:
                self.selected_order = task_id
                self.display_order_details(self.orders[task_id])
    
    def add_new_order(self, order_data):
        """새 주문 추가"""
        task_id = order_data['task_id']
        self.orders[task_id] = order_data
        
        # 주문 시간 (현재 시간으로 설정)
        current_time = datetime.now().strftime("%H:%M")
        order_text = f"주문 #{task_id} {current_time}"
        
        self.orders_listbox.insert(tk.END, order_text)
        
        # 알림 표시
        messagebox.showinfo("새 주문", f"새로운 주문이 접수되었습니다!\n주문 번호: {task_id}")
    
    def mark_ready(self):
        """준비완료 처리"""
        if not self.selected_order:
            return
            
        task_id = self.selected_order
        
        try:
            # HTTP 요청으로 상태 변경
            response = requests.post(
                f"{RMS_HTTP_URL}/food_order_status_change",
                json={
                    "type": "request",
                    "action": "food_order_status_change", 
                    "payload": {
                        "task_id": task_id
                    }
                },
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('payload', {}).get('status_changed') == 'food_ready':
                    # 성공적으로 상태 변경됨
                    self.move_to_ready(task_id)
                    messagebox.showinfo("완료", f"주문 #{task_id}이 준비완료되었습니다!")
                else:
                    messagebox.showerror("오류", "상태 변경에 실패했습니다.")
            else:
                messagebox.showerror("오류", f"서버 오류: {response.status_code}")
                
        except requests.RequestException as e:
            messagebox.showerror("오류", f"통신 오류: {str(e)}")
    
    def move_to_ready(self, task_id):
        """주문을 준비완료 탭으로 이동"""
        if task_id in self.orders:
            # 준비완료 목록에 추가
            order_data = self.orders[task_id]
            self.ready_orders[task_id] = order_data
            
            # 준비완료 리스트박스에 추가
            self.ready_listbox.insert(tk.END, f"주문 #{task_id} - 준비완료")
            
            # 신청품목에서 제거
            del self.orders[task_id]
            
            # 리스트박스에서 제거
            for i in range(self.orders_listbox.size()):
                if task_id in self.orders_listbox.get(i):
                    self.orders_listbox.delete(i)
                    break
            
            # 선택 해제
            self.selected_order = None
            self.clear_order_details()
    
    def show_robot_arrival(self, task_id, robot_id):
        """로봇 도착 알림"""
        # 팝업 창 생성
        popup = tk.Toplevel(self.root)
        popup.title(f"{robot_id} 도착")
        popup.geometry("400x300")
        popup.configure(bg="white")
        
        # 팝업을 화면 중앙에 위치
        popup.transient(self.root)
        popup.grab_set()
        
        # 창을 화면 중앙에 배치
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 200
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 150
        popup.geometry(f"+{x}+{y}")
        
        # 메인 프레임
        main_frame = tk.Frame(popup, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 로봇 아이콘 (텍스트로 표현)
        icon_label = tk.Label(main_frame, text="🤖", font=("Arial", 48), 
                             bg="white", fg="#3498db")
        icon_label.pack(pady=(20, 10))
        
        # 제목
        title_label = tk.Label(main_frame, text=f"{robot_id} 도착", 
                              font=("Arial", 20, "bold"), 
                              bg="white", fg="#2c3e50")
        title_label.pack(pady=(0, 10))
        
        # 메시지
        message_label = tk.Label(main_frame, 
                                text=f"{robot_id}이 픽업 장소에 도착했습니다.",
                                font=("Arial", 12), 
                                bg="white", fg="#7f8c8d",
                                wraplength=300)
        message_label.pack(pady=(0, 20))
        
        # 주문 정보 (해당 주문이 있는 경우)
        if task_id in self.orders:
            order_info = self.orders[task_id]
            order_text = f"주문 #{task_id}"
            if 'request_location' in order_info:
                order_text += f" ({order_info['request_location']})"
            
            order_label = tk.Label(main_frame, text=order_text,
                                  font=("Arial", 11, "bold"),
                                  bg="white", fg="#e74c3c")
            order_label.pack(pady=(0, 20))
        
        # 확인 버튼
        ok_button = tk.Button(main_frame, text="확인", 
                             font=("Arial", 12, "bold"),
                             bg="#3498db", fg="white",
                             relief=tk.FLAT, padx=30, pady=8,
                             command=popup.destroy)
        ok_button.pack(pady=(0, 10))
        
        # 5초 후 자동으로 닫기
        popup.after(5000, popup.destroy)
    
    def start_websocket_connection(self):
        """WebSocket 연결 시작"""
        def run_websocket():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.websocket_handler())
        
        ws_thread = threading.Thread(target=run_websocket, daemon=True)
        ws_thread.start()
    
    async def websocket_handler(self):
        """WebSocket 메시지 처리"""
        while True:
            try:
                async with websockets.connect(RMS_WS_URL) as websocket:
                    self.websocket = websocket
                    self.ws_connected = True
                    print("WebSocket 연결됨")
                    
                    async for message in websocket:
                        try:
                            data = json.loads(message)
                            self.root.after(0, self.handle_websocket_message, data)
                        except json.JSONDecodeError:
                            print(f"잘못된 JSON 메시지: {message}")
                            
            except Exception as e:
                print(f"WebSocket 오류: {e}")
                self.ws_connected = False
                await asyncio.sleep(5)  # 5초 후 재연결 시도
    
    def handle_websocket_message(self, data):
        """WebSocket 메시지 처리 (메인 스레드에서 실행)"""
        message_type = data.get('type')
        action = data.get('action')
        payload = data.get('payload', {})
        
        if message_type == 'event':
            if action == 'food_order_creation':
                # 새 주문 접수
                self.add_new_order(payload)
            elif action == 'food_pickup_arrival':
                # 로봇 도착
                task_id = payload.get('task_id')
                robot_id = payload.get('robot_id')
                self.show_robot_arrival(task_id, robot_id)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = StaffGUI()
    app.run() 