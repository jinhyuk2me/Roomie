#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
import threading
import time
import numpy as np
import cv2
from typing import Optional, Tuple, List

# ROS2 메시지 타입들
from geometry_msgs.msg import Point

# 커스텀 서비스
from roomie_msgs.srv import ButtonStatus, SetVSMode

# OpenNI2 환경변수 설정 (import 전에 실행)
import os

def setup_openni2_environment():
    """OpenNI2 실행을 위한 환경변수 설정 - openni2_test.py와 동일"""
    openni_path = os.path.expanduser("~/Downloads/OpenNI_SDK_ROS2_v1.0.2_20220809_b32e47_linux/ros2_astra_camera/astra_camera/openni2_redist/x64")
    
    # 경로가 존재하는지 확인
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
        self.depth_fx = 570.3  # focal length x
        self.depth_fy = 570.3  # focal length y
        self.depth_cx = 320.0  # principal point x  
        self.depth_cy = 240.0  # principal point y
        
        # 현재 프레임들
        self.current_depth = None
        self.current_color = None
        self.frame_lock = threading.Lock()
        
    def initialize(self) -> bool:
        """OpenNI2 카메라 초기화"""
        try:
            self.logger.info("🚀 OpenNI2 카메라 초기화 시작...")
            
            # OpenNI2 초기화
            openni2.initialize()
            self.logger.info("✅ OpenNI2 초기화 완료")
            
            # 장치 열기
            self.device = openni2.Device.open_any()
            self.logger.info("✅ 장치 열기 완료")
            
            # 장치 정보 출력
            device_info = self.device.get_device_info()
            self.logger.info(f"📋 장치: {device_info.name.decode()} ({device_info.vendor.decode()})")
            
            # RGB 스트림 생성
            try:
                self.rgb_stream = self.device.create_color_stream()
                self.rgb_stream.start()
                video_mode = self.rgb_stream.get_video_mode()
                self.logger.info(f"✅ RGB 스트림: {video_mode.resolutionX}x{video_mode.resolutionY}@{video_mode.fps}fps")
            except Exception as e:
                self.logger.warning(f"⚠️ RGB 스트림 생성 실패: {e}")
                self.rgb_stream = None
            
            # Depth 스트림 생성
            try:
                self.depth_stream = self.device.create_depth_stream()
                self.depth_stream.start()
                video_mode = self.depth_stream.get_video_mode()
                self.logger.info(f"✅ Depth 스트림: {video_mode.resolutionX}x{video_mode.resolutionY}@{video_mode.fps}fps")
            except Exception as e:
                self.logger.warning(f"⚠️ Depth 스트림 생성 실패: {e}")
                self.depth_stream = None
            
            if not self.rgb_stream and not self.depth_stream:
                self.logger.error("❌ RGB와 Depth 스트림 모두 생성 실패")
                return False
            
            self.is_running = True
            self.logger.info("🎉 OpenNI2 카메라 초기화 완료!")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ OpenNI2 카메라 초기화 실패: {e}")
            return False
    
    def get_frames(self) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
        """OpenNI2에서 RGB와 Depth 프레임 획득 - openni2_test.py와 동일한 방식"""
        if not self.is_running:
            raise RuntimeError("카메라가 초기화되지 않았습니다")
        
        try:
            depth_image = None
            color_image = None
            
            # 🔧 RGB 프레임 획득 - openni2_test.py와 정확히 동일한 방식
            if self.rgb_stream:
                try:
                    rgb_frame = self.rgb_stream.read_frame()
                    rgb_data = rgb_frame.get_buffer_as_uint8()
                    rgb_array = np.frombuffer(rgb_data, dtype=np.uint8)
                    
                    # openni2_test.py와 동일: RGB888 형태로 reshape
                    h = rgb_frame.height
                    w = rgb_frame.width
                    rgb_image = rgb_array.reshape((h, w, 3))
                    
                    # openni2_test.py와 동일: BGR로 변환하여 저장
                    color_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
                    
                except Exception as e:
                    self.logger.warning(f"RGB 프레임 읽기 실패: {e}")
            
            # 🔧 Depth 프레임 획득 - openni2_test.py와 정확히 동일한 방식  
            if self.depth_stream:
                try:
                    depth_frame = self.depth_stream.read_frame()
                    depth_data = depth_frame.get_buffer_as_uint16()
                    depth_array = np.frombuffer(depth_data, dtype=np.uint16)
                    
                    # openni2_test.py와 동일: Depth 이미지로 reshape
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
            self.logger.info("🧹 OpenNI2 카메라 정리 완료")
            
        except Exception as e:
            self.logger.warning(f"카메라 정리 중 에러: {e}")

