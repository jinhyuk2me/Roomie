# RMS 서버 설정
RMS_HOST = "localhost"
RMS_PORT = 8000
RMS_WS_URL = f"ws://{RMS_HOST}:{RMS_PORT}/ws"
RMS_HTTP_URL = f"http://{RMS_HOST}:{RMS_PORT}"

# 음식 타입 매핑
FOOD_TYPES = {
    0: "스파게티",
    1: "피자", 
    2: "스테이크",
    3: "버거"
} 