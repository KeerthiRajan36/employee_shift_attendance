from sqlalchemy.orm import Session

from app.models.attendance import Attendance
from app.models.employee import Employee

from sqlalchemy import extract


def monthly_report(
    db: Session,
    month: int,
    year: int,
    employee_id: int = None,
    department: str = None,
    page: int = 1,
    limit: int = 10
):

    query = db.query(
        Attendance
    ).join(Employee)

    query = query.filter(
        extract("month", Attendance.date) == month,
        extract("year", Attendance.date) == year
    )

    if employee_id:

        query = query.filter(
            Attendance.employee_id == employee_id
        )

    if department:

        query = query.filter(
            Employee.department == department
        )

    return query.offset(
        (page - 1) * limit
    ).limit(limit).all()