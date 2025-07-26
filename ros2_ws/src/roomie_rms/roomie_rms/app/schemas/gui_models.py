from pydantic import BaseModel, Field, field_serializer
from typing import List, Optional, Dict, Any
from datetime import datetime, date

# --- Common Models ---
class BasePayload(BaseModel):
    location_name: Optional[str] = None

class BaseResponse(BaseModel):
    success: bool = True
    message: Optional[str] = None

class OrderItem(BaseModel):
    name: str
    price: Optional[int] = None
    quantity: int

# GUI <=> 서버 기본 통신 모델
class SimpleRequest(BaseModel):
    command: str
    data: dict

class SimpleResponse(BaseModel):
    status: str
    message: str

# 음식 메뉴 아이템 모델
class FoodItem(BaseModel):
    id: int
    name: str
    price: int
    image_path: str

# 물품 메뉴 아이템 모델  
class SupplyItem(BaseModel):
    id: int
    name: str
    image_path: str

# 위치 아이템 모델
class LocationItem(BaseModel):
    id: int
    name: str

# --- Get Food Menu ---
class GetFoodMenuRequest(BaseModel):
    payload: BasePayload

class GetFoodMenuResponsePayload(BasePayload):
    menu_items: List[FoodItem]
    estimated_time: int

class GetFoodMenuResponse(BaseModel):
    status: str
    message: str
    payload: GetFoodMenuResponsePayload

# --- Get Supply Menu ---
class GetSupplyMenuRequest(BaseModel):
    payload: BasePayload

class GetSupplyMenuResponsePayload(BasePayload):
    menu_items: List[SupplyItem]
    estimated_time: int

class GetSupplyMenuResponse(BaseModel):
    status: str
    message: str
    payload: GetSupplyMenuResponsePayload

# --- Get Locations ---
class GetLocationsRequest(BaseModel):
    payload: BasePayload

class GetLocationsResponsePayload(BasePayload):
    locations: List[LocationItem]

class GetLocationsResponse(BaseModel):
    status: str
    message: str
    payload: GetLocationsResponsePayload

# --- Create Delivery Task ---
class CreateDeliveryTaskRequestPayload(BasePayload):
    location_name: str
    task_type_name: str
    order_details: Dict[str, List[OrderItem]]

class CreateDeliveryTaskRequest(BaseModel):
    payload: CreateDeliveryTaskRequestPayload

class CreateDeliveryTaskResponsePayload(BasePayload):
    task_id: int
    order_id: int
    success: bool = True
    message: str = "주문이 성공적으로 생성되었습니다."
    estimated_time: int = 30  # 기본 예상 시간 (분)
    task_creation_time: str

class CreateDeliveryTaskResponse(BaseResponse):
    payload: CreateDeliveryTaskResponsePayload

# --- SGUI WebSocket Event Models ---

# SGUI 음식 주문 발생 알림
class FoodOrderCreationEventPayload(BaseModel):
    task_id: str
    location: str
    order_details: List[OrderItem]

class FoodOrderCreationEvent(BaseModel):
    type: str = "event"
    action: str = "food_order_creation"
    payload: FoodOrderCreationEventPayload

# SGUI 비품 요청 발생 알림
class SupplyOrderCreationEventPayload(BaseModel):
    task_id: str
    location: str
    order_details: List[Dict[str, Any]]  # name, quantity (no price for supplies)

class SupplyOrderCreationEvent(BaseModel):
    type: str = "event"
    action: str = "supply_order_creation"
    payload: SupplyOrderCreationEventPayload

# SGUI 음식 픽업 장소 도착 알림
class FoodPickupArrivalEventPayload(BaseModel):
    task_id: str
    robot_id: str

class FoodPickupArrivalEvent(BaseModel):
    type: str = "event"
    action: str = "food_pickup_arrival"
    payload: FoodPickupArrivalEventPayload

# SGUI 비품 픽업 장소 도착 알림
class SupplyPickupArrivalEventPayload(BaseModel):
    task_id: str
    robot_id: str

class SupplyPickupArrivalEvent(BaseModel):
    type: str = "event"
    action: str = "supply_pickup_arrival"
    payload: SupplyPickupArrivalEventPayload

# SGUI 음식 주문 작업 상태 전환 요청/응답
class FoodOrderStatusChangeRequestPayload(BaseModel):
    task_id: str

class FoodOrderStatusChangeRequest(BaseModel):
    type: str = "request"
    action: str = "food_order_status_change"
    payload: FoodOrderStatusChangeRequestPayload

class FoodOrderStatusChangeResponsePayload(BaseModel):
    task_id: str
    status_changed: str

class FoodOrderStatusChangeResponse(BaseModel):
    type: str = "response"
    action: str = "food_order_status_change"
    payload: FoodOrderStatusChangeResponsePayload

# --- GGUI WebSocket Event Models ---

# GGUI 호출 수락 알림
class CallRequestAcceptanceEventPayload(BaseModel):
    task_name: str
    estimated_wait_time: int

