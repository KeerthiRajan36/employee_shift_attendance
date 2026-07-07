from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Employee Shift & Attendance Management System"

    DATABASE_URL: str = "sqlite:///./attendance.db"

    SECRET_KEY: str = "employee_shift_secret_key"

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


settings = Settings()