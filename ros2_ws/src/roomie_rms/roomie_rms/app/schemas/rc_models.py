"""
ROS2 Robot Controller (RC) 통신을 위한 데이터 모델들

인터페이스 명세 (roomie_interface_spec.md)에 정의된 
Service, Topic, Action 메시지들을 Pydantic 모델로 정의
"""

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# =============================================================================
# Service 요청/응답 모델
# =============================================================================

class CreateTaskRequest(BaseModel):
    """길안내 작업 생성 요청 (/roomie/command/create_task)"""
    robot_id: int
    target_location_id: int

class CreateTaskResponse(BaseModel):
    """길안내 작업 생성 응답"""
    robot_id: int
    task_id: int
    success: bool
    message: str

class GetLocationsRequest(BaseModel):
    """좌표 데이터 요청 (/roomie/command/get_locations)"""
    robot_id: int

class GetLocationsResponse(BaseModel):
    """좌표 데이터 응답"""
    robot_id: int
    success: bool
    location_ids: List[int]
    floor_ids: List[int]
    location_xs: List[float]
    location_ys: List[float]

# =============================================================================
# Topic 메시지 모델
# =============================================================================

class RobotState(BaseModel):
    """로봇 상태 (/roomie/status/robot_state)"""
    robot_id: int
    robot_state_id: int

class TaskState(BaseModel):
    """작업 상태 (/roomie/status/task_state)"""
    task_id: int
    task_state_id: int

class Arrival(BaseModel):
    """장소 도착 (/roomie/event/arrival)"""
    robot_id: int
    task_id: int
    location_id: int

class BatteryStatus(BaseModel):
    """배터리 잔량 (/roomie/status/battery_status)"""
    robot_id: int
    charge_percentage: float
    is_charging: bool

class RoomiePose(BaseModel):
    """현재 로봇 위치와 방향 (/roomie/status/roomie_pose)"""
    robot_id: int
    floor_id: int
    # geometry_msgs/Pose는 별도 처리 필요

class PickupCompleted(BaseModel):
    """픽업 완료 (/roomie/event/pickup_completed)"""
    robot_id: int
    task_id: int
    timestamp: datetime

class DeliveryCompleted(BaseModel):
    """수령 완료 (/roomie/event/delivery_completed)"""
    robot_id: int
    task_id: int
    timestamp: datetime

# =============================================================================
# Action 메시지 모델
# =============================================================================

class PerformTaskGoal(BaseModel):
    """작업 할당 목표 (/roomie/action/perform_task)"""
    robot_id: int
    task_id: int
    task_type_id: int
    task_status_id: int
    target_location_id: int
    pickup_location_id: int
    order_info: str  # JSON 문자열

class PerformTaskResult(BaseModel):
    """작업 할당 결과"""
    robot_id: int
    task_id: int
    success: bool
    message: str

class PerformTaskFeedback(BaseModel):
    """작업 할당 피드백"""
    robot_id: int
    task_id: int
    task_status_id: int

class PerformReturnGoal(BaseModel):
    """복귀 목표 (/roomie/action/perform_return)"""
    robot_id: int

class PerformReturnResult(BaseModel):
    """복귀 결과"""
    robot_id: int
    message: str 