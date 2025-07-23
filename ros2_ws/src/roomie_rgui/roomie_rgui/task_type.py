from enum import Enum

class TaskType(Enum):
    WAITING = 0
    CALL = 1
    GUIDE = 2
    DELIVERY = 3
    RETURN = 4
    CHARGING = 5
    FAILED = 6
    ERROR = 7