from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.repositories.user_repository import UserRepository


class AuthService:

    @staticmethod
    def login(db: Session, email: str, password: str) -> dict:
        user = UserRepository.get_by_email(db, email)

        if not user or not verify_password(
            password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password")

        if not user.is_active:
            raise ValueError("User account is inactive")

        access_token = create_access_token(subject=str(user.id))

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }