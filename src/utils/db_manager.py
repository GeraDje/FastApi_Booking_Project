from src.config import settings
from src.repositories.bookigs import BookingsRepository
from src.repositories.facilities import FacilitiesRepository, RoomsFacilitiesRepository
from src.repositories.hotels import HotelsRepository
from src.repositories.rooms import RoomsRepository
from src.repositories.users import UsersRepository

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import text
import logging


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.hotels = HotelsRepository(self.session)
        self.rooms = RoomsRepository(self.session)
        self.users = UsersRepository(self.session)
        self.bookings = BookingsRepository(self.session)
        self.facilities = FacilitiesRepository(self.session)
        self.rooms_facilities = RoomsFacilitiesRepository(self.session)
        return self

    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()


class DatabaseConnector:

    def __init__(self):
        self.engine = None
        self.connected = False

    async def connect(self):
        """Подключение к БД с проверкой"""
        try:
            # Создаем движок
            self.engine = create_async_engine(
                settings.DB_URL,
            )

            # Пытаемся выполнить простой запрос для проверки
            async with self.engine.connect() as conn:
                await conn.execute(text("SELECT 1"))

            self.connected = True
            logging.info(f"✅ Database connected successfully,"
                         f" host: {settings.DB_HOST},"
                         f" port: {settings.DB_PORT}, "
                         f"db_name: {settings.DB_NAME}")

        except Exception as e:
            self.connected = False
            logging.error(f"❌ Database connection failed: {e}")
            raise

    async def close(self):
        """Закрытие соединения"""
        if self.engine:
            await self.engine.dispose()
            logging.info("📴 Database connection closed")


db_manager = DatabaseConnector()
