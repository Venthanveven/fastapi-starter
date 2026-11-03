from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:

    @staticmethod
    def create_user(db: Session, user_data: UserCreate):
        existing_user = UserRepository.get_by_email(
            db,
            str(user_data.email),
        )

        if existing_user:
            raise ValueError("Email already registered")

        hashed_password = hash_password(user_data.password)

        return UserRepository.create(
            db=db,
            user_data=user_data,
            hashed_password=hashed_password,
        )

    @staticmethod
    def get_all_users(db: Session):
        return UserRepository.get_all_users(db)

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        user = UserRepository.get_by_id(db, user_id)

        if user is None:
            raise ValueError("User not found")

        return user

    @staticmethod
    def update_user(
        db: Session,
        user_id: int,
        user_data: UserUpdate,
    ):
        user = UserRepository.get_by_id(db, user_id)

        if user is None:
            raise ValueError("User not found")

        return UserRepository.update(
            db=db,
            user=user,
            user_data=user_data,
        )
    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = UserRepository.get_by_id(db, user_id)

        if user is None:
            raise ValueError("User not found")

        UserRepository.delete(db, user)    