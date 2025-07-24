#!/usr/bin/env python3

import cv2
import numpy as np

def test_rgb_camera():
    """간단한 RGB 카메라 테스트"""
    print("🎥 RGB 카메라 테스트 시작...")
    
    # 카메라 장치 탐지 (0부터 시작해서 여러 장치 확인)
    for cam_id in range(5):
        print(f"📹 카메라 {cam_id} 테스트 중...")
        cap = cv2.VideoCapture(cam_id)
        
        if cap.isOpened():
            # 프레임 크기 설정
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            cap.set(cv2.CAP_PROP_FPS, 30)
            
            print(f"✅ 카메라 {cam_id} 연결 성공!")
            print(f"   해상도: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
            print(f"   FPS: {cap.get(cv2.CAP_PROP_FPS)}")
            
            # 몇 프레임 테스트
            for i in range(10):
                ret, frame = cap.read()
                if ret:
                    print(f"🎬 프레임 {i+1}: {frame.shape}, 타입: {frame.dtype}")
                    
                    # 중앙 픽셀 RGB 값 출력
                    h, w = frame.shape[:2]
                    center_pixel = frame[h//2, w//2]
                    print(f"   중앙 픽셀 BGR: {center_pixel}")
                    
                    # 실시간 영상 표시
                    cv2.imshow('RGB Camera Test', frame)
                    
                    # ESC 키로 종료
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:  # ESC
                        break
                else:
                    print(f"❌ 프레임 {i+1} 읽기 실패")
                    break
            
            cap.release()
            cv2.destroyAllWindows()
            return True
        else:
            print(f"❌ 카메라 {cam_id} 연결 실패")
            cap.release()
    
    print("❌ 사용 가능한 RGB 카메라를 찾을 수 없습니다.")
    return False

if __name__ == "__main__":
    test_rgb_camera() 