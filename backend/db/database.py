"""
    _summary_
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATABASE_URL = f"{settings.PGS_DB_DRIVER}://{settings.PGS_DB_USER_NAME}:{settings.PGS_DB_PASSWORD}@{settings.PGS_DB_HOST}:{settings.PGS_DB_PORT}/{settings.PGS_DB_SID}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=settings.PGS_DEBUG_FLAG,
    pool_size=10,
    max_overflow=2,
    pool_recycle=300,
    pool_pre_ping=True,
    pool_use_lifo=True,
    pool_timeout=30,
)

SessionLocal = sessionmaker(autoflush=settings.PGS_AUTOFLUSH, bind=engine)
