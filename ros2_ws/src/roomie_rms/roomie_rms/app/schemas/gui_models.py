from pydantic import BaseModel
from typing import List
from datetime import datetime

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
    payload: dict

# RMS -> SGUI 음식 주문 발생 이벤트
class FoodOrderCreationEvent(BaseModel):
    type: str = "event"
    action: str = "food_order_creation"
    payload: dict