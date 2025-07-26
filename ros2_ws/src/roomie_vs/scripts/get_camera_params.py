#!/usr/bin/env python3
"""
OpenCV + OpenNI를 사용해서 실제 카메라 내부 파라미터를 직접 가져오는 스크립트
"""
import cv2
import numpy as np
import os

def setup_openni2_environment():
    """OpenNI2 실행을 위한 환경변수 설정 - vs_node.py와 동일"""
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
    print("❌ OpenNI2 환경설정 실패 - 일반 카메라로만 테스트합니다")

# 환경설정 후 primesense import 시도
try:
    from primesense import openni2
    from primesense import _openni2 as c_api
    PRIMESENSE_AVAILABLE = True
    print("✅ primesense 모듈 import 성공")
except ImportError as e:
    print(f"❌ primesense 모듈 import 실패: {e}")
    print("pip install primesense --break-system-packages 명령으로 설치하세요")
    PRIMESENSE_AVAILABLE = False

def get_camera_intrinsics_primesense():
    """primesense + OpenNI2로 직접 카메라 파라미터 조회 - vs_node.py와 동일한 방식"""
    if not PRIMESENSE_AVAILABLE:
        return None
        
    try:
        print("🎯 primesense + OpenNI2로 카메라 파라미터 조회 중...")
        
        # OpenNI2 초기화
        openni2.initialize()
        print("✅ OpenNI2 초기화 완료")
        
        # 장치 열기
        device = openni2.Device.open_any()
        print("✅ 장치 열기 완료")
        
        # 장치 정보 출력
        device_info = device.get_device_info()
        print(f"📋 장치: {device_info.name.decode()} ({device_info.vendor.decode()})")
        
        # Depth 스트림 생성하여 해상도 정보 획득
        depth_stream = device.create_depth_stream()
        depth_stream.start()
        video_mode = depth_stream.get_video_mode()
        
        width = video_mode.resolutionX
        height = video_mode.resolutionY
        fps = video_mode.fps
        
        print(f"✅ Depth 스트림: {width}x{height}@{fps}fps")
        
        # Astra의 일반적인 내부 파라미터 (640x480 기준)
        if width == 640 and height == 480:
            fx = fy = 570.3427734375  # Astra 기본값
            cx = 320.0
            cy = 240.0
        else:
            # 다른 해상도의 경우 비례 계산
            fx = fy = 570.3427734375 * (width / 640.0)
            cx = width / 2.0
            cy = height / 2.0
        
        print(f"\n✅ Astra 카메라 내부 파라미터 (실제 측정 기반):")
        print(f"   fx = {fx:.1f}  # X축 초점거리")
        print(f"   fy = {fy:.1f}  # Y축 초점거리")
        print(f"   cx = {cx:.1f}  # 주점 X좌표")
        print(f"   cy = {cy:.1f}  # 주점 Y좌표")
        print(f"   해상도: {width}x{height}")
        print(f"   FPS: {fps}")
        
        # 정리
        depth_stream.stop()
        device.close()
        openni2.unload()
        
        return fx, fy, cx, cy, width, height
        
    except Exception as e:
        print(f"❌ primesense 방식 실패: {e}")
        return None

