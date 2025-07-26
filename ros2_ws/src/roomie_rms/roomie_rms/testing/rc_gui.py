#!/usr/bin/env python3
"""
로봇 컨트롤러(RC) 시뮬레이터 - 통합 버전
ROS2 노드와 PyQt6 GUI가 통합된 RC 시뮬레이터입니다.
"""

import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse
from rclpy.executors import MultiThreadedExecutor
import threading
import time

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QComboBox, QPushButton, QLineEdit, QTextEdit, QSlider, QGroupBox, QFormLayout
)
from PyQt6.QtCore import QObject, pyqtSignal, Qt, QMetaObject, Q_ARG

from roomie_msgs.msg import RobotState, Arrival, BatteryStatus, PickupCompleted, DeliveryCompleted
from roomie_msgs.action import PerformTask


class RCSimulatorGUI(QMainWindow):
    """
    로봇 컨트롤러(RC) 시뮬레이터 GUI
    - 로봇의 상태를 시각적으로 보여주고, 수동으로 제어할 수 있습니다.
    - 실제 로봇의 ROS2 노드(rc_node)와 연동됩니다.
    """

    # GUI에서 ROS2 노드로 보내는 신호 정의
    signal_robot_state_changed = pyqtSignal(str)
    signal_battery_level_changed = pyqtSignal(int)
    
    # ROS2 노드에서 GUI로 보내는 신호 정의 (스레드 안전성을 위해)
    signal_log_update = pyqtSignal(str)
    signal_task_update = pyqtSignal(int, str)
    signal_task_status_update = pyqtSignal(bool) # is_task_active
    signal_arrival_status_update = pyqtSignal(bool) # is_at_current_destination
    signal_pickup_status_update = pyqtSignal(bool) # has_picked_up

    def __init__(self):
        super().__init__()
        self.worker = None

        # --- 상태 변수 초기화 ---
        self.is_task_active = False
        self.is_at_current_destination = False
        self.has_picked_up = False

        self.setWindowTitle("🤖 로봇 컨트롤러(RC) 시뮬레이터")
        self.setGeometry(100, 100, 500, 600)

        # --- 메인 위젯 및 레이아웃 ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # --- 위젯 생성 ---
        self.create_status_group()
        self.create_task_group()
        self.create_event_group()
        self.create_log_group()

        # --- 레이아웃에 그룹 추가 ---
        main_layout.addWidget(self.status_group)
        main_layout.addWidget(self.task_group)
        main_layout.addWidget(self.event_group)
        main_layout.addWidget(self.log_group)
        
        # --- 시그널 연결 (스레드 안전성을 위해) ---
        self.signal_log_update.connect(self.update_log)
        self.signal_task_update.connect(self.update_task_info)
        self.signal_task_status_update.connect(self.on_task_status_update)
        self.signal_arrival_status_update.connect(self.on_arrival_status_update)
        self.signal_pickup_status_update.connect(self.on_pickup_status_update)

    def create_status_group(self):
        """로봇 상태 정보 그룹 생성"""
        self.status_group = QGroupBox("로봇 상태")
        layout = QFormLayout()

        self.robot_id_label = QLabel("로봇 ID: 1 (고정)")
        self.robot_state_combo = QComboBox()
        self.robot_state_combo.addItems(["작업 가능", "작업 중", "충전 중", "에러"])
        
        self.battery_slider = QSlider(Qt.Orientation.Horizontal)
        self.battery_slider.setRange(0, 100)
        self.battery_slider.setValue(100)
        self.battery_label = QLabel(f"{self.battery_slider.value()}%")

        layout.addRow("ID:", self.robot_id_label)
        layout.addRow("상태 변경:", self.robot_state_combo)
        
        battery_layout = QHBoxLayout()
        battery_layout.addWidget(self.battery_slider)
        battery_layout.addWidget(self.battery_label)
        layout.addRow("배터리:", battery_layout)
        
        self.status_group.setLayout(layout)
        
        # --- 시그널 연결 ---
        self.robot_state_combo.currentTextChanged.connect(self.signal_robot_state_changed.emit)
        self.battery_slider.valueChanged.connect(self.on_battery_slider_changed)

    def create_task_group(self):
        """현재 작업 정보 그룹 생성"""
        self.task_group = QGroupBox("현재 작업 정보")
        layout = QFormLayout()

        self.task_id_label = QLineEdit("대기 중")
        self.task_id_label.setReadOnly(True)
        self.order_info_label = QTextEdit()
        self.order_info_label.setReadOnly(True)

        layout.addRow("작업 ID:", self.task_id_label)
        layout.addRow("주문 정보:", self.order_info_label)
        self.task_group.setLayout(layout)

    def create_event_group(self):
        """이벤트 발생 그룹 생성"""
        self.event_group = QGroupBox("수동 이벤트 발생")
        layout = QHBoxLayout()

        self.arrival_button = QPushButton("목적지 도착")
        self.pickup_button = QPushButton("픽업 완료")
        self.delivery_button = QPushButton("수령 완료")

        self.arrival_button.clicked.connect(self.publish_arrival_event)
        self.pickup_button.clicked.connect(self.publish_pickup_completed_event)
        self.delivery_button.clicked.connect(self.publish_delivery_completed_event)

        layout.addWidget(self.arrival_button)
        layout.addWidget(self.pickup_button)
        layout.addWidget(self.delivery_button)
        
        self.event_group.setLayout(layout)

        # 초기 버튼 상태 설정
        self.update_button_states()

    def create_log_group(self):
        """로그 정보 그룹 생성"""
        self.log_group = QGroupBox("통신 로그")
        layout = QVBoxLayout()
        self.log_text_edit = QTextEdit()
        self.log_text_edit.setReadOnly(True)
        layout.addWidget(self.log_text_edit)
        self.log_group.setLayout(layout)

    def update_button_states(self):
        """작업 상태에 따라 버튼의 활성화/비활성화 상태를 업데이트합니다."""
        # '도착' 버튼: 작업 중이고, 아직 현재 목적지에 도착하지 않았을 때 활성화
        self.arrival_button.setEnabled(self.is_task_active and not self.is_at_current_destination)
        # '픽업' 버튼: 작업 중이고, 목적지에 도착했으며, 아직 픽업하지 않았을 때 활성화
        self.pickup_button.setEnabled(self.is_task_active and self.is_at_current_destination and not self.has_picked_up)
        # '수령' 버튼: 작업 중이고, 목적지에 도착했으며, 픽업을 완료했을 때 활성화
        self.delivery_button.setEnabled(self.is_task_active and self.is_at_current_destination and self.has_picked_up)


    def update_log(self, message):
        """로그 메시지 추가 (메인 스레드에서만 호출됨)"""
        try:
            self.log_text_edit.append(message)
        except Exception as e:
            # GUI가 이미 파괴된 경우
            print(f"로그 업데이트 실패: {e}")
        
    def update_task_info(self, task_id, order_info):
        """작업 정보 업데이트 (메인 스레드에서만 호출됨)"""
        try:
            self.task_id_label.setText(str(task_id))
            self.order_info_label.setText(order_info)
            self.update_log(f"[INFO] 새 작업 할당됨: {task_id}")
        except Exception as e:
            print(f"작업 정보 업데이트 실패: {e}")

    def on_battery_slider_changed(self, value):
        """배터리 슬라이더 값 변경 시 호출"""
        self.battery_label.setText(f"{value}%")
        self.signal_battery_level_changed.emit(value)

    def on_task_status_update(self, is_active):
        self.is_task_active = is_active
        if not is_active: # 작업이 끝나면 모든 상태 초기화
            self.task_id_label.setText("N/A")
            self.order_info_label.setText("N/A")
            self.is_at_current_destination = False
            self.has_picked_up = False
        self.update_button_states()

    def on_arrival_status_update(self, is_at_destination):
        self.is_at_current_destination = is_at_destination
        self.update_button_states()

    def on_pickup_status_update(self, has_picked_up):
        self.has_picked_up = has_picked_up
        self.update_button_states()

    def publish_arrival_event(self):
        if self.worker:
            self.worker.publish_arrival_event()

    def publish_pickup_completed_event(self):
        if self.worker:
            self.worker.publish_pickup_completed_event()
    
    def publish_delivery_completed_event(self):
        if self.worker:
            self.worker.publish_delivery_completed_event()


