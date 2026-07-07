from datetime import date
from datetime import time

from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import model_validator


class AttendanceBase(BaseModel):

    employee_id: int

    shift_id: int

    date: date

    check_in: time

    check_out: time

    attendance_status: Literal[
        "Present",
        "Absent",
        "Half Day",
        "Work From Home"
    ]


    @model_validator(mode="after")
    def validate_time(self):

        if self.check_out <= self.check_in:
            raise ValueError(
                "Check-out must be greater than check-in"
            )

        return self


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(AttendanceBase):
    pass


class AttendanceResponse(AttendanceBase):

    model_config = ConfigDict(from_attributes=True)

    id: int