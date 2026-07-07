from fastapi import FastAPI

from app.database.database import Base
from app.database.database import engine

from app.config import settings

from app.models import *

from app.routers.auth_router import router as auth_router
from app.routers.employee_router import router as employee_router
from app.routers.shift_router import router as shift_router
from app.routers.attendance_router import router as attendance_router
from app.routers.report_router import router as report_router
from app.exceptions.handlers import register_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

register_exception_handlers(app)

app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(shift_router)
app.include_router(attendance_router)
app.include_router(report_router)


@app.get("/")
def home():
    return {
        "message": settings.APP_NAME
    }