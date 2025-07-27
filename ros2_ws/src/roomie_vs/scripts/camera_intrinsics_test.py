#!/usr/bin/env python3
"""
카메라 내부 파라미터(Camera Intrinsics) 측정 및 검증 스크립트
Astra 카메라의 정확한 fx, fy, cx, cy 값을 찾기 위한 도구
"""

import os
import sys
import numpy as np

# OpenNI2 환경 설정
def setup_openni2_environment():
    """OpenNI2 환경 변수 설정"""
    try:
        # 현재 패키지 경로 설정
        current_dir = os.path.dirname(os.path.abspath(__file__))
        package_dir = os.path.dirname(current_dir)
        
        # OpenNI2 관련 환경 변수 설정
        openni2_paths = [
            "/usr/lib/OpenNI2-FreenectDriver",
            "/usr/lib/ni", 
            "/usr/local/lib/OpenNI2-FreenectDriver",
            "/opt/ros/humble/lib",
            f"{package_dir}/lib"
        ]
        
        for path in openni2_paths:
            if os.path.exists(path):
                os.environ["OPENNI2_REDIST"] = path
                print(f"✅ OPENNI2_REDIST 설정: {path}")
                break
        else:
            print("⚠️ OpenNI2 경로를 찾을 수 없지만 계속 진행합니다")
        
        # LD_LIBRARY_PATH 업데이트
        ld_library_path = os.environ.get("LD_LIBRARY_PATH", "")
        for path in openni2_paths:
            if os.path.exists(path) and path not in ld_library_path:
                ld_library_path = f"{path}:{ld_library_path}"
        
        os.environ["LD_LIBRARY_PATH"] = ld_library_path
        return True
        
    except Exception as e:
        print(f"❌ OpenNI2 환경 설정 실패: {e}")
        return False

# 환경설정 먼저 실행
if not setup_openni2_environment():
    print("OpenNI2 환경 설정에 실패했지만 계속 진행합니다.")

# OpenNI2 import
try:
    from primesense import openni2
    from primesense import _openni2 as c_api
    print("✅ primesense 모듈 import 성공")
except ImportError as e:
    print(f"❌ primesense 모듈 import 실패: {e}")
    print("pip install primesense --break-system-packages 명령으로 설치하세요")
    sys.exit(1)

import cv2

def get_camera_intrinsics_from_openni2():
    """OpenNI2에서 카메라 내부 파라미터 직접 조회"""
    print("🔍 OpenNI2에서 카메라 파라미터 조회 중...")
    
    try:
        # OpenNI2 초기화
        openni2.initialize()
        
        # 장치 열기
        device = openni2.Device.open_any()
        device_info = device.get_device_info()
        print(f"📋 장치: {device_info.name.decode()} ({device_info.vendor.decode()})")
        
        # RGB 스트림 정보
        if device.has_sensor(openni2.SENSOR_COLOR):
            rgb_stream = device.create_color_stream()
            video_mode = rgb_stream.get_video_mode()
            print(f"📹 RGB 해상도: {video_mode.resolutionX}x{video_mode.resolutionY}")
            print(f"📹 RGB FPS: {video_mode.fps}")
            rgb_stream.close()
        
        # Depth 스트림 정보
        if device.has_sensor(openni2.SENSOR_DEPTH):
            depth_stream = device.create_depth_stream()
            video_mode = depth_stream.get_video_mode()
            print(f"📏 Depth 해상도: {video_mode.resolutionX}x{video_mode.resolutionY}")
            print(f"📏 Depth FPS: {video_mode.fps}")
            
            # 🎯 FOV (Field of View) 정보 시도
            try:
                # OpenNI2 Camera info 조회 시도
                fov_h = depth_stream.get_horizontal_fov()
                fov_v = depth_stream.get_vertical_fov()
                print(f"🔍 Horizontal FOV: {fov_h:.4f} rad ({np.degrees(fov_h):.2f}°)")
                print(f"🔍 Vertical FOV: {fov_v:.4f} rad ({np.degrees(fov_v):.2f}°)")
                
                # FOV에서 초점거리 계산
                width = video_mode.resolutionX
                height = video_mode.resolutionY
                fx = width / (2 * np.tan(fov_h / 2))
                fy = height / (2 * np.tan(fov_v / 2))
                cx = width / 2.0
                cy = height / 2.0
                
                print("\n🎯 계산된 카메라 내부 파라미터:")
                print(f"   fx (초점거리 X): {fx:.3f}")
                print(f"   fy (초점거리 Y): {fy:.3f}")
                print(f"   cx (주점 X): {cx:.1f}")
                print(f"   cy (주점 Y): {cy:.1f}")
                
                return fx, fy, cx, cy
                
            except Exception as e:
                print(f"⚠️ FOV 정보 조회 실패: {e}")
            
            depth_stream.close()
        
        device.close()
        openni2.unload()
        
    except Exception as e:
        print(f"❌ OpenNI2 조회 실패: {e}")
    
    return None

