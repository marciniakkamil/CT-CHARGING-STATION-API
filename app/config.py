"""Main settings for the whole project

Provides Settings object
"""
import os
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


# todo integrate dev,stg,prd environments
class Settings(BaseSettings):
    """App settings class"""

    db_url: PostgresDsn = os.getenv("DATABASE_URL")
    secret_key: str = os.getenv("SECRET_KEY")
    algoritm: str = os.getenv("ALGORITHM")
    access_token_exp_seconds: str = os.getenv("ACCESS_TOKEN_EXPIRE_SECONDS")


settings = Settings()
