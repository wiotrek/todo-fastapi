import os
from dotenv import load_dotenv
from pydantic import BaseSettings

from pathlib import Path

# path from settings env variable
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):

    # project information
    PROJECT_NAME: str = "Todo App"
    PROJECT_VERSION: str = "0.0.1"

    # fastapi config
    FASTAPI_PORT: int = os.getenv("FASTAPI_PORT", 3000)
    FASTAPI_RELOAD: bool = os.getenv("FASTAPI_RELOAD", False)
    FASTAPI_HOST: str = os.getenv("FASTAPI_HOST")

    # database config
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: int = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