def estimate_intrinsics_from_resolution():
    """해상도 기반 추정값 계산"""
    print("\n📐 해상도 기반 추정값 계산...")
    
    # 일반적인 추정값들
    estimates = [
        # (해상도, fx, fy, 설명)
        (640, 480, 570.3, 570.3, "현재 사용 중인 기본값"),
        (640, 480, 525.0, 525.0, "일반적인 웹캠 추정값"),
        (640, 480, 615.0, 615.0, "높은 화각 카메라"),
        (640, 480, 480.0, 480.0, "넓은 화각 카메라"),
    ]
    
    print("🎯 다양한 추정값들:")
    for w, h, fx, fy, desc in estimates:
        cx, cy = w/2, h/2
        fov_h = 2 * np.arctan(w / (2 * fx))
        fov_v = 2 * np.arctan(h / (2 * fy))
        print(f"   {desc}:")
        print(f"     fx={fx:.1f}, fy={fy:.1f}, cx={cx:.1f}, cy={cy:.1f}")
        print(f"     FOV: {np.degrees(fov_h):.1f}° x {np.degrees(fov_v):.1f}°")
        print()

def test_depth_accuracy(fx=570.3, fy=570.3, cx=320.0, cy=240.0):
    """실제 카메라로 깊이 정확도 테스트"""
    print(f"\n🧪 깊이 정확도 테스트 (fx={fx:.1f}, fy={fy:.1f}, cx={cx:.1f}, cy={cy:.1f})")
    
    try:
        # OpenNI2 초기화
        openni2.initialize()
        device = openni2.Device.open_any()
        
        # RGB와 Depth 스트림 생성
        rgb_stream = device.create_color_stream()
        depth_stream = device.create_depth_stream()
        
        rgb_stream.start()
        depth_stream.start()
        
        print("📸 실시간 테스트 시작 (ESC로 종료)")
        print("💡 마우스로 클릭하면 해당 지점의 3D 좌표를 표시합니다")
        
        def mouse_callback(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                depth_frame = param.get('depth_frame')
                if depth_frame is not None:
                    depth_mm = depth_frame[y, x]
                    if depth_mm > 0:
                        # 3D 좌표 계산
                        z = depth_mm / 1000.0  # mm to meters
                        x_3d = (x - cx) * z / fx
                        y_3d = (y - cy) * z / fy
                        
                        print(f"🎯 클릭 지점 ({x}, {y}): 깊이={depth_mm}mm")
                        print(f"   3D 좌표: X={x_3d:.3f}m, Y={y_3d:.3f}m, Z={z:.3f}m")
                    else:
                        print(f"❌ 클릭 지점 ({x}, {y}): 깊이 정보 없음")
        
        # 마우스 콜백 데이터
        callback_data = {'depth_frame': None}
        cv2.namedWindow('Intrinsics Test')
        cv2.setMouseCallback('Intrinsics Test', mouse_callback, callback_data)
        
        for i in range(300):  # 10초간 테스트
            # RGB 프레임
            rgb_frame = rgb_stream.read_frame()
            rgb_data = rgb_frame.get_buffer_as_uint8()
            rgb_array = np.frombuffer(rgb_data, dtype=np.uint8)
            rgb_image = rgb_array.reshape((rgb_frame.height, rgb_frame.width, 3))
            rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
            
            # Depth 프레임
            depth_frame = depth_stream.read_frame()
            depth_data = depth_frame.get_buffer_as_uint16()
            depth_array = np.frombuffer(depth_data, dtype=np.uint16)
            depth_image = depth_array.reshape((depth_frame.height, depth_frame.width))
            
            # 콜백 데이터 업데이트
            callback_data['depth_frame'] = depth_image
            
            # 정보 오버레이
            cv2.putText(rgb_image, f"Camera Intrinsics Test", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
            cv2.putText(rgb_image, f"fx={fx:.1f}, fy={fy:.1f}", (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(rgb_image, f"cx={cx:.1f}, cy={cy:.1f}", (10, 90), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(rgb_image, "Click anywhere to get 3D coordinates", (10, rgb_image.shape[0]-20), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            cv2.imshow('Intrinsics Test', rgb_image)
            
            key = cv2.waitKey(30) & 0xFF
            if key == 27:  # ESC
                break
        
        rgb_stream.stop()
        depth_stream.stop()
        device.close()
        cv2.destroyAllWindows()
        
    except Exception as e:
        print(f"❌ 깊이 테스트 실패: {e}")
    
    finally:
        openni2.unload()

def main():
    """메인 함수"""
    print("=" * 70)
    print("🎯 카메라 내부 파라미터(Camera Intrinsics) 측정 도구")
    print("=" * 70)
    
    print("\n📋 필요한 파라미터들:")
    print("   • fx: X축 초점거리 (픽셀)")
    print("   • fy: Y축 초점거리 (픽셀)")  
    print("   • cx: 주점 X좌표 (보통 width/2)")
    print("   • cy: 주점 Y좌표 (보통 height/2)")
    
    # 1. OpenNI2에서 직접 조회
    intrinsics = get_camera_intrinsics_from_openni2()
    
    # 2. 해상도 기반 추정값들
    estimate_intrinsics_from_resolution()
    
    # 3. 실제 테스트
    if intrinsics:
        fx, fy, cx, cy = intrinsics
        print(f"\n✅ OpenNI2에서 측정된 값으로 테스트합니다")
        test_depth_accuracy(fx, fy, cx, cy)
    else:
        print(f"\n⚠️ 기본값으로 테스트합니다")
        test_depth_accuracy()
    
    print("\n💡 다음 방법들로 더 정확한 값을 얻을 수 있습니다:")
    print("   1. ROS2 camera_calibration 패키지 사용")
    print("   2. OpenCV 체스보드 캘리브레이션")
    print("   3. 알려진 크기의 물체로 수동 측정")
    print("   4. 제조사 스펙 시트 확인")

if __name__ == "__main__":
    main() 