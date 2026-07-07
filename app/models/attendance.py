from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Time
from sqlalchemy import UniqueConstraint

from sqlalchemy.orm import relationship

from app.database.database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False
    )

    shift_id = Column(
        Integer,
        ForeignKey("shifts.id"),
        nullable=False
    )

    date = Column(Date, nullable=False)

    check_in = Column(Time, nullable=False)

    check_out = Column(Time, nullable=False)

    attendance_status = Column(String(30), nullable=False)

    employee = relationship(
        "Employee",
        back_populates="attendance"
    )

    shift = relationship(
        "Shift",
        back_populates="attendance"
    )

    __table_args__ = (
        UniqueConstraint(
            "employee_id",
            "date",
            name="uq_employee_date"
        ),
    )