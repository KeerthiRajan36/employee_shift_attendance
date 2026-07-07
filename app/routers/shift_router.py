from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.shift_schema import *

from app.services.shift_service import *

from app.utils.dependency import admin_required

router = APIRouter(
    prefix="/shifts",
    tags=["Shifts"]
)


@router.post("", response_model=ShiftResponse)
def create(
    shift: ShiftCreate,
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return create_shift(shift, db)


@router.get("", response_model=list[ShiftResponse])
def get_all(
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return get_all_shifts(db)


@router.put("/{shift_id}", response_model=ShiftResponse)
def update(
    shift_id: int,
    shift: ShiftUpdate,
    db: Session = Depends(get_db),
    current=Depends(admin_required)
):
    return update_shift(
        shift_id,
        shift,
        db
    )