"""Application configuration using Pydantic Settings."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Load configuration from .env file."""

    # PostgreSQL
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int
    database_url: str

    # Neo4j
    neo4j_uri: str
    neo4j_user: str
    neo4j_password: str

    # Redis
    redis_url: str

    # API
    api_host: str
    api_port: int
    secret_key: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()