class ButtonDetector:
    """OpenCV 기반 버튼 탐지 클래스"""
    
    def __init__(self, logger):
        self.logger = logger
        
    def detect_buttons(self, color_image: np.ndarray, depth_image: np.ndarray) -> List[dict]:
        """이미지에서 버튼들을 탐지하고 정보 반환"""
        if color_image is None:
            return []
            
        try:
            # HoughCircles로 원형 버튼 탐지
            gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
            circles = cv2.HoughCircles(
                gray,
                cv2.HOUGH_GRADIENT,
                dp=1,
                minDist=60,
                param1=50,
                param2=30,
                minRadius=20,
                maxRadius=60
            )
            
            buttons = []
            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for (x, y, r) in circles[:5]:  # 최대 5개
                    # Depth 정보
                    depth_value = depth_image[y, x] if depth_image is not None else 1000
                    
                    # 버튼 눌림 상태 추정
                    is_pressed = self._check_button_pressed(depth_image, x, y, r) if depth_image is not None else False
                    
                    buttons.append({
                        'center': (x, y),
                        'radius': r,
                        'depth_mm': int(depth_value),
                        'is_pressed': is_pressed
                    })
            
            return buttons
            
        except Exception as e:
            self.logger.error(f"버튼 탐지 에러: {e}")
            return []
    
    def _check_button_pressed(self, depth_image: np.ndarray, cx: int, cy: int, radius: int) -> bool:
        """버튼 눌림 상태 확인 (주변 깊이와 비교)"""
        try:
            # 버튼 중심의 깊이값
            center_depth = depth_image[cy, cx]
            if center_depth <= 0:
                return False
            
            # 버튼 주변 영역의 평균 깊이값 
            y1, y2 = max(0, cy-radius), min(depth_image.shape[0], cy+radius)
            x1, x2 = max(0, cx-radius), min(depth_image.shape[1], cx+radius)
            
            surrounding_region = depth_image[y1:y2, x1:x2]
            valid_depths = surrounding_region[surrounding_region > 0]
            
            # 유효한 깊이 값이 충분하지 않으면 판단 불가
            if valid_depths.size < 5:
                return False
                
            surrounding_depth = np.mean(valid_depths)
            
            # 중심이 주변보다 깊으면 눌린 것으로 판단
            return center_depth > surrounding_depth + 10  # 10mm 차이
            
        except Exception:
            return False

