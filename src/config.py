from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

# определяем абсолютный путь до корня проекта
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    DB_NAME: str

    model_config = SettingsConfigDict(
        # pathlib позволяет формировать путь
        # с помощью оператора "/", аналогично os.path.join()
        env_file=BASE_DIR / ".env",
    )


settings = Settings()