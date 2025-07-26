#!/usr/bin/env python3

import numpy as np
import cv2
import os
import sys

# OpenNI2 환경변수 설정 (단독 실행용)
def setup_openni2_environment():
    """OpenNI2 실행을 위한 환경변수 설정"""
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
    sys.exit(1)

# 환경설정 후 OpenNI2 import
try:
    from primesense import openni2
    from primesense import _openni2 as c_api
    print("✅ primesense 모듈 import 성공")
except ImportError as e:
    print(f"❌ primesense 모듈 import 실패: {e}")
    print("pip install primesense --break-system-packages 명령으로 설치하세요")
    sys.exit(1)

def test_openni2_streams():
    """OpenNI2를 사용하여 RGB와 Depth 스트림 테스트"""
    try:
        print("🚀 OpenNI2 초기화 시작...")
        
        # OpenNI2 초기화
        openni2.initialize()
        print("✅ OpenNI2 초기화 완료")
        
        # 장치 열기
        print("📱 장치 열기...")
        dev = openni2.Device.open_any()
        print("✅ 장치 열기 완료")
        
        # 스트림 정보 출력
        print("\n📋 장치 정보:")
        print(f"  장치 URI: {dev.get_device_info().uri}")
        print(f"  장치 이름: {dev.get_device_info().name}")
        print(f"  제조사: {dev.get_device_info().vendor}")
        
        # RGB 스트림 생성
        rgb_stream = None
        depth_stream = None
        
        try:
            print("\n🎨 RGB 스트림 생성...")
            rgb_stream = dev.create_color_stream()
            rgb_stream.start()
            print("✅ RGB 스트림 시작 완료")
        except Exception as e:
            print(f"⚠️ RGB 스트림 생성 실패: {e}")
        
        try:
            print("🔍 Depth 스트림 생성...")
            depth_stream = dev.create_depth_stream()
            depth_stream.start()
            print("✅ Depth 스트림 시작 완료")
        except Exception as e:
            print(f"⚠️ Depth 스트림 생성 실패: {e}")
        
        # 스트림 정보 출력
        if rgb_stream:
            video_mode = rgb_stream.get_video_mode()
            print(f"\n📺 RGB 스트림 정보:")
            print(f"  해상도: {video_mode.resolutionX} x {video_mode.resolutionY}")
            print(f"  FPS: {video_mode.fps}")
            print(f"  픽셀 포맷: {video_mode.pixelFormat}")
            
        if depth_stream:
            video_mode = depth_stream.get_video_mode()
            print(f"\n📏 Depth 스트림 정보:")
            print(f"  해상도: {video_mode.resolutionX} x {video_mode.resolutionY}")
            print(f"  FPS: {video_mode.fps}")
            print(f"  픽셀 포맷: {video_mode.pixelFormat}")
        
        # 실시간 스트림 테스트 (ESC로 종료)
        print(f"\n🎬 실시간 스트림 시작... (ESC 키로 종료)")
        
        frame_count = 0
        while True:
            frame_count += 1
            
            # 5프레임마다 한 번씩만 정보 출력 (너무 많은 출력 방지)
            show_info = (frame_count % 5 == 1)
            
            if show_info:
                print(f"\n--- 프레임 {frame_count} ---")
            
            # RGB 프레임
            if rgb_stream:
                try:
                    rgb_frame = rgb_stream.read_frame()
                    rgb_data = rgb_frame.get_buffer_as_uint8()
                    rgb_array = np.frombuffer(rgb_data, dtype=np.uint8)
                    
                    # RGB888 형태로 reshape
                    h = rgb_frame.height
                    w = rgb_frame.width
                    rgb_image = rgb_array.reshape((h, w, 3))
                    
                    if show_info:
                        print(f"  🎨 RGB: {rgb_image.shape}, 타입: {rgb_image.dtype}")
                        
                        # 중앙 픽셀 값
                        center_rgb = rgb_image[h//2, w//2]
                        print(f"    중앙 픽셀 RGB: {center_rgb}")
                    
                    # BGR로 변환하여 표시
                    rgb_bgr = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
                    cv2.imshow('OpenNI2 RGB', rgb_bgr)
                    
                except Exception as e:
                    print(f"  ❌ RGB 프레임 읽기 실패: {e}")
            
            # Depth 프레임
            if depth_stream:
                try:
                    depth_frame = depth_stream.read_frame()
                    depth_data = depth_frame.get_buffer_as_uint16()
                    depth_array = np.frombuffer(depth_data, dtype=np.uint16)
                    
                    # Depth 이미지로 reshape
                    h = depth_frame.height
                    w = depth_frame.width  
                    depth_image = depth_array.reshape((h, w))
                    
                    if show_info:
                        print(f"  🔍 Depth: {depth_image.shape}, 타입: {depth_image.dtype}")
                        
                        # 중앙 픽셀 깊이 값
                        center_depth = depth_image[h//2, w//2]
                        print(f"    중앙 픽셀 Depth: {center_depth}mm")
                    
                    # Depth 시각화
                    depth_normalized = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
                    depth_colored = cv2.applyColorMap(depth_normalized, cv2.COLORMAP_JET)
                    cv2.imshow('OpenNI2 Depth', depth_colored)
                    
                except Exception as e:
                    print(f"  ❌ Depth 프레임 읽기 실패: {e}")
            
            # ESC 키로 종료 (더 빠른 반응성)
            key = cv2.waitKey(30) & 0xFF
            if key == 27:  # ESC
                print("🔴 ESC 키 감지 - 실시간 스트림 종료")
                break
            elif key != 255:  # 다른 키가 눌렸을 때
                print(f"ℹ️ '{chr(key)}' 키 눌림 (ESC로 종료하세요)")
        
        print("\n🎉 OpenNI2 테스트 완료!")
        return True
        
    except Exception as e:
        print(f"❌ OpenNI2 테스트 실패: {e}")
        return False
        
    finally:
        # 정리
        try:
            if rgb_stream:
                rgb_stream.stop()
            if depth_stream:
                depth_stream.stop()
            if 'dev' in locals():
                dev.close()
            openni2.unload()
            cv2.destroyAllWindows()
            print("🧹 리소스 정리 완료")
        except Exception as e:
            print(f"⚠️ 정리 중 에러: {e}")

if __name__ == "__main__":
    test_openni2_streams() 