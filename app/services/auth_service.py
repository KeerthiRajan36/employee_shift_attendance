from sqlalchemy.orm import Session

from fastapi import HTTPException
from fastapi import status

from app.models.user import User

from app.schemas.auth_schema import UserRegister
from app.schemas.auth_schema import UserLogin

from app.utils.password import hash_password
from app.utils.password import verify_password

from app.utils.jwt_handler import create_access_token


def register_user(user: UserRegister, db: Session):

    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(user: UserLogin, db: Session):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    token = create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }