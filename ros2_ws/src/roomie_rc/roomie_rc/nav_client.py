# nav_client.py

import rclpy
import rclpy.action
from rclpy.node import Node
from rclpy.qos import QoSProfile
from builtin_interfaces.msg import Time

from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from tf_transformations import quaternion_from_euler # pip install tf-transformations 필요

from action_msgs.msg import GoalStatus # 수정된 임포트


class NavClient:
    """
    ROS2 내비게이션 스택의 NavigateToPose 액션과의 통신을 담당하는 클라이언트
    """

    def __init__(self, parent_node: Node):
        self.node = parent_node
        self.goal_handle = None
        self.goal_future = None
        self.result_future = None
        self.nav_completion_callback = None # 내비게이션 완료 시 RCNode에 알릴 콜백

        # QoS 프로파일 설정 (Publish/Subscribe에 필요할 수 있음)
        self.qos_profile = QoSProfile(depth=10)

        # NavigateToPose 액션 클라이언트 초기화
        self.nav_to_pose_client = rclpy.action.ActionClient(
            self.node,
            NavigateToPose,
            'navigate_to_pose' # Nav2가 제공하는 표준 액션 서버 이름
        )
        self.node.get_logger().info('NavClient: NavigateToPose Action Client 초기화 완료')

        # 액션 서버가 사용 가능할 때까지 대기 (필수)
        if not self.nav_to_pose_client.wait_for_server(timeout_sec=5.0): # 5초 타임아웃
            self.node.get_logger().error('NavClient: NavigateToPose 액션 서버를 찾을 수 없습니다! 내비게이션 불가.')
            # TODO: 서버를 찾지 못했을 때의 예외 처리 또는 재시도 로직 추가

    def create_goal_pose(self, location_info, yaw_radians=0.0):
        """
        LocationManager 정보로부터 NavigateToPose 목표 PoseStamped 메시지 생성
        Args:
            location_info (dict): LocationManager.get_location_info()에서 반환된 딕셔너리 (x, y, floor_id 등 포함)
            yaw_radians (float): 목표 지점에서의 로봇 최종 방향 (라디안). 기본값은 0 (X축 방향).
        Returns:
            PoseStamped: Nav2에 전송할 목표 Pose 메시지
        """
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map' # Nav2는 'map' 프레임을 기본으로 사용
        goal_pose.header.stamp = self.node.get_clock().now().to_msg()
        
        goal_pose.pose.position.x = location_info['x']
        goal_pose.pose.position.y = location_info['y']
        goal_pose.pose.position.z = 0.0 # 2D 내비게이션이므로 Z는 0

        # Yaw (라디안) 값을 쿼터니언으로 변환
        q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, yaw_radians) # Roll, Pitch, Yaw
        goal_pose.pose.orientation.x = q_x
        goal_pose.pose.orientation.y = q_y
        goal_pose.pose.orientation.z = q_z
        goal_pose.pose.orientation.w = q_w
        
        return goal_pose

    def go_to_pose(self, target_pose: PoseStamped, completion_callback=None):
        """
        로봇에게 특정 Pose로 이동하도록 명령합니다.
        Args:
            target_pose (PoseStamped): 로봇이 이동할 목표 Pose (위치 및 방향)
            completion_callback (callable): 내비게이션 완료 시 호출될 콜백 함수 (성공/실패 여부, 태스크 단계 전달)
        """
        if not self.nav_to_pose_client.server_is_ready():
            self.node.get_logger().error('NavClient: NavigateToPose 액션 서버가 준비되지 않았습니다.')
            if completion_callback:
                # 서버 미준비로 인한 실패 알림
                completion_callback(False, "server_not_ready") 
            return

        self.nav_completion_callback = completion_callback

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = target_pose

        self.node.get_logger().info(f'NavClient: 내비게이션 목표 전송 시작: x={target_pose.pose.position.x:.2f}, y={target_pose.pose.position.y:.2f}')
        
        # 액션 목표 전송 및 응답 처리 콜백 등록
        self.goal_future = self.nav_to_pose_client.send_goal_async(
            goal_msg,
            feedback_callback=self._navigation_feedback_callback
        )
        self.goal_future.add_done_callback(self._goal_response_callback)

    def _goal_response_callback(self, future):
        """액션 서버로부터 목표 수락/거부 응답 처리"""
        self.goal_handle = future.result()
        if not self.goal_handle.accepted:
            self.node.get_logger().error('NavClient: 내비게이션 목표가 거부되었습니다.')
            if self.nav_completion_callback:
                self.nav_completion_callback(False, "goal_rejected") # 내비게이션 실패 알림
            return

        self.node.get_logger().info('NavClient: 내비게이션 목표가 수락되었습니다. 결과 대기 중...')
        # 목표가 수락되면, 결과 대기 콜백 등록
        self.result_future = self.goal_handle.get_result_async()
        self.result_future.add_done_callback(self._get_navigation_result_callback)

    def _get_navigation_result_callback(self, future):
        """내비게이션 액션 결과 처리"""
        status = future.result().status
        result = future.result().result # NavigateToPose 결과는 비어있음 (result)

        if status == GoalStatus.STATUS_SUCCEEDED: # 수정된 부분: GoalStatus 직접 사용
            self.node.get_logger().info('NavClient: 내비게이션 성공!')
            if self.nav_completion_callback:
                self.nav_completion_callback(True, "navigation_succeeded") # 내비게이션 성공 알림
        else:
            self.node.get_logger().error(f'NavClient: 내비게이션 실패! 상태: {status}')
            if self.nav_completion_callback:
                self.nav_completion_callback(False, f"navigation_failed_status_{status}") # 내비게이션 실패 알림

        # 콜백 처리 후 핸들 초기화
        self.goal_handle = None
        self.goal_future = None
        self.result_future = None
        self.nav_completion_callback = None

    def _navigation_feedback_callback(self, feedback_msg):
        """내비게이션 피드백 처리 (로봇의 실시간 위치, 남은 거리 등)"""
        feedback = feedback_msg.feedback
        # self.node.get_logger().info(f'NavClient: 내비게이션 진행 중... 현재 위치: ({feedback.current_pose.pose.position.x:.2f}, {feedback.current_pose.pose.position.y:.2f}), 남은 거리: {feedback.distance_remaining:.2f}m')
        # TODO: GUI 업데이트 또는 로그 기록 등에 피드백 정보 활용