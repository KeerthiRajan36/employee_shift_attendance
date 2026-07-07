from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.employee_schema import *

from app.services.employee_service import *

from app.utils.dependency import admin_required

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("", response_model=EmployeeResponse)
def create(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return create_employee(employee, db)


@router.get("", response_model=list[EmployeeResponse])
def get_all(
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return get_all_employees(db)


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_one(
    employee_id: int,
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return get_employee(employee_id, db)


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return update_employee(employee_id, employee, db)


@router.delete("/{employee_id}")
def delete(
    employee_id: int,
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return delete_employee(employee_id, db)