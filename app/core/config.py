from pydantic import BaseSettings, AnyUrl
from typing import List

class Settings(BaseSettings):
    app_title:str = "SkillSwap API"
    app_version:str = "1.0.0"
    allowed_origins: List[str] = ["*"]

    database_url: AnyUrl
    secret_key: str
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
