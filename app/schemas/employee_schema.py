from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field
from pydantic import field_validator

import re


class EmployeeBase(BaseModel):

    name: str = Field(..., min_length=3, max_length=100)

    email: EmailStr

    phone: str

    department: str

    designation: str


    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value):

        pattern = r'^[6-9]\d{9}$'

        if not re.match(pattern, value):
            raise ValueError("Invalid phone number")

        return value


class EmployeeCreate(EmployeeBase):
    user_id: int
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):

    model_config = ConfigDict(from_attributes=True)

    id: int

    is_active: bool