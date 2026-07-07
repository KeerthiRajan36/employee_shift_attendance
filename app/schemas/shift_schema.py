from datetime import time

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class ShiftBase(BaseModel):

    shift_name: str = Field(..., min_length=2)

    start_time: time

    end_time: time

    shift_type: str


class ShiftCreate(ShiftBase):
    pass


class ShiftUpdate(ShiftBase):
    pass


class ShiftResponse(ShiftBase):

    model_config = ConfigDict(from_attributes=True)

    id: int