from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import AuthService
from app.core.dependencies import get_current_user
from app.schemas.user import UserResponse


router = APIRouter()


@router.post(
    "/auth/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db),
):
    try:
        return AuthService.login(
            db=db,
            email=str(login_data.email),
            password=login_data.password,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error),
        ) from error
@router.get(
    "/auth/me",
    response_model=UserResponse,
)
def get_my_profile(
    current_user=Depends(get_current_user),
):
    return current_user
        
    