class CallRequestAcceptanceEvent(BaseModel):
    type: str = "event"
    action: str = "call_request_acceptance"
    payload: CallRequestAcceptanceEventPayload

# GGUI 로봇 도착 완료 알림
class RobotArrivalCompletionEventPayload(BaseModel):
    task_name: str
    location_name: str

class RobotArrivalCompletionEvent(BaseModel):
    type: str = "event"
    action: str = "robot_arrival_completion"
    payload: RobotArrivalCompletionEventPayload

# GGUI 배송 완료 알림
class DeliveryCompletionEventPayload(BaseModel):
    task_name: str
    request_location: str

class DeliveryCompletionEvent(BaseModel):
    type: str = "event"
    action: str = "delivery_completion"
    payload: DeliveryCompletionEventPayload

# GGUI 시간 초과 복귀 알림
class TaskTimeoutReturnEventPayload(BaseModel):
    task_name: str
    location_name: str

class TaskTimeoutReturnEvent(BaseModel):
    type: str = "event"
    action: str = "task_timeout_return"
    payload: TaskTimeoutReturnEventPayload

# --- AGUI WebSocket Event Models ---

# AGUI 작업 상태 업데이트
class TaskStatusUpdateEventPayload(BaseModel):
    total_task_count: int
    waiting_task_count: int

class TaskStatusUpdateEvent(BaseModel):
    type: str = "event"
    action: str = "task_status_update"
    payload: TaskStatusUpdateEventPayload

# AGUI 로봇 상태 업데이트
class RobotStatusUpdateEventPayload(BaseModel):
    total_robot_count: int
    waiting_robot_count: int

class RobotStatusUpdateEvent(BaseModel):
    type: str = "event"
    action: str = "robot_status_update"
    payload: RobotStatusUpdateEventPayload

# --- Task Status Change ---
class TaskStatusChangeRequestPayload(BaseModel):
    task_id: int
    new_status: str # e.g., "준비 완료"

class TaskStatusChangeRequest(BaseModel):
    payload: TaskStatusChangeRequestPayload

class TaskStatusChangeResponsePayload(BaseModel):
    success: bool
    message: str

class TaskStatusChangeResponse(BaseModel):
    payload: TaskStatusChangeResponsePayload

# ----------------------------------------------------------------
# AGUI (Admin GUI) 모델
# ----------------------------------------------------------------

# 작업 목록 조회를 위한 개별 작업 모델
class TaskInDB(BaseModel):
    task_id: int
    task_type: str
    task_status: str
    destination: str
    robot_id: int | None
    task_creation_time: datetime
    task_completion_time: datetime | None
    
    @field_serializer('task_creation_time')
    def serialize_creation_time(self, value: datetime) -> str:
        """ISO 8601 형태로 시리얼라이즈"""
        return value.isoformat() + 'Z' if value else None
    
    @field_serializer('task_completion_time')
    def serialize_completion_time(self, value: datetime | None) -> str | None:
        """ISO 8601 형태로 시리얼라이즈"""
        return value.isoformat() + 'Z' if value else None

# 작업 목록 조회 응답 모델
class TaskListResponse(BaseModel):
    tasks: List[TaskInDB]

# 로봇 목록 조회를 위한 개별 로봇 모델
class RobotInDB(BaseModel):
    robot_id: int
    model_name: str
    installation_date: Optional[date] = None
    current_location: str | None # location.name
    battery_level: float | None
    task_status: str | None # robot_status.name
    has_error: bool
    error_code: str | None # error.name

# 로봇 목록 조회 응답 모델
class RobotListResponse(BaseModel):
    robots: List[RobotInDB]

# --- GGUI HTTP 동기 인터페이스 모델들 ---

# 호출 작업 생성 요청/응답
class CreateCallTaskRequestPayload(BasePayload):
    location: str
    task_type: int

class CreateCallTaskRequest(BaseModel):
    type: str = "request"
    action: str = "create_call_task"
    payload: CreateCallTaskRequestPayload

class CreateCallTaskResponsePayload(BasePayload):
    location_name: str
    task_name: str
    success: bool
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    task_creation_time: str

class CreateCallTaskResponse(BaseModel):
    type: str = "response"
    action: str = "create_call_task"
    payload: CreateCallTaskResponsePayload

# 음식 메뉴 요청/응답
class GetFoodMenuGGUIRequestPayload(BasePayload):
    location_name: str

class GetFoodMenuGGUIRequest(BaseModel):
    type: str = "request"
    action: str = "get_food_menu"
    payload: GetFoodMenuGGUIRequestPayload

class FoodMenuItem(BaseModel):
    food_name: str
    price: int
    image: str

class GetFoodMenuGGUIResponsePayload(BasePayload):
    food_items: List[FoodMenuItem]

class GetFoodMenuGGUIResponse(BaseModel):
    type: str = "response"
    action: str = "get_food_menu"
    payload: GetFoodMenuGGUIResponsePayload

