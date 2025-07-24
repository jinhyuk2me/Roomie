from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import gui_router
from typing import Optional

# ROS2 노드 인스턴스를 저장하기 위한 임시 타입 정의
# 실제 RmsNode 클래스를 직접 임포트하면 순환 참조 문제가 발생할 수 있으므로,
# 여기서는 Any 또는 Optional을 사용합니다.
from typing import Any

app = FastAPI(title="Roomie Main Server")

# 앱의 state에 rms_node를 저장할 공간을 마련합니다.
app.state.rms_node: Optional[Any] = None

# '/images' URL을 'static/images' 로컬 폴더에 연결
app.mount("/images", StaticFiles(directory="static/images"), name="images")

# gui_router를 메인 앱에 포함
app.include_router(gui_router.router, prefix="/api/gui", tags=["GUI"])

@app.get("/")
def read_root():
    return {"Hello": "Roomie"}