# TrackingEvent.msg
int32 robot_id
int32 tracking_event_id
int32 task_id
builtin_interfaces/Time timestamp

# tracking_event_id values:
# 0: slow_down
# 1: maintain
# 2: lost
# 3: resume 