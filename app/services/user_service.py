from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.core.security import hash_password

class UserService:
    @staticmethod
    async def get_by_email(session:AsyncSession, email:str) -> Optional[User]:
        result = await session.execute(select(User).filter(User.email == email))
        return result.scalars().first()

    @staticmethod
    async def create_user(session: AsyncSession, email: str,password: str):
        existing = await UserService.get_by_email(session,email)
        if existing:
            raise ValueError("User already exists")

        hashed_pw = hash_password(password)
        user = User(email=email,hashed_password=hashed_pw)

        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user