# 비품 메뉴 요청/응답
class GetSupplyMenuGGUIRequestPayload(BasePayload):
    location_name: str

class GetSupplyMenuGGUIRequest(BaseModel):
    type: str = "request"
    action: str = "get_supply_menu"
    payload: GetSupplyMenuGGUIRequestPayload

class SupplyMenuItem(BaseModel):
    supply_name: str
    image: str

class GetSupplyMenuGGUIResponsePayload(BasePayload):
    supply_items: List[SupplyMenuItem]

class GetSupplyMenuGGUIResponse(BaseModel):
    type: str = "response"
    action: str = "get_supply_menu"
    payload: GetSupplyMenuGGUIResponsePayload

# 배송 작업 생성 요청/응답 (GGUI용)
class CreateDeliveryTaskGGUIRequestPayload(BasePayload):
    location_name: str
    task_type_name: str
    order_details: Dict[str, List[OrderItem]]

class CreateDeliveryTaskGGUIRequest(BaseModel):
    type: str = "request"
    action: str = "create_delivery_task"
    payload: CreateDeliveryTaskGGUIRequestPayload

class CreateDeliveryTaskGGUIResponsePayload(BasePayload):
    location_name: str
    task_name: str
    success: bool
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    estimated_time: int
    task_creation_time: str

class CreateDeliveryTaskGGUIResponse(BaseModel):
    type: str = "response"
    action: str = "create_delivery_task"
    payload: CreateDeliveryTaskGGUIResponsePayload

# 호출 내역 조회 요청/응답
class GetCallHistoryRequestPayload(BasePayload):
    location_name: str
    task_name: str

class GetCallHistoryRequest(BaseModel):
    type: str = "request"
    action: str = "get_call_history"
    payload: GetCallHistoryRequestPayload

class RobotStatus(BaseModel):
    x: float
    y: float
    floor_id: int

class GetCallHistoryResponsePayload(BasePayload):
    location_name: str
    task_name: str
    task_type_name: str
    estimated_time: int
    robot_status: RobotStatus

class GetCallHistoryResponse(BaseModel):
    type: str = "response"
    action: str = "get_call_history"
    payload: GetCallHistoryResponsePayload

# 주문 내역 조회 요청/응답
class GetOrderHistoryRequestPayload(BasePayload):
    request_location: str
    task_name: str
    task_type_name: str

class GetOrderHistoryRequest(BaseModel):
    type: str = "request"
    action: str = "get_order_history"
    payload: GetOrderHistoryRequestPayload

class GetOrderHistoryResponsePayload(BasePayload):
    request_location: str
    task_name: str
    task_type_name: str
    estimated_time: int
    task_creation_time: str
    robot_assignment_time: str
    pickup_completion_time: str
    delivery_arrival_time: Optional[str] = None

class GetOrderHistoryResponse(BaseModel):
    type: str = "response"
    action: str = "get_order_history"
    payload: GetOrderHistoryResponsePayload

# --- AGUI HTTP 통신 인터페이스 모델들 ---

# 작업 목록 요청
class TaskListFilters(BaseModel):
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    task_type: Optional[str] = None
    task_status: Optional[str] = None
    destination: Optional[str] = None

class TaskListRequestPayload(BasePayload):
    filters: TaskListFilters

class TaskListRequest(BaseModel):
    type: str = "request"
    action: str = "task_list"
    payload: TaskListRequestPayload

class TaskListResponsePayload(BasePayload):
    tasks: List[TaskInDB]

class TaskListAGUIResponse(BaseModel):
    type: str = "response"
    action: str = "task_list"
    payload: TaskListResponsePayload

# 작업 상세 요청
class TaskDetailRequestPayload(BasePayload):
    task_id: str

class TaskDetailRequest(BaseModel):
    type: str = "request"
    action: str = "task_detail"
    payload: TaskDetailRequestPayload

class TaskDetailResponsePayload(BasePayload):
    robot_assignment_time: Optional[str] = None
    pickup_completion_time: Optional[str] = None
    delivery_arrival_time: Optional[str] = None
    task_completion_time: Optional[str] = None

class TaskDetailResponse(BaseModel):
    type: str = "response"
    action: str = "task_detail"
    payload: TaskDetailResponsePayload

# 로봇 목록 요청
class RobotListFilters(BaseModel):
    robot_id: Optional[str] = None
    model_name: Optional[str] = None
    robot_status: Optional[str] = None

class RobotListRequestPayload(BasePayload):
    filters: RobotListFilters

class RobotListRequest(BaseModel):
    type: str = "request"
    action: str = "robot_list"
    payload: RobotListRequestPayload

class RobotListResponsePayload(BasePayload):
    robots: List[RobotInDB]

class RobotListAGUIResponse(BaseModel):
    type: str = "response"
    action: str = "robot_list"
    payload: RobotListResponsePayload