from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user, get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)


@router.get("/me", response_model=UserResponse)
def get_my_profile(
    current_user = Depends(get_current_user)
):
    return current_user