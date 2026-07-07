from sqlalchemy import Boolean, ForeignKey
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from app.database.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    phone = Column(String(20), nullable=False)

    department = Column(String(100), nullable=False)

    designation = Column(String(100), nullable=False)

    is_active = Column(Boolean, default=True)

    user = relationship("User")


    attendance = relationship(
        "Attendance",
        back_populates="employee"
    )