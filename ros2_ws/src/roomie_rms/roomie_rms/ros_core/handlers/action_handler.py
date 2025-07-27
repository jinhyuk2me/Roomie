import asyncio
from app.utils.logger import get_logger
from app.utils.error_handler import handle_ros_errors
from roomie_msgs.action import PerformTask, PerformReturn # 인터페이스 임포트

logger = get_logger(__name__)

class ActionHandler:
    """ROS2 Action 관련 로직을 콜백 기반 비동기 방식으로 관리하는 클래스"""
    
    def __init__(self, robot_manager, task_manager, db_manager, node=None):
        self.robot_manager = robot_manager
        self.task_manager = task_manager
        self.db_manager = db_manager # DB 업데이트를 위해 추가
        self.node = node
        
        # 진행 중인 액션을 추적하기 위한 딕셔너리
        self.active_goals = {} # {task_id: goal_handle}
        self.active_return_goals = {} # {robot_id: goal_handle}

    @handle_ros_errors
    def send_perform_task_goal(self, goal_data: dict):
        """
        PerformTask 액션 목표를 RC에 전송합니다.
        이 함수는 목표 전송 요청 후 즉시 반환됩니다(non-blocking).
        """
        if not self.node._perform_task_ac.server_is_ready():
            logger.error(
                'PerformTask 액션 서버를 찾을 수 없습니다.',
                category="ROS2", subcategory="ACTION-ERROR"
            )
            # TODO: 작업 상태를 '실패'로 변경하는 로직 필요
            return

        task_id = goal_data.get('task_id')
        if not task_id:
            logger.error(
                'goal_data에 task_id가 없습니다.',
                category="ROS2", subcategory="ACTION-ERROR"
            )
            return

        goal_msg = PerformTask.Goal(**goal_data)
        
        # send_goal_async는 Future 객체를 반환합니다.
        send_goal_future = self.node._perform_task_ac.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        
        # Future가 완료되면(목표 수락/거부 응답이 오면) goal_response_callback을 실행하도록 등록
        # task_id를 콜백에서 사용할 수 있도록 lambda로 래핑
        send_goal_future.add_done_callback(lambda future: self.goal_response_callback(future, task_id))
        
        logger.info(
            "PerformTask 목표 전송을 요청했습니다.",
            category="ROS2", subcategory="ACTION-CALL",
            details={"TaskID": task_id, "Action": "PerformTask"}
        )

    @handle_ros_errors
    def send_perform_return_goal(self, robot_id: int, return_location_id: int = None):
        """
        PerformReturn 액션 목표를 RC에 전송합니다.
        로봇을 대기 장소로 복귀시키는 기능입니다.
        """
        if not self.node._perform_return_ac.server_is_ready():
            logger.error(
                'PerformReturn 액션 서버를 찾을 수 없습니다.',
                category="ROS2", subcategory="ACTION-ERROR"
            )
            return

        if not robot_id:
            logger.error(
                'robot_id가 없습니다.',
                category="ROS2", subcategory="ACTION-ERROR"
            )
            return

        # 기본 복귀 위치 설정 (LOB_WAITING)
        if return_location_id is None:
            from app.config import settings
            # LOB_WAITING 위치 ID를 DB에서 조회하거나 설정에서 가져옴
            return_location_id = 1  # 기본값, 실제로는 DB에서 조회해야 함

        goal_data = {
            'robot_id': robot_id,
            'return_location_id': return_location_id
        }
        
        goal_msg = PerformReturn.Goal(**goal_data)
        
        # send_goal_async는 Future 객체를 반환합니다.
        send_goal_future = self.node._perform_return_ac.send_goal_async(
            goal_msg,
            feedback_callback=self.return_feedback_callback
        )
        
        # Future가 완료되면 goal_response_callback을 실행하도록 등록
        # robot_id를 콜백에서 사용할 수 있도록 lambda로 래핑
        send_goal_future.add_done_callback(lambda future: self.return_goal_response_callback(future, robot_id))
        
        logger.info(
            "PerformReturn 목표 전송을 요청했습니다.",
            category="ROS2", subcategory="ACTION-CALL",
            details={"RobotID": robot_id, "Action": "PerformReturn"}
        )

    def goal_response_callback(self, future, task_id):
        """목표에 대한 수락/거부 응답을 처리하는 콜백"""
        goal_handle = future.result()
        if not goal_handle.accepted:
            logger.error(
                '목표가 거부되었습니다.',
                category="ROS2", subcategory="ACTION-REJECT",
                details={"TaskID": task_id, "GoalID": str(goal_handle.goal_id)}
            )
            # TODO: 작업 상태를 '실패'로 변경하는 로직
            return

        logger.info(
            '목표가 수락되었습니다.',
            category="ROS2", subcategory="ACTION-ACCEPT",
            details={"TaskID": task_id}
        )
        
        # 활성 목표 핸들 저장
        self.active_goals[task_id] = goal_handle

        # 결과 Future에 대한 콜백 등록
        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.get_result_callback)

    def return_goal_response_callback(self, future, robot_id):
        """복귀 목표에 대한 수락/거부 응답을 처리하는 콜백"""
        goal_handle = future.result()
        if not goal_handle.accepted:
            logger.error(
                '복귀 목표가 거부되었습니다.',
                category="ROS2", subcategory="ACTION-REJECT",
                details={"RobotID": robot_id, "GoalID": str(goal_handle.goal_id)}
            )
            return

        logger.info(
            '복귀 목표가 수락되었습니다.',
            category="ROS2", subcategory="ACTION-ACCEPT",
            details={"RobotID": robot_id}
        )
        
        # 활성 복귀 목표 핸들 저장
        self.active_return_goals[robot_id] = goal_handle

        # 결과 Future에 대한 콜백 등록
        get_result_future = goal_handle.get_result_async()
        get_result_future.add_done_callback(self.get_return_result_callback)

    def feedback_callback(self, feedback_msg):
        """액션 수행 중 RC로부터 피드백을 수신하여 처리하는 콜백"""
        feedback = feedback_msg.feedback
        task_id = feedback.task_id
        new_status_id = feedback.task_status_id
        
        logger.info(
            f"피드백 수신 - 새로운 상태: {new_status_id}",
            category="ROS2", subcategory="ACTION-FEEDBACK",
            details={"TaskID": task_id, "NewStatusID": new_status_id}
        )
        
        # DB의 작업 상태를 피드백에 따라 업데이트
        # self.task_manager.update_task_status(task_id, new_status_id) # 이러한 메서드가 필요합니다.
        # 예시: UPDATE task SET task_status_id = %s WHERE id = %s

    def return_feedback_callback(self, feedback_msg):
        """복귀 액션 수행 중 RC로부터 피드백을 수신하여 처리하는 콜백"""
        feedback = feedback_msg.feedback
        robot_id = feedback.robot_id
        return_status = feedback.return_status
        
        logger.info(
            f"복귀 피드백 수신 - 상태: {return_status}",
            category="ROS2", subcategory="ACTION-FEEDBACK",
            details={"RobotID": robot_id, "ReturnStatus": return_status}
        )
        
        # 로봇 상태를 복귀 중으로 업데이트
        # self.robot_manager.update_robot_status(robot_id, '복귀 중')

    def get_result_callback(self, future):
        """액션의 최종 결과를 처리하는 콜백"""
        result = future.result().result
        task_id = result.task_id
        success = result.success
        message = result.message

        if success:
            logger.info(
                f"최종 작업 성공. 메시지: {message}",
                category="ROS2", subcategory="ACTION-DONE",
                details={"TaskID": task_id, "Result": "SUCCESS"}
            )
            # 작업이 완전히 끝났으므로, '수령 완료' 등의 최종 상태로 업데이트
            # self.task_manager.update_task_status(task_id, settings.db_consts.task_status['수령 완료'])
        else:
            logger.error(
                f"최종 작업 실패. 메시지: {message}",
                category="ROS2", subcategory="ACTION-DONE",
                details={"TaskID": task_id, "Result": "FAILURE"}
            )
            # self.task_manager.update_task_status(task_id, settings.db_consts.task_status['작업 실패'])
        
        # 완료된 작업은 활성 목표 목록에서 제거
        if task_id in self.active_goals:
            del self.active_goals[task_id]

    def get_return_result_callback(self, future):
        """복귀 액션의 최종 결과를 처리하는 콜백"""
        result = future.result().result
        robot_id = result.robot_id
        success = result.success
        message = result.message

        if success:
            logger.info(
                f"복귀 완료. 메시지: {message}",
                category="ROS2", subcategory="ACTION-DONE",
                details={"RobotID": robot_id, "Result": "SUCCESS"}
            )
            # 로봇 상태를 '작업 가능'으로 업데이트
            # self.robot_manager.update_robot_status(robot_id, '작업 가능')
        else:
            logger.error(
                f"복귀 실패. 메시지: {message}",
                category="ROS2", subcategory="ACTION-DONE",
                details={"RobotID": robot_id, "Result": "FAILURE"}
            )
            # 로봇 상태를 '시스템 오류'로 업데이트
            # self.robot_manager.update_robot_status(robot_id, '시스템 오류')
        
        # 완료된 복귀 작업은 활성 목표 목록에서 제거
        if robot_id in self.active_return_goals:
            del self.active_return_goals[robot_id]

    def cancel_task(self, task_id: int):
        """진행 중인 작업을 취소합니다."""
        if task_id in self.active_goals:
            goal_handle = self.active_goals[task_id]
            goal_handle.cancel_goal_async()
            logger.info(
                "작업 취소 요청",
                category="ROS2", subcategory="ACTION-CANCEL",
                details={"TaskID": task_id}
            )
        else:
            logger.warning(
                "취소할 활성 작업이 없습니다.",
                category="ROS2", subcategory="ACTION-CANCEL",
                details={"TaskID": task_id}
            )

    def cancel_return(self, robot_id: int):
        """진행 중인 복귀 작업을 취소합니다."""
        if robot_id in self.active_return_goals:
            goal_handle = self.active_return_goals[robot_id]
            goal_handle.cancel_goal_async()
            logger.info(
                "복귀 취소 요청",
                category="ROS2", subcategory="ACTION-CANCEL",
                details={"RobotID": robot_id}
            )
        else:
            logger.warning(
                "취소할 활성 복귀 작업이 없습니다.",
                category="ROS2", subcategory="ACTION-CANCEL",
                details={"RobotID": robot_id}
            )