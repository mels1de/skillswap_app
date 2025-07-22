from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_async_engine(str(settings.DATABASE_URL),echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session