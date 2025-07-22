from pydantic_settings import BaseSettings
from pydantic import AnyUrl, Field
from typing import List

class Settings(BaseSettings):
    app_title: str = "SkillSwap API"
    app_version: str = "1.0.0"
    allowed_origins: List[str] = Field(default_factory=lambda: ["*"])

    REDIS_URL: AnyUrl = Field(..., env="REDIS_URL")
    RABBITMQ_URL: AnyUrl = Field(..., env="RABBITMQ_URL")

    DATABASE_URL: AnyUrl = Field(..., env="DATABASE_URL")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")

    access_token_expire_minutes: int = 30

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

settings = Settings()

