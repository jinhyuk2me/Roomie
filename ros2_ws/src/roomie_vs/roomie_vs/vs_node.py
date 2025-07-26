#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
import threading
import time
import numpy as np
import cv2
import cv2.aruco as aruco
from typing import Optional, Tuple, List

# ROS2 메시지 타입들
from geometry_msgs.msg import Point

# 커스텀 서비스
from roomie_msgs.srv import (
    ButtonStatus, 
    SetVSMode,
    ElevatorWidth,
    ElevatorStatus, 
    DoorStatus,
    SpaceAvailability,
    Location
)
from roomie_msgs.msg import TrackingEvent, Registered

# OpenNI2 환경변수 설정
import os

def setup_openni2_environment():
    """OpenNI2 실행을 위한 환경변수 설정"""
    openni_path = os.path.expanduser("~/Downloads/OpenNI_SDK_ROS2_v1.0.2_20220809_b32e47_linux/ros2_astra_camera/astra_camera/openni2_redist/x64")
    
    if not os.path.exists(openni_path):
        print(f"❌ OpenNI2 경로를 찾을 수 없습니다: {openni_path}")
        return False
    
    # 환경변수 설정
    os.environ['OPENNI2_REDIST'] = openni_path
    if 'LD_LIBRARY_PATH' in os.environ:
        os.environ['LD_LIBRARY_PATH'] += f":{openni_path}"
    else:
        os.environ['LD_LIBRARY_PATH'] = openni_path
    
    # PYTHONPATH에 사용자 라이브러리 경로 추가
    user_lib_path = "/home/jinhyuk2me/.local/lib/python3.12/site-packages"
    if 'PYTHONPATH' in os.environ:
        os.environ['PYTHONPATH'] += f":{user_lib_path}"
    else:
        os.environ['PYTHONPATH'] = user_lib_path
    
    print(f"✅ OpenNI2 환경변수 설정 완료: {openni_path}")
    return True

# 환경설정 먼저 실행
if not setup_openni2_environment():
    import sys
    sys.exit(1)

# 환경설정 후 OpenNI2 import
try:
    from primesense import openni2
    from primesense import _openni2 as c_api
    print("✅ primesense 모듈 import 성공")
except ImportError as e:
    print(f"❌ primesense 모듈 import 실패: {e}")
    print("pip install primesense --break-system-packages 명령으로 설치하세요")
    import sys
    sys.exit(1)

class OpenNI2Camera:
    """OpenNI2를 직접 사용한 안정적인 Astra 카메라 클래스"""
    
    def __init__(self, logger):
        self.logger = logger
        self.is_running = False
        self.device = None
        self.rgb_stream = None
        self.depth_stream = None
        
        # 카메라 내부 파라미터 (Astra 기본값)
        self.depth_fx = 570.3
        self.depth_fy = 570.3
        self.depth_cx = 320.0
        self.depth_cy = 240.0
        
        # 현재 프레임들
        self.current_depth = None
        self.current_color = None
        self.frame_lock = threading.Lock()
        
    def initialize(self) -> bool:
        """OpenNI2 카메라 초기화"""
        try:
            self.logger.info("OpenNI2 카메라 초기화 시작...")
            
            # OpenNI2 초기화
            openni2.initialize()
            self.logger.info("OpenNI2 초기화 완료")
            
            # 장치 열기
            self.device = openni2.Device.open_any()
            self.logger.info("장치 열기 완료")
            
            # 장치 정보 출력
            device_info = self.device.get_device_info()
            self.logger.info(f"장치: {device_info.name.decode()} ({device_info.vendor.decode()})")
            
            # RGB 스트림 생성
            try:
                self.rgb_stream = self.device.create_color_stream()
                self.rgb_stream.start()
                video_mode = self.rgb_stream.get_video_mode()
                self.logger.info(f"RGB 스트림: {video_mode.resolutionX}x{video_mode.resolutionY}@{video_mode.fps}fps")
            except Exception as e:
                self.logger.warning(f"RGB 스트림 생성 실패: {e}")
                self.rgb_stream = None
            
            # Depth 스트림 생성
            try:
                self.depth_stream = self.device.create_depth_stream()
                self.depth_stream.start()
                video_mode = self.depth_stream.get_video_mode()
                self.logger.info(f"Depth 스트림: {video_mode.resolutionX}x{video_mode.resolutionY}@{video_mode.fps}fps")
            except Exception as e:
                self.logger.warning(f"Depth 스트림 생성 실패: {e}")
                self.depth_stream = None
            
            if not self.rgb_stream and not self.depth_stream:
                self.logger.error("RGB와 Depth 스트림 모두 생성 실패")
                return False
            
            self.is_running = True
            self.logger.info("OpenNI2 카메라 초기화 완료!")
            return True
            
        except Exception as e:
            self.logger.error(f"OpenNI2 카메라 초기화 실패: {e}")
            return False
    
    def get_frames(self) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
        """OpenNI2에서 RGB와 Depth 프레임 획득"""
        if not self.is_running:
            raise RuntimeError("카메라가 초기화되지 않았습니다")
        
        try:
            depth_image = None
            color_image = None
            
            # RGB 프레임 획득
            if self.rgb_stream:
                try:
                    rgb_frame = self.rgb_stream.read_frame()
                    rgb_data = rgb_frame.get_buffer_as_uint8()
                    rgb_array = np.frombuffer(rgb_data, dtype=np.uint8)
                    
                    h = rgb_frame.height
                    w = rgb_frame.width
                    rgb_image = rgb_array.reshape((h, w, 3))
                    
                    # BGR로 변환
                    color_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
                    
                except Exception as e:
                    self.logger.warning(f"RGB 프레임 읽기 실패: {e}")
            
            # Depth 프레임 획득
            if self.depth_stream:
                try:
                    depth_frame = self.depth_stream.read_frame()
                    depth_data = depth_frame.get_buffer_as_uint16()
                    depth_array = np.frombuffer(depth_data, dtype=np.uint16)
                    
                    h = depth_frame.height
                    w = depth_frame.width  
                    depth_image = depth_array.reshape((h, w))
                    
                except Exception as e:
                    self.logger.warning(f"Depth 프레임 읽기 실패: {e}")
            
            # 현재 프레임 저장
            with self.frame_lock:
                if depth_image is not None:
                    self.current_depth = depth_image.copy()
                if color_image is not None:
                    self.current_color = color_image.copy()
            
            return depth_image, color_image
            
        except Exception as e:
            self.logger.error(f"프레임 획득 실패: {e}")
            raise RuntimeError(f"카메라 프레임 획득 실패: {e}")
    
    def pixel_to_3d(self, u: int, v: int, depth_mm: int) -> Tuple[float, float, float]:
        """2D 픽셀 좌표를 3D 월드 좌표로 변환"""
        if depth_mm <= 0:
            return 0.0, 0.0, 0.0
            
        z = depth_mm / 1000.0  # mm to meters
        x = (u - self.depth_cx) * z / self.depth_fx
        y = (v - self.depth_cy) * z / self.depth_fy
        
        return x, y, z
    
    def cleanup(self):
        """카메라 정리"""
        self.is_running = False
        
        try:
            if self.rgb_stream:
                self.rgb_stream.stop()
                self.rgb_stream = None
                
            if self.depth_stream:
                self.depth_stream.stop()
                self.depth_stream = None
                
            if self.device:
                self.device.close()
                self.device = None
                
            openni2.unload()
            self.logger.info("OpenNI2 카메라 정리 완료")
            
        except Exception as e:
            self.logger.warning(f"카메라 정리 중 에러: {e}")

