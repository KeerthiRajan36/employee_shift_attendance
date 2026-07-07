from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.attendance import Attendance
from app.models.employee import Employee
from app.models.shift import Shift

from app.schemas.attendance_schema import AttendanceCreate
from app.schemas.attendance_schema import AttendanceUpdate


def create_attendance(
    attendance: AttendanceCreate,
    db: Session
):

    employee = db.query(Employee).filter(
        Employee.id == attendance.employee_id
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    shift = db.query(Shift).filter(
        Shift.id == attendance.shift_id
    ).first()

    if not shift:

        raise HTTPException(
            status_code=404,
            detail="Shift Not Found"
        )

    exists = db.query(Attendance).filter(
        Attendance.employee_id == attendance.employee_id,
        Attendance.date == attendance.date
    ).first()

    if exists:

        raise HTTPException(
            status_code=400,
            detail="Attendance Already Marked"
        )

    new_record = Attendance(
        **attendance.model_dump()
    )

    db.add(new_record)

    db.commit()

    db.refresh(new_record)

    return new_record

def get_all_attendance(db: Session):

    return db.query(Attendance).all()

def get_employee_attendance(
    employee_id: int,
    db: Session
):

    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()

def update_attendance(
    attendance_id: int,
    attendance: AttendanceUpdate,
    db: Session
):

    db_attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()

    if not db_attendance:

        raise HTTPException(
            status_code=404,
            detail="Attendance Not Found"
        )

    for key, value in attendance.model_dump().items():
        setattr(db_attendance, key, value)

    db.commit()

    db.refresh(db_attendance)

    return db_attendance