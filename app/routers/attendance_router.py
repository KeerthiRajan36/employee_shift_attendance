from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.employee import Employee

from app.database.database import get_db

from app.schemas.attendance_schema import *

from app.services.attendance_service import *

from app.utils.dependency import (
    admin_required,
    get_current_user
)

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


@router.post("", response_model=AttendanceResponse)
def create(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return create_attendance(attendance, db)


@router.get("", response_model=list[AttendanceResponse])
def get_all(
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return get_all_attendance(db)


@router.get("/{employee_id}",
            response_model=list[AttendanceResponse])
def get_employee_records(
    employee_id: int,
    db: Session = Depends(get_db),
    current=Depends(get_current_user)
):
    emp = db.query(Employee).filter(
    Employee.user_id == current.id
).first()

    if current.role == "Employee":

        if emp is None:
            raise HTTPException(
                status_code=404,
                detail="Employee Profile Not Found"
            )

        if emp.id != employee_id:
            raise HTTPException(
                status_code=403,
                detail="Access Denied"
            )
            
        return get_employee_attendance(
            employee_id,
            db
        )


@router.put(
    "/{attendance_id}",
    response_model=AttendanceResponse
)
def update(
    attendance_id: int,
    attendance: AttendanceUpdate,
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return update_attendance(
        attendance_id,
        attendance,
        db
    )