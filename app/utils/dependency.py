from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.user import User

from app.utils.jwt_handler import verify_token


security = HTTPBearer()


def get_current_user(
    credential: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credential.credentials
    payload = verify_token(token)

    if payload is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    email = payload.get("sub")

    if email is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User Not Found"
        )

    return user

def employee_required(
    current_user: User = Depends(get_current_user)
):

    if current_user.role != "Employee":

        raise HTTPException(
            status_code=403,
            detail="Employee Access Required"
        )

    return current_user

def admin_required(
    current_user: User = Depends(get_current_user)
):

    if current_user.role != "Admin":

        raise HTTPException(
            status_code=403,
            detail="Admin Access Required"
        )

    return current_user

def admin_or_employee(
    current_user: User = Depends(get_current_user)
):

    if current_user.role not in [
        "Admin",
        "Employee"
    ]:

        raise HTTPException(
            status_code=403,
            detail="Permission Denied"
        )

    return current_user