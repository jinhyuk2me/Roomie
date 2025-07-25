# RobotState.msg
int32 robot_id
int32 robot_state_id
# int32 task_id

# robot_state_id values:
# 0: 작업 불가능
# 1: 작업 가능
# 2: 작업 입력 중
# 3: 작업 수행 중
# 4: 복귀 대기 중
# 5: 복귀 중
# 6: 작업 실패
# 7: 시스템 오류 