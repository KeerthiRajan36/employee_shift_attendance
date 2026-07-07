from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.report_service import monthly_report

from app.utils.dependency import admin_required

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/monthly")
def report(
    month: int,
    year: int,
    employee_id: int = None,
    department: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):

    return monthly_report(
        db,
        month,
        year,
        employee_id,
        department,
        page,
        limit
    )