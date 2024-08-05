"""
    _summary_

    Raises:
        credentials_exception: _description_
        credentials_exception: _description_
        credentials_exception: _description_

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
"""
from core.config import settings
from db.database import SessionLocal
from utils.logging import logger


def get_db():
    """
    _summary_

    Yields:
        _type_: _description_
    """

    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        logger.debug(e)
    finally:
        db.close()

