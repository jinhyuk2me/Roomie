from enum import Enum

class DeliveryState(Enum):
    PICKUP_MOVING = 0
    PICKUP_ARRIVED = 1
    CHECKING_ORDER = 2
    PICKUP_DRAWER_CONTROL = 3
    DELIVERY_MOVING = 4
    DELIVERY_ARRIVED = 5
    DELIVERY_DRAWER_CONTROL = 6
    THANK_YOU = 7

# 배송 이외 다른 Task는 추후 구현함