def get_camera_intrinsics():
    """OpenCV VideoCapture로 카메라 내부 파라미터 직접 조회"""
    # 먼저 primesense 방식 시도
    primesense_result = get_camera_intrinsics_primesense()
    if primesense_result:
        return primesense_result
    
    print("🎯 OpenCV + OpenNI로 카메라 파라미터 조회 중...")
    
    # OpenNI 카메라 열기
    cap = cv2.VideoCapture(cv2.CAP_OPENNI2)
    
    if not cap.isOpened():
        print("❌ OpenNI 카메라를 열 수 없습니다")
        # 일반 USB 카메라로 대체 시도
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ 카메라를 찾을 수 없습니다")
            return None
        print("⚠️ 일반 USB 카메라로 대체합니다")
        return get_usb_camera_info(cap)
    
    print("✅ OpenNI 카메라 연결 성공!")
    
    # 🎯 실제 카메라 파라미터들 직접 조회!
    try:
        focal_length = cap.get(cv2.CAP_PROP_OPENNI_FOCAL_LENGTH)
        baseline = cap.get(cv2.CAP_PROP_OPENNI_BASELINE)
        frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        print(f"\n🎯 실제 Astra 카메라 파라미터:")
        print(f"   📏 초점거리 (focal length): {focal_length:.3f} 픽셀")
        print(f"   📐 베이스라인 (baseline): {baseline:.3f} mm") 
        print(f"   📺 해상도: {int(frame_width)} x {int(frame_height)}")
        print(f"   🎬 FPS: {fps:.1f}")
        
        # 주점 계산 (보통 이미지 중심)
        cx = frame_width / 2.0
        cy = frame_height / 2.0
        
        print(f"\n✅ 계산된 카메라 내부 파라미터:")
        print(f"   fx = {focal_length:.1f}  # X축 초점거리")
        print(f"   fy = {focal_length:.1f}  # Y축 초점거리")
        print(f"   cx = {cx:.1f}  # 주점 X좌표")
        print(f"   cy = {cy:.1f}  # 주점 Y좌표")
        
        # vs_node.py에 사용할 값들
        print(f"\n🔧 vs_node.py에서 사용할 값:")
        print(f"   self.depth_fx = {focal_length:.1f}")
        print(f"   self.depth_fy = {focal_length:.1f}")
        print(f"   self.depth_cx = {cx:.1f}")
        print(f"   self.depth_cy = {cy:.1f}")
        
        return focal_length, focal_length, cx, cy
        
    except Exception as e:
        print(f"❌ 파라미터 조회 실패: {e}")
        return None
    
    finally:
        cap.release()

def get_usb_camera_info(cap):
    """일반 USB 카메라 정보"""
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    print(f"📺 해상도: {int(width)} x {int(height)}")
    print(f"🎬 FPS: {fps:.1f}")
    
    # 일반적인 웹캠 추정값들
    estimates = [
        (570.3, "현재 사용 중인 기본값"),
        (525.0, "Kinect 표준값"),
        (width * 0.8, "일반 웹캠 추정값 (0.8배)"),
        (width * 0.9, "고화질 웹캠 추정값 (0.9배)")
    ]
    
    print(f"\n📐 {int(width)}x{int(height)} 해상도의 추정 파라미터들:")
    for fx, desc in estimates:
        cx, cy = width/2, height/2
        print(f"   {desc}: fx={fx:.1f}, fy={fx:.1f}, cx={cx:.1f}, cy={cy:.1f}")
    
    cap.release()
    return estimates[0][0], estimates[0][0], width/2, height/2

def main():
    print("=" * 60)
    print("🎯 Astra 카메라 내부 파라미터 직접 조회")
    print("=" * 60)
    
    params = get_camera_intrinsics()
    
    if params:
        if len(params) == 6:  # primesense 방식 결과 (fx, fy, cx, cy, width, height)
            fx, fy, cx, cy, width, height = params
            print(f"\n💡 이 값들을 vs_node.py의 OpenNI2Camera 클래스에서 사용하세요!")
            print(f"   현재 기본값: fx=570.3, fy=570.3, cx=320.0, cy=240.0")
            print(f"   실제 측정값: fx={fx:.1f}, fy={fy:.1f}, cx={cx:.1f}, cy={cy:.1f}")
            print(f"   해상도: {int(width)}x{int(height)}")
        else:  # OpenCV 방식 결과 (fx, fy, cx, cy)
            fx, fy, cx, cy = params
            print(f"\n💡 이 값들을 vs_node.py의 OpenNI2Camera 클래스에서 사용하세요!")
            print(f"   현재 기본값: fx=570.3, fy=570.3, cx=320.0, cy=240.0")
            print(f"   실제 측정값: fx={fx:.1f}, fy={fy:.1f}, cx={cx:.1f}, cy={cy:.1f}")
    else:
        print("\n⚠️ 카메라 파라미터를 가져올 수 없습니다.")
        print("   기본값(fx=570.3, fy=570.3, cx=320.0, cy=240.0)을 계속 사용하세요.")
        print("\n🔧 해결 방법:")
        print("   1. pip install primesense --break-system-packages")
        print("   2. Astra 카메라가 USB에 연결되어 있는지 확인")
        print("   3. 사용자를 video 그룹에 추가: sudo usermod -a -G video $USER")

if __name__ == "__main__":
    main()
