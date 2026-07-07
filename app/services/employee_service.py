from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.models.user import User
from app.schemas.employee_schema import EmployeeCreate
from app.schemas.employee_schema import EmployeeUpdate


def create_employee(
    employee: EmployeeCreate,
    db: Session
):
    
    user = db.query(User).filter(
    User.id == employee.user_id
).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    if user.role != "Employee":
        raise HTTPException(
            status_code=400,
            detail="User must have Employee role"
        )

    exists = db.query(Employee).filter(
        Employee.email == employee.email
    ).first()

    if exists:
        raise HTTPException(
            status_code=400,
            detail="Employee Email Already Exists"
        )

    new_employee = Employee(**employee.model_dump())

    db.add(new_employee)

    db.commit()

    db.refresh(new_employee)

    return new_employee


def get_all_employees(db: Session):

    return db.query(Employee).filter(
        Employee.is_active == True
    ).all()


def get_employee(employee_id: int, db: Session):

    employee = db.query(Employee).filter(
        Employee.id == employee_id,
        Employee.is_active == True
    ).first()

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    return employee


def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session
):

    db_employee = get_employee(employee_id, db)

    for key, value in employee.model_dump().items():
        setattr(db_employee, key, value)

    db.commit()

    db.refresh(db_employee)

    return db_employee


def delete_employee(employee_id: int, db: Session):

    employee = get_employee(employee_id, db)

    employee.is_active = False

    db.commit()

    return {
        "message": "Employee Deleted Successfully"
    }