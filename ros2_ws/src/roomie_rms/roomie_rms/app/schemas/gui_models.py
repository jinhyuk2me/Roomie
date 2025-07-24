from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date

# GUI <=> 서버 기본 통신 모델
class SimpleRequest(BaseModel):
    command: str
    data: dict

class SimpleResponse(BaseModel):
    status: str
    message: str

# 음식 메뉴 아이템 모델
class FoodItem(BaseModel):
    food_name: str
    price: int
    image: str

# GGUI -> RMS 음식 메뉴 요청
class GetFoodMenuRequest(BaseModel):
    type: str
    action: str
    payload: dict

# RMS -> GGUI 음식 메뉴 응답
class GetFoodMenuResponse(BaseModel):
    type: str = "response"
    action: str = "get_food_menu"
    payload: dict

# 배송 주문 아이템 상세
class OrderItemDetail(BaseModel):
    name: str
    quantity: int
    price: int

# GGUI -> RMS 배송 작업 생성 페이로드
class CreateDeliveryTaskPayload(BaseModel):
    location_name: str
    task_type_name: str
    order_details: dict[str, List[OrderItemDetail]]

# GGUI -> RMS 배송 작업 생성 요청
class CreateDeliveryTaskRequest(BaseModel):
    type: str = "request"
    action: str = "create_delivery_task"
    payload: CreateDeliveryTaskPayload

# RMS -> GGUI 배송 작업 생성 응답
class CreateDeliveryTaskResponse(BaseModel):
    type: str = "response"
    action: str = "create_delivery_task"
    payload: CreateDeliveryTaskResponsePayload

# RMS -> SGUI 음식 주문 발생 이벤트
class FoodOrderCreationEvent(BaseModel):
    type: str = "event"
    action: str = "food_order_creation"
    payload: dict

# --- Food Order Status Change (SGUI) ---
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