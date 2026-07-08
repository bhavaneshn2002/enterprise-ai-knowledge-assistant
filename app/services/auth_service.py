from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import (
    verify_password,
    create_access_token,
)


def authenticate_user(
    db: Session,
    email: str,
    password: str
):
    # Find user by email
    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return None

    # Verify password
    if not verify_password(
        password,
        user.password
    ):
        return None

    # Generate JWT token
    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }