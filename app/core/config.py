from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_TITLE: str = "YouTube Notes API"
    PROJECT_DESCRIPTION: str = "Сервис для создания конспектов по ссылке на YouTube"
    PROJECT_VERSION: str = "0.1.0"

    ALLOWED_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
