from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

engin = create_async_engine(settings.DB_URL,echo= True)

async_session_maker = async_sessionmaker(bind=engin, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
