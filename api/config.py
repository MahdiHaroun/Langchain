from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    langsmith_api_key: str
    langsmith_tracing: str
    langsmith_endpoint: Optional[str] = None
    langsmith_project: Optional[str] = None
    openai_api_key: Optional[str] = None

    class Config:
        env_file = ".env"
        extra = "ignore"  # This allows extra fields to be ignored


settings = Settings()