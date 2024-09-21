from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str
    DB_CONNECTION: str
    DB_NAME: str


settings = Settings()
