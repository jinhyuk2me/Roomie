import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
import uvicorn
from app.main import app
from app.utils.logger import logger
from app.services.db_manager import db_manager
from app.services.websocket_manager import manager as websocket_manager
import threading
import asyncio
from datetime import datetime
import json

from roomie_msgs.msg.robot_status import RobotState, Arrival, BatteryStatus, RoomiePose
from roomie_msgs.msg.task_management import TaskState, PickupCompleted, DeliveryCompleted
from roomie_msgs.srv.robot_control import GetLocations, CreateTask
from roomie_msgs.action import PerformTask, PerformReturn

# RoomiePose 메시지에 포함된 geometry_msgs 임포트 (현재는 폴더 없음)
from geometry_msgs.msg import Pose


class RmsNode(Node):
    def __init__(self):
        super().__init__('rms_node')
        logger.info('RMS ROS2 노드가 초기화되었습니다.')

        # --- Service Servers ---
        self.get_locations_srv = self.create_service(
            GetLocations,
            '/roomie/command/get_locations',
            self.get_locations_callback
        )

        # --- Service Clients ---
        self.create_task_cli = self.create_client(CreateTask, '/roomie/command/create_task')

        # --- Action Clients ---
        self._perform_task_ac = ActionClient(self, PerformTask, '/roomie/action/perform_task')
        self._perform_return_ac = ActionClient(self, PerformReturn, '/roomie/action/perform_return')

        # --- Publishers (RMS -> RC) ---
        self.task_state_pub = self.create_publisher(TaskState, '/roomie/status/task_state', 10)

        # --- Subscribers (RC -> RMS) ---
        self.create_subscription(RobotState, '/roomie/status/robot_state', self.robot_state_callback, 10)
        self.create_subscription(TaskState, '/roomie/status/task_state', self.task_state_callback, 10)
        self.create_subscription(Arrival, '/roomie/event/arrival', self.arrival_callback, 10)
        self.create_subscription(BatteryStatus, '/roomie/status/battery_status', self.battery_status_callback, 10)
        self.create_subscription(RoomiePose, '/roomie/status/roomie_pose', self.roomie_pose_callback, 10)
        self.create_subscription(PickupCompleted, '/roomie/event/pickup_completed', self.pickup_completed_callback, 10)
        self.create_subscription(DeliveryCompleted, '/roomie/event/delivery_completed', self.delivery_completed_callback, 10)
        
        self.get_logger().info('ROS2-RC 통신 인터페이스가 준비되었습니다.')

    # --- Service Callbacks ---
    def get_locations_callback(self, request, response):
        """RC로부터 위치 정보 요청을 받아 DB에 저장된 모든 위치 정보를 반환합니다."""
        logger.info(f"RC로부터 좌표 데이터 요청 수신 (로봇 ID: {request.robot_id})")
        
        conn = db_manager.get_connection()
        if not conn:
            logger.error("DB 연결 실패로 위치 정보를 반환할 수 없습니다.")
            response.success = False
            return response
            
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id, floor_id, location_x, location_y FROM location WHERE location_x IS NOT NULL AND location_y IS NOT NULL")
            locations = cursor.fetchall()
            
            response.robot_id = request.robot_id
            response.success = True
            response.location_ids = [loc['id'] for loc in locations]
            response.floor_ids = [loc['floor_id'] for loc in locations]
            response.location_xs = [loc['location_x'] for loc in locations]
            response.location_ys = [loc['location_y'] for loc in locations]
            
            logger.info(f"DB에 저장된 모든 위치 정보 {len(locations)}개를 RC (로봇 ID: {request.robot_id})로 전송합니다.")
            
        except Exception as e:
            logger.error(f"위치 정보 조회 중 오류 발생: {e}")
            response.success = False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                
        return response

    # --- Publisher Methods ---
    def publish_task_state(self, task_id, status_id):
        """RC에게 작업의 현재 상태를 알립니다."""
        msg = TaskState()
        msg.task_id = task_id
        msg.task_state_id = status_id
        self.task_state_pub.publish(msg)
        logger.info(f"RC로 작업 상태 전송: Task ID {task_id}, State ID {status_id}")

    # --- Main Business Logic ---
    def _execute_task_assignment(self, robot_id):
        """(별도 스레드에서 실행) 준비된 작업을 찾아 로봇에 할당하고 액션을 호출합니다."""
        logger.info(f"로봇 {robot_id}에 대한 작업 할당 로직 시작...")
        
        conn = db_manager.get_connection()
        if not conn:
            logger.error("작업 할당 실패 (DB 연결 불가)")
            return
            
        try:
            cursor = conn.cursor(dictionary=True)
            
            # 가장 오래된 '준비 완료' 상태의 작업 찾기
            #    FOR UPDATE로 다른 스레드가 같은 작업을 동시에 가져가지 못하도록 잠금
            query = """
                SELECT id, type_id, location_id FROM task 
                WHERE task_status_id = 1 
                ORDER BY task_creation_time ASC LIMIT 1 FOR UPDATE
            """
            cursor.execute(query)
            task_to_assign = cursor.fetchone()

            if not task_to_assign:
                logger.info("할당할 작업 없음. 로직을 종료합니다.")
                return

            task_id = task_to_assign['id']
            logger.info(f"로봇 {robot_id}에게 작업 {task_id}를 할당합니다.")

            # 작업을 '로봇 할당됨' 상태로 변경하고, 로봇 ID, 시간 기록
            update_query = """
                UPDATE task SET robot_id = %s, task_status_id = 2, robot_assignment_time = %s 
                WHERE id = %s
            """
            cursor.execute(update_query, (robot_id, datetime.now(), task_id))

            # RC에 작업을 지시하기 위해 주문 정보 조회
            order_info_query = """
                SELECT f.name, foi.quantity 
                FROM `order` o
                JOIN food_order_item foi ON o.id = foi.order_id
                JOIN food f ON foi.food_id = f.id
                WHERE o.task_id = %s
            """
            cursor.execute(order_info_query, (task_id,))
            order_items = cursor.fetchall()
            
            # DB에서 조회한 주문 내역을 JSON 형식으로 변환
            order_details = {
                "items": [{"name": item['name'], "quantity": item['quantity']} for item in order_items]
            }
            order_info_json = json.dumps(order_details)

            conn.commit()
            
            # RC에 작업을 지시하기 위해 PerformTask 액션 호출
            goal_data = {
                'robot_id': robot_id,
                'task_id': task_id,
                'task_type_id': task_to_assign['type_id'],
                'task_status_id': 2, # 로봇 할당됨
                'target_location_id': task_to_assign['location_id'],
                'pickup_location_id': 2, # 'RES_PICKUP'의 ID
                'order_info': order_info_json
            }
            
            # 비동기 함수를 스레드에서 안전하게 실행
            logger.info(f"PerformTask 액션 목표 전송 시작: Task ID {task_id}")
            asyncio.run(self.send_perform_task_goal(goal_data))

        except Exception as e:
            logger.error(f"작업 할당 중 오류 발생: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def _update_robot_current_state(self, cursor, robot_id, status_id=None, location_id=None, battery_level=None, error_id=None):
        """(Helper) robot_current_state 테이블을 동시성 문제 없이 안전하게 업데이트합니다."""
        
        # 1. SELECT ... FOR UPDATE로 해당 로봇의 현재 상태 레코드를 잠그고 가져옵니다.
        cursor.execute(
            "SELECT id FROM robot_current_state WHERE robot_id = %s FOR UPDATE",
            (robot_id,)
        )
        current_state_record = cursor.fetchone()

        current_time = datetime.now()
        
        if current_state_record:
            # 2a. 레코드가 있으면 UPDATE
            record_id = current_state_record['id']
            update_fields = ["last_updated_time = %s"]
            values = [current_time]
            
            if status_id is not None:
                update_fields.append("robot_status_id = %s")
                values.append(status_id)
            if location_id is not None:
                update_fields.append("location_id = %s")
                values.append(location_id)
            if battery_level is not None:
                update_fields.append("battery_level = %s")
                values.append(battery_level)
            if error_id is not None:
                update_fields.append("error_id = %s")
                values.append(error_id)
            
            values.append(record_id)
            
            query = f"UPDATE robot_current_state SET {', '.join(update_fields)} WHERE id = %s"
            cursor.execute(query, tuple(values))

        else:
            # 2b. 레코드가 없으면 INSERT
            # 모든 필드 값을 채워야 함. 없는 값은 NULL로 처리.
            query = """
                INSERT INTO robot_current_state 
                (robot_id, robot_status_id, location_id, battery_level, error_id, last_updated_time)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (robot_id, status_id, location_id, battery_level, error_id, current_time))


    # --- Subscriber Callbacks (RC -> RMS) ---
    def robot_state_callback(self, msg):
        logger.info(f"로봇 상태 수신: Robot ID {msg.robot_id}, State ID {msg.robot_state_id}")
        
        # 로봇이 '작업 가능' 상태가 되면 작업 할당 로직 실행
        if msg.robot_state_id == 1:
            threading.Thread(target=self._execute_task_assignment, args=(msg.robot_id,)).start()

        # DB 업데이트
        conn = db_manager.get_connection()
        if not conn: return
        try:
            conn.start_transaction()
            cursor = conn.cursor(dictionary=True)
            
            # 상태에 따라 error_id를 설정하거나 해제
            error_id_to_update = None
            is_error_state = msg.robot_state_id in [6, 7] # 6: 작업 실패, 7: 시스템 오류
            
            if is_error_state:
                # TODO: 실제 에러 원인(101, 102, 103)을 RC로부터 받아와야 함.
                #       지금은 상태 ID와 에러 ID를 임시로 매핑.
                error_id_to_update = 103 # '시스템 오류'로 가정
            else:
                # 정상 상태로 돌아오면 에러를 NULL로 해제
                error_id_to_update = None

            self._update_robot_current_state(cursor, msg.robot_id, status_id=msg.robot_state_id, error_id=error_id_to_update)
            
            # 2. 로그 기록
            # ... (robot_log에 INSERT 하는 로직 추가 필요)
            
            conn.commit()
        except Exception as e:
            logger.error(f"로봇 상태 업데이트 중 오류: {e}")
            if conn.in_transaction: conn.rollback()
        finally:
            if conn.is_connected():
                if 'cursor' in locals() and cursor: cursor.close()
                conn.close()
        
        # WebSocket 전파
        event_data = {
            "type": "event",
            "action": "robot_status_update",
            "payload": { "robot_id": msg.robot_id, "robot_status_id": msg.robot_state_id }
        }
        self._broadcast_websocket_event("admin", event_data)
        self._broadcast_websocket_event("staff", event_data)

    def task_state_callback(self, msg):
        logger.info(f"작업 상태 수신 (RC -> RMS): Task ID {msg.task_id}, State ID {msg.task_state_id}")
        # 당장은 필요 없으나 RC에 긴급상황이 발생하거나 작업 중단이 필요한 경우 사용될 수 있음
        pass

    def arrival_callback(self, msg):
        """로봇이 특정 위치에 도착했을 때 호출됩니다."""
        task_id = msg.task_id
        arrival_location_id = msg.location_id
        logger.info(f"로봇 도착 이벤트 수신 | 작업ID: {task_id}, 도착위치ID: {arrival_location_id}")

        conn = db_manager.get_connection()
        if not conn: return

        try:
            conn.start_transaction()
            cursor = conn.cursor(dictionary=True)

            # 작업 정보 조회 (목적지, 할당된 로봇 ID 등)
            cursor.execute("""
                SELECT t.robot_id, t.location_id as destination_id, l.name as destination_name
                FROM task t
                JOIN location l ON t.location_id = l.id
                WHERE t.id = %s
            """, (task_id,))
            task_info = cursor.fetchone()

            if not task_info:
                logger.error(f"도착 이벤트 처리 중 작업 정보를 찾을 수 없음: Task ID {task_id}")
                conn.rollback()
                return

            robot_id = task_info['robot_id']
            destination_id = task_info['destination_id']
            destination_name = task_info['destination_name']
            
            # --- 시나리오 분기 ---
            # 1. 픽업 장소 도착 (location_id 2: RES_PICKUP)
            if arrival_location_id == 2:
                logger.info(f"로봇(ID:{robot_id})이 픽업 장소에 도착했습니다. (작업ID: {task_id})")
                # task 상태를 '픽업 대기 중'(4)으로 변경
                self._update_task_status(cursor, task_id, 4)
                self.publish_task_state(task_id, 4)

                # SGUI에 '음식 픽업 도착' 이벤트 브로드캐스트
                event_payload = {"task_id": task_id, "robot_id": robot_id}
                sdui_event = FoodPickupArrivalEvent(payload=event_payload)
                self._broadcast_websocket_event("staff", sdui_event.model_dump())

            # 2. 최종 목적지 도착
            elif arrival_location_id == destination_id:
                logger.info(f"로봇(ID:{robot_id})이 최종 목적지({destination_name})에 도착했습니다. (작업ID: {task_id})")
                # task 상태를 '배송 도착'(6)으로 변경하고 도착 시간 기록
                update_query = "UPDATE task SET task_status_id = %s, delivery_arrival_time = %s WHERE id = %s"
                cursor.execute(update_query, (6, datetime.now(), task_id))
                self.publish_task_state(task_id, 6)

                # GGUI에 '배송 완료' 이벤트를 '특정' 손님에게만 전송
                event_payload = {"task_name": str(task_id), "request_location": destination_name}
                ggui_event = DeliveryCompletionEvent(payload=event_payload)
                self._send_websocket_event_to_client("guest", destination_name, ggui_event.model_dump())
            
            else:
                logger.warning(f"도착 위치({arrival_location_id})가 픽업 또는 목적지와 일치하지 않습니다.")

            # 로봇 현재 위치 업데이트
            self._update_robot_current_state(cursor, robot_id, location_id=arrival_location_id)
            conn.commit()

        except Exception as e:
            logger.error(f"도착 이벤트 처리 중 오류: {e}")
            if conn.in_transaction: conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def _broadcast_websocket_event(self, client_type: str, data: dict):
        """(Helper) WebSocket 이벤트를 스레드 안전하게 전송합니다."""
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.run_coroutine_threadsafe(websocket_manager.broadcast_to(client_type, data), loop)
            else:
                asyncio.run(websocket_manager.broadcast_to(client_type, data))
            logger.info(f"'{client_type}' 그룹에 WebSocket 이벤트 전송: {data['action']}")
        except Exception as e:
            logger.error(f"WebSocket 이벤트 전송 중 오류 발생: {e}")

    def _send_websocket_event_to_client(self, client_type: str, client_id: str, data: dict):
        """(Helper) 특정 클라이언트에게 WebSocket 이벤트를 스레드 안전하게 전송합니다."""
        if websocket_manager:
            try:
                # ROS2의 동기 콜백에서 FastAPI의 비동기 함수를 실행하기 위해 asyncio.run 사용
                asyncio.run(websocket_manager.send_to_client(client_type, client_id, data))
                logger.info(f"Sent WebSocket event to client: type='{client_type}', id='{client_id}'")
            except Exception as e:
                logger.error(f"Error sending WebSocket event to client {client_id}: {e}")

    def battery_status_callback(self, msg):
        # 수신한 배터리 정보를 AGUI에 실시간으로 전송하기만 함.
        event_data = {
            "type": "event",
            "action": "robot_battery_update",
            "payload": {
                "robot_id": msg.robot_id,
                "charge_percentage": msg.charge_percentage,
                "is_charging": msg.is_charging
            }
        }
        self._broadcast_websocket_event("admin", event_data)

        # DB 업데이트
        conn = db_manager.get_connection()
        if not conn: return
        try:
            conn.start_transaction()
            cursor = conn.cursor(dictionary=True)
            self._update_robot_current_state(cursor, msg.robot_id, battery_level=msg.charge_percentage)
            conn.commit()
        except Exception as e:
            logger.error(f"배터리 상태 업데이트 중 오류: {e}")
            if conn.in_transaction: conn.rollback()
        finally:
            if conn.is_connected():
                if 'cursor' in locals() and cursor: cursor.close()
                conn.close()

    def roomie_pose_callback(self, msg):
        conn = db_manager.get_connection()
        if not conn: return

        try:
            cursor = conn.cursor(dictionary=True)

            # 가장 최근의 위치 기록을 가져와서 현재 위치와 동일한지 확인 (DB 부하 감소)
            cursor.execute("""
                SELECT location_id, floor_id FROM robot_dynamic
                WHERE robot_id = %s ORDER BY record_time DESC LIMIT 1
            """, (msg.robot_id,))
            last_pose = cursor.fetchone()

            # TODO: 현재 로봇의 x, y, theta 좌표(msg.pose)를 기반으로 가장 가까운 location_id를 찾는 로직 필요.
            #       우선은 임의의 location_id가 있다고 가정하고 진행. 현재는 이 로직이 없어 아래 코드는 실행되지 않음.
            current_location_id = None # 이 값을 실제 로직으로 찾아야 함

            if last_pose and last_pose['location_id'] == current_location_id:
                # 위치가 변경되지 않았으면 DB에 기록하지 않음
                return

            if current_location_id is not None:
                # robot_dynamic 테이블에 새로운 위치 기록
                # robot_status_id, task_id 등은 현재 알 수 없으므로 기존 값을 유지하거나 Null로 처리해야 함.
                # 여기서는 Nullable 필드인 floor_id, location_id, record_time만 기록 시도.
                cursor.execute("""
                    INSERT INTO robot_log (robot_id, location_id, record_time)
                    VALUES (%s, %s, %s)
                """, (msg.robot_id, current_location_id, datetime.now()))
                conn.commit()

        except Exception as e:
            logger.error(f"로봇 위치(Pose) 업데이트 중 오류 발생: {e}")
            conn.rollback()
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


    def pickup_completed_callback(self, msg):
        logger.info(f"픽업 완료 이벤트 수신: Robot ID {msg.robot_id}, Task ID {msg.task_id}")
        
        # 명세서 12단계: "배송 중" 상태로 변경
        conn = db_manager.get_connection()
        if not conn: return
        try:
            conn.start_transaction()
            cursor = conn.cursor(dictionary=True)

            query = "UPDATE task SET task_status_id = 5, pickup_completion_time = %s WHERE id = %s"
            cursor.execute(query, (datetime.now(), msg.task_id))
            
            # 픽업 완료 시 로봇의 현재 위치는 '알 수 없음' 또는 특정 중간 지점으로 업데이트 할 수 있음.
            # 여기서는 NULL로 설정하여 로봇이 특정 장소에 있지 않음을 명시.
            self._update_robot_current_state(cursor, msg.robot_id, location_id=None)
            
            conn.commit()
            
            self.publish_task_state(msg.task_id, 5) # RC에게 상태 전파
            logger.info(f"Task {msg.task_id} 상태 '배송 중(5)'으로 업데이트 완료.")

        except Exception as e:
            logger.error(f"픽업 완료 처리 중 오류: {e}")
            if conn.in_transaction: conn.rollback()
        finally:
            if conn.is_connected():
                if 'cursor' in locals() and cursor: cursor.close()
                conn.close()

    def delivery_completed_callback(self, msg):
        logger.info(f"배송 완료 이벤트 수신: Robot ID {msg.robot_id}, Task ID {msg.task_id}")
        
        # 명세서 최종 단계: '수령 완료(7)' 상태로 변경
        conn = db_manager.get_connection()
        if not conn:
            logger.error(f"배송 완료 처리 실패 (DB 연결 불가): Task ID {msg.task_id}")
            return
            
        try:
            conn.start_transaction()
            cursor = conn.cursor(dictionary=True)

            query = "UPDATE task SET task_status_id = 7, task_completion_time = %s WHERE id = %s"
            cursor.execute(query, (datetime.now(), msg.task_id))

            # 작업 완료 후 로봇의 위치는 대기 장소 등으로 변경될 수 있음.
            # 여기서는 NULL로 설정.
            self._update_robot_current_state(cursor, msg.robot_id, location_id=None)

            conn.commit()
            
            self.publish_task_state(msg.task_id, 7) # RC에게 상태 전파
            logger.info(f"Task {msg.task_id} 최종 상태 '수령 완료(7)'로 업데이트 완료.")

        except Exception as e:
            logger.error(f"배송 완료 처리 중 오류: {e}")
            if conn.in_transaction: conn.rollback()
        finally:
            if conn.is_connected():
                if 'cursor' in locals() and cursor: cursor.close()
                conn.close()
        
    # --- Action/Service Call Methods (FastAPI -> RMS) ---
    # FastAPI의 동기적인 환경에서 ROS2의 비동기 함수를 호출하기 위한 인터페이스
    # 실제 연동 시에는 스레드 안전성을 고려한 추가적인 설계가 필요할 있음
    async def call_create_task_service(self, robot_id, target_location_id):
        """CreateTask 서비스를 비동기적으로 호출합니다."""
        if not self.create_task_cli.wait_for_service(timeout_sec=1.0):
            logger.error('CreateTask 서비스 서버를 찾을 수 없습니다.')
            return None
            
        req = CreateTask.Request()
        req.robot_id = robot_id
        req.target_location_id = target_location_id
        
        future = self.create_task_cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        
        return future.result()

    async def send_perform_task_goal(self, goal_data):
        """PerformTask 액션을 비동기적으로 호출합니다."""
        if not self._perform_task_ac.wait_for_server(timeout_sec=1.0):
            logger.error('PerformTask 액션 서버를 찾을 수 없습니다.')
            return None

        goal_msg = PerformTask.Goal(**goal_data)
        send_goal_future = self._perform_task_ac.send_goal_async(goal_msg)
        
        rclpy.spin_until_future_complete(self, send_goal_future)
        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:
            logger.error('PerformTask 액션 목표가 거부되었습니다.')
            return None
        
        get_result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, get_result_future)
        
        return get_result_future.result().result

def run_fastapi():
    """FastAPI 서버를 실행하는 함수"""
    logger.info('FastAPI 서버를 시작합니다. (호스트: 0.0.0.0, 포트: 8000)')
    uvicorn.run(app, host="0.0.0.0", port=8000)

def main(args=None):
    logger.info('Roomie RMS 시스템을 시작합니다.')
    
    # 1. FastAPI 서버를 별도 스레드에서 실행
    logger.info('FastAPI 서버 스레드를 생성합니다.')
    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.daemon = True
    fastapi_thread.start()

    # 2. ROS2 노드 실행
    logger.info('ROS2 노드를 초기화합니다.')
    rclpy.init(args=args)
    rms_node = RmsNode()
    app.state.rms_node = rms_node  # FastAPI 앱에 노드 인스턴스 저장
    
    try:
        logger.info('ROS2 노드 스핀을 시작합니다.')
        rclpy.spin(rms_node)
    except KeyboardInterrupt:
        logger.warning('사용자에 의해 시스템이 중단됩니다.')
    finally:
        logger.info('RMS 시스템을 종료합니다.')
        rms_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()