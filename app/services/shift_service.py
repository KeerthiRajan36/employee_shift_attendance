from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.shift import Shift

from app.schemas.shift_schema import ShiftCreate
from app.schemas.shift_schema import ShiftUpdate


def create_shift(
    shift: ShiftCreate,
    db: Session
):

    if shift.end_time <= shift.start_time:

        raise HTTPException(
            status_code=400,
            detail="End Time must be greater than Start Time"
        )

    new_shift = Shift(**shift.model_dump())

    db.add(new_shift)

    db.commit()

    db.refresh(new_shift)

    return new_shift


def get_all_shifts(db: Session):

    return db.query(Shift).all()


def update_shift(
    shift_id: int,
    shift: ShiftUpdate,
    db: Session
):

    db_shift = db.query(Shift).filter(
        Shift.id == shift_id
    ).first()

    if not db_shift:

        raise HTTPException(
            status_code=404,
            detail="Shift Not Found"
        )

    for key, value in shift.model_dump().items():
        setattr(db_shift, key, value)

    db.commit()

    db.refresh(db_shift)

    return db_shift