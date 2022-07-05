from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src import settings

remote_engine = create_engine(settings.REMOTE_DATABASE_URL, echo=settings.DEBUG)
RemoteSession = sessionmaker(bind=remote_engine)
RemoteBase = declarative_base(bind=remote_engine)


def get_remote_db():
    db = RemoteSession()
    try:
        yield db
    finally:
        db.close()