class YOLOButtonDetector:
    """YOLO 기반 엘리베이터 객체 탐지 클래스"""
    
    def __init__(self, logger):
        self.logger = logger
        self.yolo_model = None
        
        # 4개 클래스 정의
        self.class_names = [
            'button', 'direction_light', 'display', 'door'
        ]
        
        # 클래스별 ID 매핑
        self.button_id_map = {
            'button': 'BUTTON',
        }
        
        # YOLO 모델 초기화
        self._initialize_yolo_model()
        
    def _initialize_yolo_model(self):
        """YOLO 모델 초기화 및 로딩"""
        try:
            from ultralytics import YOLO
            
            model_path = self._find_best_model()
            if model_path:
                self.yolo_model = YOLO(model_path)
                self.logger.info(f"엘리베이터 감지 모델 로딩 성공: {model_path}")
                return True
            else:
                self.logger.error("엘리베이터 감지 YOLO 모델을 찾을 수 없습니다")
                self.logger.error("training/best.pt 파일이 있는지 확인하세요")
                raise FileNotFoundError("엘리베이터 감지 YOLO 모델 파일을 찾을 수 없습니다")
                
        except ImportError:
            self.logger.error("ultralytics 패키지가 필요합니다: pip install ultralytics")
            raise ImportError("ultralytics 패키지를 설치하세요")
        except Exception as e:
            self.logger.error(f"YOLO 모델 초기화 실패: {e}")
            raise RuntimeError(f"YOLO 모델 로딩 실패: {e}")
    
    def _find_best_model(self):
        """엘리베이터 감지 YOLO 모델 찾기"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        possible_training_dirs = [
            os.path.join(script_dir, "..", "training"),
            os.path.join(os.path.expanduser("~"), "project_ws", "Roomie", "ros2_ws", "src", "roomie_vs", "training"),
            os.path.join(os.getcwd(), "ros2_ws", "src", "roomie_vs", "training"),
            "ros2_ws/src/roomie_vs/training"
        ]
        
        training_dir = None
        for candidate in possible_training_dirs:
            if os.path.exists(candidate):
                training_dir = candidate
                break
        
        if training_dir is None:
            self.logger.error("training 디렉토리를 찾을 수 없습니다")
            return None
            
        self.logger.info(f"엘리베이터 감지 모델 검색: {training_dir}")
        
        best_model_path = os.path.join(training_dir, "best.pt")
        if os.path.exists(best_model_path):
            self.logger.info(f"엘리베이터 감지 모델 발견: {best_model_path}")
            return best_model_path
        
        self.logger.error(f"엘리베이터 감지 모델을 찾을 수 없습니다: {best_model_path}")
        return None
        
    def detect_buttons(self, color_image: np.ndarray, depth_image: np.ndarray, conf_threshold: float = 0.7) -> List[dict]:
        """YOLO로 이미지에서 엘리베이터 객체들을 탐지"""
        if color_image is None or self.yolo_model is None:
            return []
            
        try:
            return self._detect_with_yolo(color_image, depth_image, conf_threshold)
        except Exception as e:
            self.logger.error(f"YOLO 버튼 탐지 에러: {e}")
            return []
    
    def _detect_with_yolo(self, color_image: np.ndarray, depth_image: np.ndarray, conf_threshold: float = 0.7) -> List[dict]:
        """YOLO 모델을 사용한 버튼 탐지"""
        try:
            results = self.yolo_model.predict(
                color_image, 
                conf=conf_threshold,
                verbose=False
            )
            
            buttons = []
            if results and len(results) > 0:
                result = results[0]
                
                if result.boxes is not None and len(result.boxes) > 0:
                    boxes = result.boxes.xyxy.cpu().numpy()
                    confs = result.boxes.conf.cpu().numpy()
                    classes = result.boxes.cls.cpu().numpy()
                    
                    for box, conf, cls in zip(boxes, confs, classes):
                        x1, y1, x2, y2 = box.astype(int)
                        center_x = int((x1 + x2) / 2)
                        center_y = int((y1 + y2) / 2)
                        width = x2 - x1
                        height = y2 - y1
                        radius = int(max(width, height) / 2)
                        
                        # 클래스 정보
                        class_id = int(cls)
                        class_name = self.class_names[class_id] if class_id < len(self.class_names) else f"unknown_{class_id}"
                        
                        # Depth 정보
                        depth_value = depth_image[center_y, center_x] if depth_image is not None else 1000
                        
                        # 버튼 눌림 상태 추정
                        is_pressed = False
                        button_id = None
                        
                        if class_name == 'button':
                            button_id = self.button_id_map.get(class_name, 'BUTTON')
                            if depth_image is not None:
                                is_pressed = self._check_button_pressed(depth_image, center_x, center_y, radius)
                        
                        buttons.append({
                            'center': (center_x, center_y),
                            'radius': radius,
                            'depth_mm': int(depth_value),
                            'is_pressed': is_pressed,
                            'class_name': class_name,
                            'class_id': class_id,
                            'button_id': button_id,
                            'confidence': float(conf),
                            'bbox': (x1, y1, x2, y2),
                            'is_button': class_name == 'button'
                        })
            
            self.logger.debug(f"엘리베이터 객체 탐지 결과: {len(buttons)}개")
            return buttons
            
        except Exception as e:
            self.logger.error(f"YOLO 탐지 에러: {e}")
            return []
    
    def _check_button_pressed(self, depth_image: np.ndarray, cx: int, cy: int, radius: int) -> bool:
        """버튼 눌림 상태 확인"""
        try:
            center_depth = depth_image[cy, cx]
            if center_depth <= 0:
                return False
            
            y1, y2 = max(0, cy-radius), min(depth_image.shape[0], cy+radius)
            x1, x2 = max(0, cx-radius), min(depth_image.shape[1], cx+radius)
            
            surrounding_region = depth_image[y1:y2, x1:x2]
            valid_depths = surrounding_region[surrounding_region > 0]
            
            if valid_depths.size < 5:
                return False
                
            surrounding_depth = np.mean(valid_depths)
            
            # 중심이 주변보다 깊으면 눌린 것으로 판단
            return center_depth > surrounding_depth + 10  # 10mm 차이
            
        except Exception:
            return False

class VSNode(Node):
    """OpenNI2 기반 Vision Service ROS2 노드"""
    
    def __init__(self):
        super().__init__('vs_node')
        
        # 카메라와 버튼 탐지기 초기화
        self.camera = OpenNI2Camera(self.get_logger())
        self.button_detector = YOLOButtonDetector(self.get_logger())
        
        # 이미지 처리 옵션
        self.flip_horizontal = True  # 좌우반전을 기본으로 켜기
        self.confidence_threshold = 0.7
        
        # ArUco 마커 감지 설정
        try:
            # OpenCV 버전 확인
            opencv_version = cv2.__version__
            self.get_logger().info(f"OpenCV 버전: {opencv_version}")
            
            # 여러 ArUco 사전 시도
            aruco_dicts_to_try = [
                (cv2.aruco.DICT_4X4_50, "DICT_4X4_50"),
                (cv2.aruco.DICT_4X4_100, "DICT_4X4_100"), 
                (cv2.aruco.DICT_4X4_250, "DICT_4X4_250"),
                (cv2.aruco.DICT_4X4_1000, "DICT_4X4_1000"),
                (cv2.aruco.DICT_5X5_50, "DICT_5X5_50"),
                (cv2.aruco.DICT_6X6_50, "DICT_6X6_50")
            ]
            
            # 첫 번째로 성공하는 사전 사용 (기본: DICT_ARUCO_ORIGINAL)
            self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
            self.aruco_dict_name = "DICT_ARUCO_ORIGINAL"
            
            # ArUco 감지 파라미터를 더 관대하게 설정
            self.aruco_params = cv2.aruco.DetectorParameters()
            
            # 매우 관대한 파라미터 설정
            self.aruco_params.adaptiveThreshWinSizeMin = 3
            self.aruco_params.adaptiveThreshWinSizeMax = 53  # 더 큰 윈도우
            self.aruco_params.adaptiveThreshWinSizeStep = 4
            self.aruco_params.adaptiveThreshConstant = 5    # 더 낮은 임계값
            
            # 마커 크기 허용 범위를 매우 넓게
            self.aruco_params.minMarkerPerimeterRate = 0.01  # 매우 작은 마커도 허용
            self.aruco_params.maxMarkerPerimeterRate = 8.0   # 매우 큰 마커도 허용
            
            # 다각형 근사를 매우 관대하게
            self.aruco_params.polygonalApproxAccuracyRate = 0.2
            
            # 코너 간 거리를 매우 작게
            self.aruco_params.minCornerDistanceRate = 0.005
            self.aruco_params.minMarkerDistanceRate = 0.005
            
            # 에러 허용을 매우 높게
            self.aruco_params.maxErroneousBitsInBorderRate = 0.5  # 50% 에러까지 허용
            self.aruco_params.errorCorrectionRate = 0.8  # 80% 에러 정정
            
            # 코너 정제 강화
            self.aruco_params.cornerRefinementMethod = cv2.aruco.CORNER_REFINE_SUBPIX
            self.aruco_params.cornerRefinementWinSize = 7
            self.aruco_params.cornerRefinementMaxIterations = 50
            self.aruco_params.cornerRefinementMinAccuracy = 0.01
            
            # 마커 경계 설정
            self.aruco_params.markerBorderBits = 1
            self.aruco_params.perspectiveRemovePixelPerCell = 8  # 더 높은 해상도
            self.aruco_params.perspectiveRemoveIgnoredMarginPerCell = 0.05  # 더 작은 마진
            
            # Otsu 임계값 설정
            self.aruco_params.minOtsuStdDev = 2.0  # 더 낮은 표준편차
            
            # ArucoDetector 생성
            self.aruco_detector = cv2.aruco.ArucoDetector(self.aruco_dict, self.aruco_params)
            self.aruco_api_version = "4.12+"
            
            self.get_logger().info(f"ArUco 초기화 성공 (사전: {self.aruco_dict_name}, 관대한 파라미터)")
                
        except Exception as e:
            self.get_logger().warning(f"ArUco 초기화 실패: {e}")
            self.aruco_dict = None
            self.aruco_params = None
            self.aruco_detector = None
            self.aruco_api_version = "none"
        
        # 마지막으로 감지된 위치 저장
        self.last_detected_location_id = 0  # 기본값: LOB_WAITING
        self.last_detection_time = None
        
        # ArUco 마커 ID와 location_id 직접 매핑 (interface 문서 기준)
        self.aruco_to_location = {
            0: 0,     # LOB_WAITING
            1: 1,     # LOB_CALL  
            2: 2,     # RES_PICKUP
            3: 3,     # RES_CALL
            4: 4,     # SUP_PICKUP
            5: 5,     # ELE_1
            6: 6,     # ELE_2
            101: 101, # ROOM_101
            102: 102, # ROOM_102
            201: 201, # ROOM_201
            202: 202, # ROOM_202
        }
        
        # VS 모드 상태 관리
        self.current_mode_id = 0
        self.mode_names = {
            0: "대기모드 (후방)",
            1: "등록모드 (후방)", 
            2: "추적모드 (후방)",
            3: "엘리베이터 외부 모드 (전방)",
            4: "엘리베이터 내부 모드 (전방)",
            5: "일반모드 (전방)",
            100: "배송 시뮬레이션 모드",
            101: "호출 시뮬레이션 모드",
            102: "길안내 시뮬레이션 모드",
            103: "복귀 시뮬레이션 모드",
            104: "엘리베이터 시뮬레이션 모드"
        }
        
        # 시뮬레이션 모드별 시나리오 카운터
        self.simulation_counters = {
            100: 0,  # 배송 시뮬레이션
            101: 0,  # 호출 시뮬레이션
            102: 0,  # 길안내 시뮬레이션
            103: 0,  # 복귀 시뮬레이션
            104: 0   # 엘리베이터 시뮬레이션
        }
        
        # 카메라 초기화
        self.camera_initialized = False
        if self.camera.initialize():
            self.camera_initialized = True
            self.get_logger().info("OpenNI2 Astra 카메라 초기화 성공")
        else:
            self.get_logger().error("OpenNI2 Astra 카메라 초기화 실패")
            raise RuntimeError("실제 카메라 초기화 실패")
        
        # ROS2 서비스들 (/vs/command/*)
        self.get_logger().info("VS 서비스 인터페이스 초기화 중...")
        
        self.set_mode_service = self.create_service(
            SetVSMode,
            '/vs/command/set_vs_mode',
            self.set_vs_mode_callback
        )
        
        self.elevator_width_service = self.create_service(
            ElevatorWidth,
            '/vs/command/elevator_width',
            self.elevator_width_callback
        )
        
        self.button_status_service = self.create_service(
            ButtonStatus, 
            '/vs/command/button_status', 
            self.button_status_callback
        )
        
        self.elevator_status_service = self.create_service(
            ElevatorStatus,
            '/vs/command/elevator_status',
            self.elevator_status_callback
        )
        
        self.door_status_service = self.create_service(
            DoorStatus,
            '/vs/command/door_status',
            self.door_status_callback
        )
        
        self.space_availability_service = self.create_service(
            SpaceAvailability,
            '/vs/command/space_availability',
            self.space_availability_callback
        )
        
        self.location_service = self.create_service(
            Location,
            '/vs/command/location',
            self.location_callback
        )
        
        # ROS2 토픽 퍼블리셔들
        
        self.tracking_event_pub = self.create_publisher(
            TrackingEvent,
            '/vs/tracking_event',
            10
        )
        
        self.registered_pub = self.create_publisher(
            Registered,
            '/vs/registered',
            10
        )
        
        self.get_logger().info("모든 VS 인터페이스 초기화 완료!")
        self.get_logger().info("구현된 서비스 7개: set_vs_mode, elevator_width, button_status, elevator_status, door_status, space_availability, location")
        self.get_logger().info("구현된 토픽 2개: tracking_event, registered")
        self.get_logger().info("ArUco 마커 기반 위치 감지 시스템 활성화")
        self.get_logger().info("OpenNI2 기반 VS Node 초기화 완료!")
    
    def detect_and_update_location(self) -> int:
        """ArUco 마커를 감지하여 위치 업데이트 및 현재 위치 반환"""
        if self.aruco_detector is None:
            self.get_logger().debug("ArUco 시스템이 초기화되지 않음")
            return self.last_detected_location_id
        
        try:
            # 현재 카메라 프레임 획득
            with self.camera.frame_lock:
                current_color = self.camera.current_color
            
            if current_color is None:
                self.get_logger().debug("카메라 프레임이 없음")
                return self.last_detected_location_id
            
            # 좌우반전 적용 (A키 테스트와 동일하게)
            processed_image = current_color.copy()
            if self.flip_horizontal:
                processed_image = cv2.flip(processed_image, 1)
            
            # 그레이스케일 변환
            gray = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
            
            # A키 테스트와 동일한 관대한 파라미터로 감지
            test_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
            test_params = cv2.aruco.DetectorParameters()
            test_params.minMarkerPerimeterRate = 0.03
            test_params.maxMarkerPerimeterRate = 4.0
            test_params.polygonalApproxAccuracyRate = 0.1
            test_params.maxErroneousBitsInBorderRate = 0.35
            test_params.errorCorrectionRate = 0.6
            test_detector = cv2.aruco.ArucoDetector(test_dict, test_params)
            
            # ArUco 마커 감지 (A키 테스트와 동일한 방식)
            corners, ids, rejected = test_detector.detectMarkers(gray)
            
            # 조용한 자동 감지 (로그 최소화)
            
            if ids is not None and len(ids) > 0:
                # 첫 번째 감지된 마커 사용
                detected_id = int(ids[0][0])
                
                # 매핑된 location_id 확인
                if detected_id in self.aruco_to_location:
                    new_location_id = self.aruco_to_location[detected_id]
                    
                    # 새로운 위치가 이전과 다르면 업데이트
                    if new_location_id != self.last_detected_location_id:
                        old_location = self.last_detected_location_id
                        self.last_detected_location_id = new_location_id
                        self.last_detection_time = self.get_clock().now()
                        
                        location_names = {
                            0: "LOB_WAITING", 1: "LOB_CALL", 2: "RES_PICKUP", 3: "RES_CALL",
                            4: "SUP_PICKUP", 5: "ELE_1", 6: "ELE_2", 101: "ROOM_101",
                            102: "ROOM_102", 201: "ROOM_201", 202: "ROOM_202"
                        }
                        old_name = location_names.get(old_location, f"UNKNOWN({old_location})")
                        new_name = location_names.get(new_location_id, f"UNKNOWN({new_location_id})")
                        
                        self.get_logger().info(f"🎯 위치 변경: {old_name} → {new_name} (ArUco 마커 {detected_id})")
                    else:
                        # 같은 위치 재확인 (조용하게)
                        self.last_detection_time = self.get_clock().now()
                    
                    return self.last_detected_location_id
                else:
                    self.get_logger().warning(f"⚠️ 알 수 없는 ArUco 마커: {detected_id} (매핑 테이블에 없음)")
                    self.get_logger().info(f"지원되는 마커 ID: {list(self.aruco_to_location.keys())}")
                    return self.last_detected_location_id
            else:
                # 마커가 감지되지 않음 - 마지막 위치 유지
                return self.last_detected_location_id
                
        except Exception as e:
            self.get_logger().error(f"❌ ArUco 마커 감지 에러: {e}")
            import traceback
            self.get_logger().error(f"스택 트레이스: {traceback.format_exc()}")
            return self.last_detected_location_id
    
    def test_aruco_detection(self):
        """ArUco 감지 테스트 함수 ('A' 키용) - 모든 ArUco 사전 시도"""
        try:
            # 현재 카메라 프레임 획득
            with self.camera.frame_lock:
                current_color = self.camera.current_color
            
            if current_color is None:
                self.get_logger().warning("⚠️ 카메라 프레임이 없습니다")
                return
            
            # 좌우반전 적용
            processed_image = current_color.copy()
            if self.flip_horizontal:
                processed_image = cv2.flip(processed_image, 1)
                self.get_logger().info("🔄 좌우반전 적용됨")
            
            # 그레이스케일 변환
            gray = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
            self.get_logger().info(f"📊 이미지 크기: {gray.shape}, 타입: {gray.dtype}")
            
            # 모든 주요 ArUco 사전 시도
            aruco_dicts_to_test = [
                (cv2.aruco.DICT_4X4_50, "DICT_4X4_50"),
                (cv2.aruco.DICT_4X4_100, "DICT_4X4_100"),
                (cv2.aruco.DICT_4X4_250, "DICT_4X4_250"),
                (cv2.aruco.DICT_4X4_1000, "DICT_4X4_1000"),
                (cv2.aruco.DICT_5X5_50, "DICT_5X5_50"),
                (cv2.aruco.DICT_5X5_100, "DICT_5X5_100"),
                (cv2.aruco.DICT_5X5_250, "DICT_5X5_250"),
                (cv2.aruco.DICT_5X5_1000, "DICT_5X5_1000"),
                (cv2.aruco.DICT_6X6_50, "DICT_6X6_50"),
                (cv2.aruco.DICT_6X6_100, "DICT_6X6_100"),
                (cv2.aruco.DICT_6X6_250, "DICT_6X6_250"),
                (cv2.aruco.DICT_6X6_1000, "DICT_6X6_1000"),
                (cv2.aruco.DICT_7X7_50, "DICT_7X7_50"),
                (cv2.aruco.DICT_7X7_100, "DICT_7X7_100"),
                (cv2.aruco.DICT_7X7_250, "DICT_7X7_250"),
                (cv2.aruco.DICT_7X7_1000, "DICT_7X7_1000"),
                (cv2.aruco.DICT_ARUCO_ORIGINAL, "DICT_ARUCO_ORIGINAL"),
            ]
            
            self.get_logger().info(f"🔍 모든 ArUco 사전 테스트 시작 ({len(aruco_dicts_to_test)}개)")
            
            detected_in_dicts = []
            
            for dict_id, dict_name in aruco_dicts_to_test:
                try:
                    # 테스트용 ArUco 사전과 detector 생성
                    test_dict = cv2.aruco.getPredefinedDictionary(dict_id)
                    test_params = cv2.aruco.DetectorParameters()
                    
                    # 관대한 파라미터 설정
                    test_params.minMarkerPerimeterRate = 0.03
                    test_params.maxMarkerPerimeterRate = 4.0
                    test_params.polygonalApproxAccuracyRate = 0.1
                    test_params.maxErroneousBitsInBorderRate = 0.35
                    test_params.errorCorrectionRate = 0.6
                    
                    test_detector = cv2.aruco.ArucoDetector(test_dict, test_params)
                    
                    # ArUco 마커 감지
                    corners, ids, rejected = test_detector.detectMarkers(gray)
                    
                    detected_count = len(ids) if ids is not None else 0
                    rejected_count = len(rejected) if rejected is not None else 0
                    
                    if detected_count > 0:
                        self.get_logger().info(f"🎯 {dict_name}: {detected_count}개 마커 감지!")
                        
                        # 감지된 마커 ID들 출력
                        marker_ids = [int(id[0]) for id in ids]
                        self.get_logger().info(f"   감지된 마커 ID: {marker_ids}")
                        
                        # 1번 마커가 있는지 확인
                        if 1 in marker_ids:
                            self.get_logger().info(f"   ✅ 1번 마커 발견! {dict_name}을 사용하세요!")
                            detected_in_dicts.append((dict_name, marker_ids))
                        else:
                            detected_in_dicts.append((dict_name, marker_ids))
                    else:
                        if rejected_count > 0:
                            self.get_logger().debug(f"   {dict_name}: 0개 감지, {rejected_count}개 거부됨")
                        
                except Exception as e:
                    self.get_logger().debug(f"   {dict_name}: 테스트 실패 - {e}")
            
            # 결과 요약
            self.get_logger().info("📋 테스트 결과 요약:")
            if detected_in_dicts:
                self.get_logger().info(f"✅ 마커가 감지된 사전들 ({len(detected_in_dicts)}개):")
                for dict_name, marker_ids in detected_in_dicts:
                    self.get_logger().info(f"   {dict_name}: 마커 ID {marker_ids}")
                    if 1 in marker_ids:
                        self.get_logger().info(f"   👆 {dict_name}에서 1번 마커 발견! 이 사전을 사용하세요!")
            else:
                self.get_logger().warning("❌ 어떤 ArUco 사전에서도 마커를 감지하지 못했습니다")
                self.get_logger().info("💡 확인사항:")
                self.get_logger().info("   1. 마커가 화면에 선명하게 보이는가?")
                self.get_logger().info("   2. 조명이 충분한가?")
                self.get_logger().info("   3. 마커가 평평하고 왜곡되지 않았는가?")
                self.get_logger().info("   4. 마커 크기가 너무 작거나 크지 않은가?")
                
        except Exception as e:
            self.get_logger().error(f"❌ ArUco 테스트 에러: {e}")
            import traceback
            self.get_logger().error(f"스택 트레이스: {traceback.format_exc()}")
    
    def _add_aruco_visualization(self, image: np.ndarray):
        """ArUco 마커 감지 결과를 이미지에 표시"""
        if self.aruco_detector is None:
            return
        
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # A키 테스트와 동일한 관대한 파라미터로 감지
            test_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
            test_params = cv2.aruco.DetectorParameters()
            test_params.minMarkerPerimeterRate = 0.03
            test_params.maxMarkerPerimeterRate = 4.0
            test_params.polygonalApproxAccuracyRate = 0.1
            test_params.maxErroneousBitsInBorderRate = 0.35
            test_params.errorCorrectionRate = 0.6
            test_detector = cv2.aruco.ArucoDetector(test_dict, test_params)
            
            # ArUco 마커 감지
            corners, ids, rejected = test_detector.detectMarkers(gray)
            
            if ids is not None:
                # 감지된 마커 그리기
                cv2.aruco.drawDetectedMarkers(image, corners, ids)
                
                # 마커 정보 텍스트 표시
                cv2.putText(image, f"ArUco Markers: {len(ids)}", (10, 160), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
                
                # 첫 번째 마커의 location_id 표시
                if len(ids) > 0:
                    marker_id = int(ids[0][0])
                    location_id = self.aruco_to_location.get(marker_id, -1)
                    if location_id != -1:
                        location_names = {
                            0: "LOB_WAITING", 1: "LOB_CALL", 2: "RES_PICKUP", 3: "RES_CALL",
                            4: "SUP_PICKUP", 5: "ELE_1", 6: "ELE_2", 101: "ROOM_101",
                            102: "ROOM_102", 201: "ROOM_201", 202: "ROOM_202"
                        }
                        location_name = location_names.get(location_id, f"ID_{location_id}")
                        cv2.putText(image, f"Location: {location_name}", (10, 185), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        except Exception as e:
            pass
    
    def button_status_callback(self, request, response):
        """버튼 상태 요청 처리"""
        try:
            self.get_logger().info(f"버튼 상태 요청: robot_id={request.robot_id}, button_ids={request.button_ids}")
            
            response.robot_id = request.robot_id
            n_buttons = len(request.button_ids)
            
            if n_buttons == 0:
                response.xs = []
                response.ys = []
                response.depths = []
                response.is_pressed = []
                response.timestamp = []
                return response

            xs, ys, depths, is_pressed, timestamps = [], [], [], [], []
            
            try:
                # 현재 프레임 획득
                with self.camera.frame_lock:
                    current_depth = self.camera.current_depth
                    current_color = self.camera.current_color
                
                # 이미지 좌우반전
                if self.flip_horizontal:
                    if current_color is not None:
                        current_color = cv2.flip(current_color, 1)
                    if current_depth is not None:
                        current_depth = cv2.flip(current_depth, 1)
                
                if current_color is not None:
                    # YOLO로 엘리베이터 객체 탐지
                    detected_objects = self.button_detector.detect_buttons(current_color, current_depth, self.confidence_threshold)
                    
                    # 'button' 클래스 객체들만 필터링
                    detected_buttons = [obj for obj in detected_objects if obj.get('class_name') == 'button']
                    
                    for i, button_id in enumerate(request.button_ids):
                        timestamp = self.get_clock().now().to_msg()
                        
                        if i < len(detected_buttons):
                            btn = detected_buttons[i]
                            center = btn['center']
                            
                            # 3D 좌표로 변환
                            x_3d = (center[0] - 320.0) / 570.3 * (btn['depth_mm'] / 1000.0)
                            y_3d = (center[1] - 240.0) / 570.3 * (btn['depth_mm'] / 1000.0)
                            z_3d = btn['depth_mm'] / 1000.0
                            
                            xs.append(float(x_3d))
                            ys.append(float(y_3d))
                            depths.append(float(z_3d))
                            is_pressed.append(bool(btn['is_pressed']))
                            timestamps.append(timestamp)
                            
                            confidence = btn.get('confidence', 1.0)
                            self.get_logger().info(f"버튼 탐지 - button #{i+1}: "
                                                 f"x={x_3d:.3f}, y={y_3d:.3f}, z={z_3d:.3f}, "
                                                 f"pressed={btn['is_pressed']}, conf={confidence:.2f}")
                        else:
                            # 더미값 사용
                            dummy_x = 0.1 + (len(xs) * 0.05)
                            dummy_y = 0.2 + (len(xs) * 0.03)
                            dummy_z = 1.0
                            
                            xs.append(float(dummy_x))
                            ys.append(float(dummy_y))
                            depths.append(float(dummy_z))
                            is_pressed.append(bool(False))
                            timestamps.append(timestamp)
                            
                            self.get_logger().info(f"요청된 버튼 #{i+1} 미탐지 - 더미값 사용")
                else:
                    self.get_logger().warning("카메라 프레임이 없음 - 더미값 사용")
                    for i, button_id in enumerate(request.button_ids):
                        xs.append(float(0.1 + i * 0.05))
                        ys.append(float(0.2 + i * 0.03))
                        depths.append(float(0.8 + i * 0.1))
                        is_pressed.append(bool(False))
                        timestamps.append(self.get_clock().now().to_msg())
                        
            except Exception as detection_error:
                self.get_logger().error(f"버튼 탐지 중 에러: {detection_error}")
                # 탐지 실패 시 더미값 사용
                for i, button_id in enumerate(request.button_ids):
                    xs.append(float(0.1 + i * 0.05))
                    ys.append(float(0.2 + i * 0.03))
                    depths.append(float(0.8 + i * 0.1))
                    is_pressed.append(bool(False))
                    timestamps.append(self.get_clock().now().to_msg())
                    
            response.success = True
            response.xs = xs
            response.ys = ys
            response.depths = depths
            response.is_pressed = is_pressed
            response.timestamp = timestamps
            
            self.get_logger().info(f"엘리베이터 버튼 상태 응답 완료: {len(xs)}개 버튼")
                
        except Exception as e:
            self.get_logger().error(f"버튼 상태 서비스 에러: {e}")
            response.robot_id = request.robot_id
            response.success = False
            response.xs = []
            response.ys = []
            response.depths = []
            response.is_pressed = []
            response.timestamp = []
        
        return response
    
    # 토픽 퍼블리시 메소드들
    
    def publish_tracking_event(self, robot_id: int, tracking_event_id: int, task_id: int = 1):
        """추적 이벤트 발행 (추적모드에서만 동작)"""
        try:
            if self.current_mode_id != 2:
                current_mode = self.mode_names.get(self.current_mode_id, "알 수 없음")
                self.get_logger().warning(f"추적 이벤트 발행 실패: 현재 모드가 '{current_mode}'입니다")
                return False
            
            msg = TrackingEvent()
            msg.robot_id = robot_id
            msg.tracking_event_id = tracking_event_id
            msg.task_id = task_id
            msg.timestamp = self.get_clock().now().to_msg()
            
            self.tracking_event_pub.publish(msg)
            
            event_names = {
                0: "slow_down",
                1: "maintain", 
                2: "lost",
                3: "resume"
            }
            event_name = event_names.get(tracking_event_id, f"unknown({tracking_event_id})")
            self.get_logger().info(f"추적 이벤트 발행: {event_name} (robot_id={robot_id}, task_id={task_id})")
            return True
            
        except Exception as e:
            self.get_logger().error(f"추적 이벤트 발행 에러: {e}")
            return False
    
    def publish_registered_event(self, robot_id: int):
        """추적 대상 등록 완료 이벤트 발행 (등록모드에서만 동작)"""
        try:
            if self.current_mode_id != 1:
                current_mode = self.mode_names.get(self.current_mode_id, "알 수 없음")
                self.get_logger().warning(f"등록 완료 이벤트 발행 실패: 현재 모드가 '{current_mode}'입니다")
                return False
            
            msg = Registered()
            msg.robot_id = robot_id
            msg.timestamp = self.get_clock().now().to_msg()
            
            self.registered_pub.publish(msg)
            self.get_logger().info(f"등록 완료 이벤트 발행: robot_id={robot_id}")
            return True
            
        except Exception as e:
            self.get_logger().error(f"등록 완료 이벤트 발행 에러: {e}")
            return False
    
    def simulate_tracking_sequence(self, robot_id: int = 1, task_id: int = 1):
        """추적 시뮬레이션 시퀀스"""
        import threading
        import time
        
        def tracking_simulation():
            self.get_logger().info(f"추적 시뮬레이션 시작: robot_id={robot_id}")
            
            # 등록모드로 자동 전환
            old_mode_id = self.current_mode_id
            old_mode_name = self.mode_names.get(old_mode_id, "알 수 없음")
            
            self.get_logger().info(f"자동 모드 전환: {old_mode_name} → 등록모드")
            self.current_mode_id = 1
            
            time.sleep(1)
            
            # 등록 완료 이벤트 발행
            self.get_logger().info("[1/6] 등록 완료 이벤트 발행")
            if self.publish_registered_event(robot_id):
                self.get_logger().info("등록 완료")
            
            time.sleep(2)
            
            # 추적모드로 자동 전환
            self.get_logger().info("자동 모드 전환: 등록모드 → 추적모드")
            self.current_mode_id = 2
            
            time.sleep(1)
            
            # 추적 시퀀스 실행
            tracking_events = [
                (1, "maintain - 정상 추적"),
                (0, "slow_down - 속도 감소 요청"),
                (1, "maintain - 추적 재개"),
                (2, "lost - 추적 대상 상실"),
                (3, "resume - 추적 복구")
            ]
            
            for i, (event_id, description) in enumerate(tracking_events):
                time.sleep(2)
                self.get_logger().info(f"[{i+2}/6] {description}")
                if self.publish_tracking_event(robot_id, event_id, task_id):
                    self.get_logger().info(f"추적 이벤트 발행 성공")
            
            # 원래 모드로 복원
            time.sleep(1)
            if old_mode_id != self.current_mode_id:
                self.get_logger().info(f"모드 복원: 추적모드 → {old_mode_name}")
                self.current_mode_id = old_mode_id
            
            self.get_logger().info("추적 시뮬레이션 완료")
        
        threading.Thread(target=tracking_simulation, daemon=True).start()
    
    def set_vs_mode_callback(self, request, response):
        """VS 모드 설정 처리"""
        try:
            self.get_logger().info(f"VS 모드 설정 요청: robot_id={request.robot_id}, mode_id={request.mode_id}")
            
            if request.mode_id not in self.mode_names:
                self.get_logger().error(f"잘못된 모드 ID: {request.mode_id}")
                response.robot_id = request.robot_id
                response.success = False
                return response
            
            old_mode = self.mode_names.get(self.current_mode_id, "알 수 없음")
            new_mode = self.mode_names[request.mode_id]
            
            self.current_mode_id = request.mode_id
            
            response.robot_id = request.robot_id
            response.success = True
            
            self.get_logger().info(f"VS 모드 변경: {old_mode} → {new_mode}")
            
            # 시뮬레이션 모드 초기화
            if request.mode_id in self.simulation_counters:
                self.simulation_counters[request.mode_id] = 0
                
        except Exception as e:
            self.get_logger().error(f"VS 모드 설정 에러: {e}")
            response.robot_id = request.robot_id
            response.success = False
        
        return response
    
    def elevator_width_callback(self, request, response):
        """엘리베이터 입구 너비 감지 처리"""
        try:
            self.get_logger().info(f"엘리베이터 너비 감지 요청: robot_id={request.robot_id}")
            
            dummy_left = -0.85
            dummy_right = 0.85
            
            response.robot_id = request.robot_id
            response.success = True
            response.left_boundary = float(dummy_left)
            response.right_boundary = float(dummy_right)
            
            self.get_logger().info(f"엘리베이터 너비: left={dummy_left:.3f}m, right={dummy_right:.3f}m")
                
        except Exception as e:
            self.get_logger().error(f"엘리베이터 너비 감지 에러: {e}")
            response.robot_id = request.robot_id
            response.success = False
            response.left_boundary = 0.0
            response.right_boundary = 0.0
        
        return response
    
    def elevator_status_callback(self, request, response):
        """엘리베이터 위치 및 방향 감지 처리"""
        try:
            self.get_logger().info(f"엘리베이터 상태 감지 요청: robot_id={request.robot_id}")
            
            import random
            dummy_direction = random.choice([0, 1])
            dummy_position = random.choice([1, 2, 3])
            
            response.robot_id = request.robot_id
            response.success = True
            response.direction = dummy_direction
            response.position = dummy_position
            
            direction_str = "상행" if dummy_direction == 0 else "하행"
            self.get_logger().info(f"엘리베이터 상태: {direction_str}, {dummy_position}층")
                
        except Exception as e:
            self.get_logger().error(f"엘리베이터 상태 감지 에러: {e}")
            response.robot_id = request.robot_id
            response.success = False
            response.direction = 0
            response.position = 1
        
        return response
    
    def door_status_callback(self, request, response):
        """문 열림 감지 처리"""
        try:
            self.get_logger().info(f"문 상태 감지 요청: robot_id={request.robot_id}")
            
            import random
            dummy_door_opened = random.choice([True, False])
            
            response.robot_id = request.robot_id
            response.success = True
            response.door_opened = dummy_door_opened
            
            door_str = "열림" if dummy_door_opened else "닫힘"
            self.get_logger().info(f"문 상태: {door_str}")
                
        except Exception as e:
            self.get_logger().error(f"문 상태 감지 에러: {e}")
            response.robot_id = request.robot_id
            response.success = False
            response.door_opened = False
        
        return response
    
    def space_availability_callback(self, request, response):
        """엘리베이터 탑승/하차시 공간 확보 여부 감지 처리"""
        try:
            self.get_logger().info(f"공간 가용성 감지 요청: robot_id={request.robot_id}")
            
            import random
            dummy_space_available = random.choice([True, False])
            
            response.robot_id = request.robot_id
            response.success = True
            response.space_availability = dummy_space_available
            
            space_str = "확보됨" if dummy_space_available else "확보 안됨"
            self.get_logger().info(f"공간 가용성: {space_str}")
                
        except Exception as e:
            self.get_logger().error(f"공간 가용성 감지 에러: {e}")
            response.robot_id = request.robot_id
            response.success = False
            response.space_availability = False
        
        return response
    
    def location_callback(self, request, response):
        """현재 위치 감지 처리"""
        try:
            self.get_logger().info(f"위치 감지 요청: robot_id={request.robot_id}")
            
            response.robot_id = request.robot_id
            response.success = True
            
            # 시뮬레이션 모드별 위치 시나리오 처리
            if self.current_mode_id == 100:  # 배송 시뮬레이션
                counter = self.simulation_counters[100]
                if counter == 0:
                    location_id = 2  # RES_PICKUP
                    self.get_logger().info("배송 시뮬레이션: 픽업 장소 도착")
                elif counter == 1:
                    location_id = 101  # ROOM_101
                    self.get_logger().info("배송 시뮬레이션: 101호 도착")
                else:
                    location_id = 101  # ROOM_101 유지
                    self.get_logger().info("배송 시뮬레이션: 101호 대기 중")
                
                self.simulation_counters[100] += 1
                response.location_id = location_id
                
            elif self.current_mode_id == 103:  # 복귀 시뮬레이션
                counter = self.simulation_counters[103]
                if counter == 0:
                    location_id = 0  # LOB_WAITING
                    self.get_logger().info("복귀 시뮬레이션: 로비 대기 위치 도착")
                else:
                    location_id = 0  # LOB_WAITING 유지
                    self.get_logger().info("복귀 시뮬레이션: 로비 대기 중")
                
                self.simulation_counters[103] += 1
                response.location_id = location_id
                
            else:  # 일반 모드 - ArUco 마커 기반 위치
                current_location = self.detect_and_update_location()
                response.location_id = current_location
                
                location_names = {
                    0: "LOB_WAITING", 1: "LOB_CALL", 2: "RES_PICKUP", 3: "RES_CALL",
                    4: "SUP_PICKUP", 5: "ELE_1", 6: "ELE_2", 101: "ROOM_101",
                    102: "ROOM_102", 201: "ROOM_201", 202: "ROOM_202"
                }
                location_name = location_names.get(current_location, f"UNKNOWN({current_location})")
                
                # 마지막 감지 시간 정보 포함
                if self.last_detection_time:
                    time_diff = (self.get_clock().now() - self.last_detection_time).nanoseconds / 1e9
                    self.get_logger().info(f"현재 위치: {location_name} (마지막 감지: {time_diff:.1f}초 전)")
                else:
                    self.get_logger().info(f"현재 위치: {location_name} (초기값)")
                
        except Exception as e:
            self.get_logger().error(f"위치 감지 에러: {e}")
            response.robot_id = request.robot_id
            response.success = False
            response.location_id = self.last_detected_location_id
        
        return response

    def _draw_buttons_on_image(self, image: np.ndarray, buttons: List[dict]) -> np.ndarray:
        """YOLO로 탐지된 객체들을 이미지에 시각화"""
        import cv2
        
        for i, button in enumerate(buttons):
            center = button['center']
            is_pressed = button['is_pressed']
            depth_mm = button['depth_mm']
            class_name = button.get('class_name', f'btn_{i+1}')
            confidence = button.get('confidence', 1.0)
            bbox = button.get('bbox', None)
            
            # YOLO 바운딩박스 그리기
            if bbox and len(bbox) == 4:
                x1, y1, x2, y2 = bbox
                color = (0, 255, 0) if not is_pressed else (255, 0, 0)
                cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
                
                # 클래스 이름과 신뢰도 표시
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(image, label, (x1, y1-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                
                # 거리 정보 표시
                distance_text = f"{depth_mm}mm"
                cv2.putText(image, distance_text, (center[0]-20, center[1]+30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
                
                # 눌림 상태 표시
                if is_pressed:
                    pressed_text = "PRESSED"
                    cv2.putText(image, pressed_text, (center[0]-30, center[1]+50), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        return image

    def _add_info_text(self, image: np.ndarray, buttons: List[dict]):
        """YOLO 탐지 결과 및 시스템 정보를 영상에 표시"""
        import cv2
        
        # 상단에 제목
        cv2.putText(image, "Roomie Vision System v2 (Elevator Objects)", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
        
        # YOLO 모델 상태 및 설정 표시
        model_status = "✅" if self.button_detector.yolo_model else "❌"
        flip_status = "ON" if self.flip_horizontal else "OFF"
        cv2.putText(image, f"YOLO {model_status} | Flip:{flip_status} | Conf:{self.confidence_threshold}(High)", (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # 탐지된 객체 수
        cv2.putText(image, f"Objects Detected: {len(buttons)}", (10, 85), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        
        # 탐지된 엘리베이터 객체 분류 표시
        if buttons:
            object_counts = {}
            for btn in buttons:
                class_name = btn.get('class_name', 'unknown')
                object_counts[class_name] = object_counts.get(class_name, 0) + 1
            
            if object_counts:
                counts_text = ", ".join([f"{k}:{v}" for k, v in object_counts.items()])
                cv2.putText(image, f"Objects: {counts_text}", (10, 110), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128, 255, 128), 1)
        
        # 눌린 버튼 표시
        pressed_buttons = []
        for btn in buttons:
            if btn['is_pressed'] and btn.get('class_name') == 'button':
                pressed_buttons.append("BUTTON")
        
        if pressed_buttons:
            pressed_text = f"Pressed: {len(pressed_buttons)} button(s)"
            cv2.putText(image, pressed_text, (10, 135), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        
        # ArUco 마커 시각화 추가
        self._add_aruco_visualization(image)
        
        # 현재 위치 정보 표시
        location_names = {
            0: "LOB_WAITING", 1: "LOB_CALL", 2: "RES_PICKUP", 3: "RES_CALL",
            4: "SUP_PICKUP", 5: "ELE_1", 6: "ELE_2", 101: "ROOM_101",
            102: "ROOM_102", 201: "ROOM_201", 202: "ROOM_202"
        }
        current_location_name = location_names.get(self.last_detected_location_id, f"ID_{self.last_detected_location_id}")
        cv2.putText(image, f"Current Location: {current_location_name}", (10, 210), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 128, 0), 2)
        
        # 종료 안내
        cv2.putText(image, "ESC:Exit, B:Info, M:Status, F:Flip, C:Conf, A:ArUco Test", (10, image.shape[0]-20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)

    def __del__(self):
        """소멸자 - 카메라 정리"""
        if hasattr(self, 'camera'):
            self.camera.cleanup()

def main(args=None):
    rclpy.init(args=args)
    
    try:
        node = VSNode()
        
        # 메인 쓰레드에서 GUI와 ROS2를 함께 처리
        node.get_logger().info("메인 쓰레드에서 GUI 시작!")
        
        import cv2
        frame_count = 0
        
        try:
            while rclpy.ok():
                frame_count += 1
                
                # GUI 처리를 우선순위로
                try:
                    # 프레임 획득
                    depth_image, color_image = node.camera.get_frames()
                    
                    # 이미지 좌우반전
                    if node.flip_horizontal:
                        if color_image is not None:
                            color_image = cv2.flip(color_image, 1)
                        if depth_image is not None:
                            depth_image = cv2.flip(depth_image, 1)
                    
                    # ArUco 마커 자동 감지 (매 프레임마다)
                    if color_image is not None:
                        node.detect_and_update_location()
                    
                    # 버튼 탐지 및 시각화
                    buttons = []
                    if color_image is not None:
                        buttons = node.button_detector.detect_buttons(color_image, depth_image, node.confidence_threshold)
                        
                        display_image = color_image.copy()
                        if buttons:
                            display_image = node._draw_buttons_on_image(display_image, buttons)
                        node._add_info_text(display_image, buttons)
                        
                        cv2.imshow('Roomie VS RGB (YOLO Enhanced)', display_image)
                    
                    if depth_image is not None:
                        depth_normalized = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
                        depth_colored = cv2.applyColorMap(depth_normalized, cv2.COLORMAP_JET)
                        cv2.imshow('Roomie VS Depth', depth_colored)
                    
                    # 키 처리
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:  # ESC
                        node.get_logger().info("ESC 키 눌림 - GUI 종료")
                        break
                    elif key == ord('r') or key == ord('R'):  # R키: 추적 시뮬레이션
                        node.get_logger().info("'R' 키 눌림 - 추적 시뮬레이션 시작")
                        node.simulate_tracking_sequence(robot_id=1, task_id=1)
                    elif key == ord('t') or key == ord('T'):  # T키: 단일 추적 이벤트
                        current_mode = node.mode_names.get(node.current_mode_id, "알 수 없음")
                        node.get_logger().info(f"'T' 키 눌림 - 추적 이벤트 발행 시도 (현재: {current_mode})")
                        import random
                        event_id = random.choice([0, 1, 2, 3])
                        success = node.publish_tracking_event(robot_id=1, tracking_event_id=event_id, task_id=1)
                        if not success:
                            node.get_logger().info("추적 이벤트를 발행하려면 '1t' 명령으로 추적모드로 변경하세요")
                    elif key == ord('g') or key == ord('G'):  # G키: 등록 완료 이벤트
                        current_mode = node.mode_names.get(node.current_mode_id, "알 수 없음")
                        node.get_logger().info(f"'G' 키 눌림 - 등록 완료 이벤트 발행 시도 (현재: {current_mode})")
                        success = node.publish_registered_event(robot_id=1)
                        if not success:
                            node.get_logger().info("등록 완료 이벤트를 발행하려면 '1r' 명령으로 등록모드로 변경하세요")
                    elif key == ord('b') or key == ord('B'):  # B키: 엘리베이터 객체 탐지 결과 출력
                        if buttons:
                            button_objects = [btn for btn in buttons if btn.get('class_name') == 'button']
                            other_objects = [btn for btn in buttons if btn.get('class_name') != 'button']
                            
                            node.get_logger().info(f"'B' 키 눌림 - 엘리베이터 객체 탐지 결과:")
                            node.get_logger().info(f"  전체 객체: {len(buttons)}개")
                            node.get_logger().info(f"  버튼: {len(button_objects)}개")
                            node.get_logger().info(f"  환경객체: {len(other_objects)}개")
                            
                            if button_objects:
                                node.get_logger().info("  탐지된 버튼들:")
                                for i, btn in enumerate(button_objects):
                                    confidence = btn.get('confidence', 1.0)
                                    pressed = "눌림" if btn['is_pressed'] else "안눌림"
                                    node.get_logger().info(f"    {i+1}. button - 신뢰도:{confidence:.2f}, {pressed}, {btn['depth_mm']}mm")
                            
                            if other_objects:
                                node.get_logger().info("  환경 객체들:")
                                for i, btn in enumerate(other_objects):
                                    class_name = btn.get('class_name', 'unknown')
                                    confidence = btn.get('confidence', 1.0)
                                    node.get_logger().info(f"    {i+1}. {class_name} - 신뢰도:{confidence:.2f}, {btn['depth_mm']}mm")
                        else:
                            node.get_logger().info("'B' 키 눌림 - 탐지된 엘리베이터 객체가 없습니다")
                    elif key == ord('f') or key == ord('F'):  # F키: 좌우반전 토글
                        node.flip_horizontal = not node.flip_horizontal
                        status = "켜짐" if node.flip_horizontal else "꺼짐"
                        node.get_logger().info(f"'F' 키 눌림 - 좌우반전: {status}")
                    elif key == ord('c') or key == ord('C'):  # C키: 신뢰도 임계값 조정
                        current_conf = node.confidence_threshold
                        if current_conf == 0.7:
                            node.confidence_threshold = 0.5
                        elif current_conf == 0.5:
                            node.confidence_threshold = 0.9
                        else:
                            node.confidence_threshold = 0.7
                        
                        node.get_logger().info(f"'C' 키 눌림 - 신뢰도 임계값: {current_conf:.2f} → {node.confidence_threshold:.2f}")

                    elif key == ord('m') or key == ord('M'):  # M키: 현재 모드 확인
                        current_mode = node.mode_names.get(node.current_mode_id, "알 수 없음")
                        model_loaded = "✅" if node.button_detector.yolo_model else "❌"
                        aruco_status = "✅" if node.aruco_dict else "❌"
                        
                        node.get_logger().info(f"'M' 키 눌림 - 현재 상태:")
                        node.get_logger().info(f"  VS 모드: {current_mode} (mode_id={node.current_mode_id})")
                        node.get_logger().info(f"  YOLO 모델: {model_loaded}")
                        node.get_logger().info(f"  ArUco 시스템: {aruco_status}")
                        node.get_logger().info(f"  좌우반전: {'ON' if node.flip_horizontal else 'OFF'}")
                        node.get_logger().info(f"  신뢰도 임계값: {node.confidence_threshold}")
                        
                        # 현재 위치 정보
                        location_names = {
                            0: "LOB_WAITING", 1: "LOB_CALL", 2: "RES_PICKUP", 3: "RES_CALL",
                            4: "SUP_PICKUP", 5: "ELE_1", 6: "ELE_2", 101: "ROOM_101",
                            102: "ROOM_102", 201: "ROOM_201", 202: "ROOM_202"
                        }
                        current_location_name = location_names.get(node.last_detected_location_id, f"ID_{node.last_detected_location_id}")
                        node.get_logger().info(f"  현재 위치: {current_location_name}")
                        
                        supported_classes = node.button_detector.class_names
                        node.get_logger().info(f"  감지 가능한 객체: {supported_classes}")
                        node.get_logger().info(f"  버튼 클래스: button")
                        
                        node.get_logger().info("후방 카메라 모드: 0(대기), 1(등록), 2(추적)")
                        node.get_logger().info("전방 카메라 모드: 3(엘리베이터 외부), 4(엘리베이터 내부), 5(일반)")
                        node.get_logger().info("시뮬레이션 모드: 100(배송), 101(호출), 102(길안내), 103(복귀), 104(엘리베이터)")
                        node.get_logger().info("키보드: A(ArUco테스트), F(좌우반전), C(신뢰도조정)")
                    elif key == ord('a') or key == ord('A'):  # A키: ArUco 감지 테스트
                        node.test_aruco_detection()
                    elif key != 255:  # 다른 키가 눌렸을 때
                        if 32 <= key <= 126:
                            node.get_logger().info(f"'{chr(key)}' 키 눌림")
                            node.get_logger().info("사용 가능한 키:")
                            node.get_logger().info("   R(추적시뮬레이션), T(추적이벤트), G(등록완료)")
                            node.get_logger().info("   B(버튼정보), M(상태확인), A(ArUco테스트)")
                            node.get_logger().info("   F(좌우반전), C(신뢰도), ESC(종료)")
                        else:
                            node.get_logger().info(f"키 코드 {key} 눌림")
                        
                except Exception as e:
                    node.get_logger().error(f"프레임 처리 오류: {e}")
                    time.sleep(0.1)
                
                # GUI 처리 완료 후에 ROS2 콜백을 비중단적으로 처리
                try:
                    rclpy.spin_once(node, timeout_sec=0.001)  # 1ms만
                except Exception as ros_error:
                    if frame_count % 1000 == 1:
                        node.get_logger().warning(f"ROS2 콜백 처리 중 에러: {ros_error}")
                    
        except KeyboardInterrupt:
            node.get_logger().info("사용자에 의해 중단되었습니다")
        finally:
            # 정리
            if hasattr(node, 'camera'):
                node.camera.cleanup()
            
            cv2.destroyAllWindows()
            node.destroy_node()
            
    except RuntimeError as e:
        print(f"카메라 초기화 실패: {e}")
        print("해결 방법:")
        print("   1. Astra 카메라가 USB에 제대로 연결되어 있는지 확인")
        print("   2. OpenNI2가 올바르게 설치되어 있는지 확인")
        print("   3. 카메라 드라이버가 설치되어 있는지 확인")
        print("   4. 다른 프로그램에서 카메라를 사용하고 있지 않은지 확인")
    except Exception as e:
        print(f"노드 실행 중 예상치 못한 에러: {e}")
        import traceback
        print(f"스택 트레이스: {traceback.format_exc()}")
    finally:
        try:
            if rclpy.ok():
                rclpy.shutdown()
        except Exception as e:
            pass

if __name__ == '__main__':
    main() 