class RosNodeWorker(Node):
    """RC 시뮬레이터의 ROS2 로직을 담당하는 워커 클래스"""
    
    def __init__(self, gui_signals):
        # Node 초기화
        super().__init__('rc_simulator_node')
        
        # GUI 시그널들 (스레드 안전성을 위해)
        self.gui_signals = gui_signals
        
        # --- 퍼블리셔 ---
        self.robot_state_pub = self.create_publisher(RobotState, '/roomie/status/robot_state', 10)
        self.arrival_pub = self.create_publisher(Arrival, '/roomie/event/arrival', 10)
        self.battery_pub = self.create_publisher(BatteryStatus, '/roomie/status/battery_status', 10)
        self.pickup_pub = self.create_publisher(PickupCompleted, '/roomie/event/pickup_completed', 10)
        self.delivery_pub = self.create_publisher(DeliveryCompleted, '/roomie/event/delivery_completed', 10)

        # --- 액션 서버 ---
        self.perform_task_server = ActionServer(
            self,
            PerformTask,
            '/roomie/action/perform_task',
            self.execute_task_callback
        )
        
        self.current_task_goal = None
        if self.gui_signals:
            self.gui_signals.signal_log_update.emit("[INFO] RC 시뮬레이터 노드 초기화 완료")

    def execute_task_callback(self, goal_handle):
        """PerformTask 액션 요청을 받았을 때 실행되는 콜백"""
        self.current_task_goal = goal_handle.request
        if self.gui_signals:
            self.gui_signals.signal_log_update.emit(f"[ACTION] 작업 요청 수신: Task ID {self.current_task_goal.task_id}")
            self.gui_signals.signal_task_update.emit(self.current_task_goal.task_id, self.current_task_goal.order_info)
            # 새 작업 시작 시 상태 업데이트
            self.gui_signals.signal_task_status_update.emit(True)
            self.gui_signals.signal_arrival_status_update.emit(False)
            self.gui_signals.signal_pickup_status_update.emit(False)
        
        goal_handle.succeed()
        
        result = PerformTask.Result()
        result.task_id = self.current_task_goal.task_id
        result.success = True
        return result

    # --- GUI 콜백을 받아 ROS2 메시지를 발행하는 메서드 ---
    def publish_robot_state(self, state_str):
        state_map = {"작업 가능": 1, "작업 중": 2, "충전 중": 4, "에러": 7}
        msg = RobotState()
        msg.robot_id = 1
        msg.robot_state_id = state_map.get(state_str, 1)
        self.robot_state_pub.publish(msg)
        if self.gui_signals:
            self.gui_signals.signal_log_update.emit(f"[PUB] 로봇 상태 발행: {state_str}")

    def publish_battery_level(self, level):
        msg = BatteryStatus()
        msg.robot_id = 1
        msg.battery_level = float(level)
        self.battery_pub.publish(msg)
        if self.gui_signals:
            self.gui_signals.signal_log_update.emit(f"[PUB] 배터리 상태 발행: {level}%")

    def publish_arrival_event(self):
        if not self.current_task_goal:
            if self.gui_signals:
                self.gui_signals.signal_log_update.emit("[WARN] 진행 중인 작업이 없어 도착 이벤트를 발행할 수 없습니다.")
            return
            
        # 픽업 완료 여부에 따라 목적지 결정
        if not self.gui_signals.has_picked_up:
            location_id = self.current_task_goal.pickup_location_id
            if self.gui_signals:
                self.gui_signals.signal_log_update.emit(f"[PUB] 픽업 장소 도착 이벤트 발행 (Loc: {location_id})")
        else:
            location_id = self.current_task_goal.target_location_id
            if self.gui_signals:
                self.gui_signals.signal_log_update.emit(f"[PUB] 최종 목적지 도착 이벤트 발행 (Loc: {location_id})")

        msg = Arrival()
        msg.task_id = self.current_task_goal.task_id
        msg.robot_id = 1
        msg.location_id = location_id
        self.arrival_pub.publish(msg)

        # 상태 업데이트: 현재 목적지에 도착했음
        self.gui_signals.signal_arrival_status_update.emit(True)

    def publish_pickup_completed_event(self):
        if not self.current_task_goal:
            if self.gui_signals:
                self.gui_signals.signal_log_update.emit("[WARN] 진행 중인 작업이 없어 픽업 완료 이벤트를 발행할 수 없습니다.")
            return
        msg = PickupCompleted()
        msg.task_id = self.current_task_goal.task_id
        msg.robot_id = 1
        self.pickup_pub.publish(msg)
        if self.gui_signals:
            self.gui_signals.signal_log_update.emit(f"[PUB] 픽업 완료 이벤트 발행")
        
        # 상태 업데이트: 픽업 완료, 이제 다음 목적지로 가야 하므로 '도착' 상태 해제
        self.gui_signals.signal_arrival_status_update.emit(False)
        self.gui_signals.signal_pickup_status_update.emit(True)

    def publish_delivery_completed_event(self):
        if not self.current_task_goal:
            if self.gui_signals:
                self.gui_signals.signal_log_update.emit("[WARN] 진행 중인 작업이 없어 배송 완료 이벤트를 발행할 수 없습니다.")
            return
        msg = DeliveryCompleted()
        msg.task_id = self.current_task_goal.task_id
        msg.robot_id = 1
        self.delivery_pub.publish(msg)
        if self.gui_signals:
            self.gui_signals.signal_log_update.emit(f"[PUB] 배송 완료 이벤트 발행")
        self.current_task_goal = None # 작업 완료
        # 작업 완료 후 모든 상태 초기화
        self.gui_signals.signal_task_status_update.emit(False)


def main(args=None):
    """메인 함수 - RC 시뮬레이터 실행"""
    rclpy.init(args=args)
    
    app = QApplication(sys.argv)
    gui = RCSimulatorGUI()
    
    # --- ROS2-GUI 연결 ---
    # GUI 시그널을 worker에 전달 (스레드 안전성을 위해)
    gui.worker = RosNodeWorker(gui) # Pass self (GUI) as signals object
    
    # 시그널 연결
    gui.signal_robot_state_changed.connect(gui.worker.publish_robot_state)
    gui.signal_battery_level_changed.connect(gui.worker.publish_battery_level)
    
    # --- ROS2 노드를 별도 스레드에서 실행 ---
    executor = MultiThreadedExecutor()
    executor.add_node(gui.worker)
    thread = threading.Thread(target=executor.spin)
    thread.daemon = True
    thread.start()
    
    gui.show()
    
    try:
        sys.exit(app.exec())
    finally:
        gui.worker.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main() 