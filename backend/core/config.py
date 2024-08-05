"""
    _summary_
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """_summary_

    Args:
        BaseSettings (_type_): _description_
    """
    PROJECT_NAME: str
    

    # Postgres connection
    PGS_DB_HOST: str
    PGS_DB_SID: str
    PGS_DB_PORT: int
    PGS_DB_USER_NAME: str
    PGS_DB_PASSWORD: str
    PGS_DB_DRIVER: str
    PGS_DEBUG_FLAG: int
    PGS_ENABLE_APPS_SESSION: str
    PGS_DB_SCHEMA: str
    PGS_AUTOFLUSH: bool
    PGS_AUTOCOMMIT: bool
    VERSION: str

    API_HOST: str
    API_ALLOW_ORIGINS: list
    API_PORT: int
    API_WORKERS: int
    API_DEBUG_MODE: bool
    API_DEBUG_LEVEL: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
