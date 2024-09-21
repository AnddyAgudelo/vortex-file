from enum import Enum

from pydantic_settings import BaseSettings


class EnvironmentOptionsEnum(str, Enum):
    LOCAL = "LOCAL"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"


class Settings(BaseSettings):
    ENV: EnvironmentOptionsEnum
    DB_CONNECTION: str
    DB_NAME: str
    API_STR: str = "/api"


settings = Settings()
