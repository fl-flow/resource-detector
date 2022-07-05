from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src import settings

local_engine = create_engine(settings.LOCAL_DATABASE_URL, echo=settings.DEBUG)
LocalSession = sessionmaker(bind=local_engine)
LocalBase = declarative_base(bind=local_engine)


def get_local_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
