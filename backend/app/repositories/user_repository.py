from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:

    @staticmethod
    def get_by_email(db: Session, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return db.scalar(statement)

    @staticmethod
    def get_by_id(db: Session, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)
        return db.scalar(statement)

    @staticmethod
    def get_all_users(db: Session) -> list[User]:
        statement = select(User).order_by(User.id)
        return list(db.scalars(statement).all())

    @staticmethod
    def create(
        db: Session,
        user_data: UserCreate,
        hashed_password: str,
    ) -> User:
        user = User(
            full_name=user_data.full_name,
            email=str(user_data.email),
            hashed_password=hashed_password,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def update(
        db: Session,
        user: User,
        user_data: UserUpdate,
    ) -> User:
        user.full_name = user_data.full_name

        db.commit()
        db.refresh(user)

        return user
    @staticmethod
    def delete(db: Session, user: User) -> None:
        db.delete(user)
        db.commit()    