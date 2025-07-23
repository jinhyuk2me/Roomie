# screen_manager.py

from PyQt6.QtWidgets import QWidget
from .ui_loader import load_ui
from .task_type import TaskType
from .task_state import DeliveryState
from enum import Enum


class ScreenManager:
    def __init__(self, node):
        self.node = node
        self.window = QWidget()
        self.window.setWindowTitle("Roomie RGUI")

        # 기본 대기 화면 로드
        load_ui(self.window, "ui/common/TOUCH_SCREEN.ui")

        self.window.show()

        self.current_task_type: TaskType | None = None
        self.current_state: Enum | None = None

        # (TaskType, 상태 enum) → .ui 경로 매핑
        self.ui_map = {
            # Delivery 작업
            (TaskType.DELIVERY, DeliveryState.PICKUP_MOVING):           "ui/delivery/DELI_1_PICKUP_MOVING.ui",
            (TaskType.DELIVERY, DeliveryState.PICKUP_ARRIVED):          "ui/delivery/DELI_2_PICKUP_ARRIVAL.ui",
            (TaskType.DELIVERY, DeliveryState.CHECKING_ORDER):          "ui/delivery/DELI_3_STAFF_ORDER_CONFIRM.ui",
            (TaskType.DELIVERY, DeliveryState.PICKUP_DRAWER_CONTROL):   "ui/delivery/DELI_4_PICKUP_DRAWER_CONTROL.ui",
            (TaskType.DELIVERY, DeliveryState.DELIVERY_MOVING):         "ui/delivery/DELI_5_DELIVERY_MOVING.ui",
            (TaskType.DELIVERY, DeliveryState.DELIVERY_ARRIVED):        "ui/delivery/DELI_6_DELIVERY_ARRIVAL.ui",
            (TaskType.DELIVERY, DeliveryState.DELIVERY_DRAWER_CONTROL): "ui/delivery/DELI_7_DELIVERY_DRAWER_CONTROL.ui",
            (TaskType.DELIVERY, DeliveryState.THANK_YOU):               "ui/delivery/DELI_8_THANK_YOU.ui",

            # TODO: CALL, GUIDE, RETURN 등 TaskType 추가 예정
        }

    def set_task_context(self, task_type: TaskType):
        self.current_task_type = task_type
        self.node.get_logger().info(f"작업 타입 설정됨: {task_type.name}")

    def set_state(self, state_enum: Enum):
        if self.current_task_type is None:
            self.node.get_logger().warn("작업(TaskType)이 설정되지 않았습니다.")
            return

        key = (self.current_task_type, state_enum)
        ui_path = self.ui_map.get(key)

        if not ui_path:
            self.node.get_logger().warn(
                f"정의되지 않은 상태 전환: {self.current_task_type.name} + {state_enum.name}"
            )
            return

        self.current_state = state_enum
        load_ui(self.window, ui_path)
        self.node.get_logger().info(
            f"화면 전환: {self.current_task_type.name} + {state_enum.name} → {ui_path}"
        )