class VSNodeV2(Node):
    """OpenNI2 기반 Vision Service ROS2 노드"""
    
    def __init__(self):
        super().__init__('vs_node_v2')
        
        # 카메라와 버튼 탐지기 초기화
        self.camera = OpenNI2Camera(self.get_logger())
        self.button_detector = ButtonDetector(self.get_logger())
        
        # 카메라 초기화 시도
        self.camera_initialized = False
        if self.camera.initialize():
            self.camera_initialized = True
            self.get_logger().info("✅ OpenNI2 Astra 카메라 초기화 성공")
        else:
            self.get_logger().error("❌ OpenNI2 Astra 카메라 초기화 실패")
            raise RuntimeError("실제 카메라 초기화 실패. 카메라 연결을 확인하고 다시 시도하세요.")
        
        # ROS2 서비스들
        self.button_status_service = self.create_service(
            ButtonStatus, 
            'vs/button_status', 
            self.button_status_callback
        )
        
        self.set_mode_service = self.create_service(
            SetVSMode,
            'vs/set_mode',
            self.set_vs_mode_callback
        )
        
        self.get_logger().info("🚀 OpenNI2 기반 VS Node 초기화 완료! (GUI는 메인쓰레드에서 실행)")
    
    def button_status_callback(self, request, response):
        """버튼 상태 요청 처리"""
        try:
            self.get_logger().info(f"버튼 상태 요청: robot_id={request.robot_id}, button_ids={request.button_ids}")
            
            # Response 초기화
            response.robot_id = request.robot_id
            n_buttons = len(request.button_ids)
            
            if n_buttons == 0:
                response.xs = []
                response.ys = []
                response.depths = []
                response.is_pressed = []
                response.timestamp = []
                return response
            
            # 카메라에서 프레임 가져오기
            depth_image, color_image = self.camera.get_frames()
            
            # 버튼 탐지
            detected_buttons = self.button_detector.detect_buttons(color_image, depth_image)
            
            # 실제 탐지된 버튼 수만큼만 처리
            actual_button_count = min(len(detected_buttons), n_buttons)
            
            xs, ys, depths, is_pressed, timestamps = [], [], [], [], []
            
            for i in range(actual_button_count):
                # 실제 탐지된 버튼 사용
                button = detected_buttons[i]
                x, y = button['center']
                depth_mm = button['depth_mm']
                
                # 3D 좌표 변환
                world_x, world_y, world_z = self.camera.pixel_to_3d(x, y, depth_mm)
                
                xs.append(float(world_x))
                ys.append(float(world_y))
                depths.append(float(world_z))
                is_pressed.append(button['is_pressed'])
                timestamps.append(self.get_clock().now().to_msg())
            
            # 요청한 버튼 수보다 실제 탐지된 버튼이 적으면 경고
            if actual_button_count < n_buttons:
                self.get_logger().warning(f"요청된 버튼 수({n_buttons})보다 탐지된 버튼 수({actual_button_count})가 적습니다.")
            
            response.xs = xs
            response.ys = ys
            response.depths = depths
            response.is_pressed = is_pressed
            response.timestamp = timestamps
            
            self.get_logger().info(f"실제 카메라에서 버튼 탐지 완료: {len(detected_buttons)}개 탐지됨")
                
        except Exception as e:
            self.get_logger().error(f"버튼 상태 서비스 에러: {e}")
            # 에러 시 빈 배열 반환
            response.robot_id = request.robot_id
            response.xs = []
            response.ys = []
            response.depths = []
            response.is_pressed = []
            response.timestamp = []
        
        return response
    
    def set_vs_mode_callback(self, request, response):
        """VS 모드 설정 처리"""
        try:
            self.get_logger().info(f"VS 모드 설정: {request.mode}")
            
            # 간단한 모드 처리
            if request.mode.lower() in ['active', 'standby', 'debug']:
                response.success = True
                response.message = f"OrbbecSDK v2 모드가 '{request.mode}'로 설정되었습니다"
            else:
                response.success = False
                response.message = f"알 수 없는 모드: {request.mode}"
                
        except Exception as e:
            self.get_logger().error(f"모드 설정 에러: {e}")
            response.success = False
            response.message = f"에러 발생: {str(e)}"
        
        return response
    
    # 🗑️ GUI 쓰레드 메소드들 제거됨 - 메인 쓰레드에서 GUI 처리

    def _draw_buttons_on_image(self, image: np.ndarray, buttons: List[dict]) -> np.ndarray:
        """이미지에 탐지된 버튼들을 그립니다"""
        import cv2
        
        for i, button in enumerate(buttons):
            center = button['center']
            radius = button['radius']
            is_pressed = button['is_pressed']
            depth_mm = button['depth_mm']
            
            # 버튼 원 그리기
            color = (0, 255, 0) if not is_pressed else (255, 0, 0)  # 초록색/빨간색
            cv2.circle(image, center, radius, color, 3)
            
            # 버튼 번호 표시
            cv2.putText(image, str(i+1), (center[0]-10, center[1]+5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            
            # 거리 정보 표시
            distance_text = f"{depth_mm}mm"
            cv2.putText(image, distance_text, (center[0]-20, center[1]+25), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
        
        return image

    def _add_info_text(self, image: np.ndarray, buttons: List[dict]):
        """영상에 정보 텍스트 추가"""
        import cv2
        
        # 상단에 제목
        cv2.putText(image, "Roomie Vision System v2", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
        
        # 실제 카메라 상태만 표시
        cv2.putText(image, "Status: Real Camera Active", (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # 탐지된 버튼 수
        cv2.putText(image, f"Buttons Detected: {len(buttons)}", (10, 85), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        
        # 눌린 버튼 표시
        pressed_buttons = [i+1 for i, btn in enumerate(buttons) if btn['is_pressed']]
        if pressed_buttons:
            cv2.putText(image, f"Pressed: {pressed_buttons}", (10, 110), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        
        # 종료 안내
        cv2.putText(image, "Press ESC to exit", (10, image.shape[0]-20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    def __del__(self):
        """소멸자 - 카메라 정리"""
        if hasattr(self, 'camera'):
            self.camera.cleanup()

def main(args=None):
    rclpy.init(args=args)
    
    try:
        node = VSNodeV2()
        
        # 🚀 메인 쓰레드에서 GUI와 ROS2를 함께 처리 (openni2_test.py와 동일한 방식)
        node.get_logger().info("🎬 메인 쓰레드에서 GUI 시작!")
        
        import cv2
        frame_count = 0
        
        try:
            while rclpy.ok():
                frame_count += 1
                
                # 🎯 GUI 처리를 우선순위로! (openni2_test.py와 동일한 순서)
                try:
                    # 프레임 획득 (openni2_test.py와 동일한 방식)
                    depth_image, color_image = node.camera.get_frames()
                    
                    # 🎯 GUI 표시 (openni2_test.py와 완전히 동일한 방식!)
                    if color_image is not None:
                        cv2.imshow('Roomie VS RGB', color_image)
                    
                    if depth_image is not None:
                        # 🎬 openni2_test.py와 완전히 동일한 Depth 시각화!
                        depth_normalized = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
                        depth_colored = cv2.applyColorMap(depth_normalized, cv2.COLORMAP_JET)
                        cv2.imshow('Roomie VS Depth', depth_colored)
                    
                    # 🎯 openni2_test.py와 완전히 동일한 키 처리! (GUI 우선!)
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:  # ESC
                        node.get_logger().info("ESC 키 눌림 - GUI 종료")
                        break
                    elif key != 255:  # 다른 키가 눌렸을 때
                        node.get_logger().info(f"'{chr(key)}' 키 눌림 (ESC로 종료하세요)")
                        
                except Exception as e:
                    node.get_logger().error(f"프레임 처리 오류: {e}")
                    time.sleep(0.1)
                
                # 🔧 GUI 처리 완료 후에 ROS2 콜백을 비중단적으로 처리
                try:
                    # 매우 짧은 시간만 ROS2 처리 (GUI를 방해하지 않도록)
                    rclpy.spin_once(node, timeout_sec=0.001)  # 1ms만
                except Exception as ros_error:
                    if frame_count % 1000 == 1:  # 가끔만 로그
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
        print(f"❌ 카메라 초기화 실패: {e}")
        print("🔧 해결 방법:")
        print("   1. Astra 카메라가 USB에 제대로 연결되어 있는지 확인")
        print("   2. OpenNI2가 올바르게 설치되어 있는지 확인")
        print("   3. 카메라 드라이버가 설치되어 있는지 확인")
        print("   4. 다른 프로그램에서 카메라를 사용하고 있지 않은지 확인")
    except Exception as e:
        print(f"❌ 노드 실행 중 예상치 못한 에러: {e}")
        import traceback
        print(f"스택 트레이스: {traceback.format_exc()}")
    finally:
        # rclpy가 이미 shutdown되었는지 확인
        try:
            if rclpy.ok():
                rclpy.shutdown()
        except Exception as e:
            pass  # 이미 shutdown된 경우 무시

if __name__ == '__main__':
    main() 