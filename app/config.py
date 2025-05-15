from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    exchange_api_key: str
    database_url: str = "currency.db"

    class Config:
        env_file = ".env"


settings = Settings()
