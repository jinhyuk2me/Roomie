from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import gui_router

app = FastAPI(title="Roomie Main Server")

# '/images' URL을 'static/images' 로컬 폴더에 연결
app.mount("/images", StaticFiles(directory="static/images"), name="images")

# gui_router를 메인 앱에 포함
app.include_router(gui_router.router, prefix="/api/gui", tags=["GUI"])

@app.get("/")
def read_root():
    return {"Hello": "Roomie"}