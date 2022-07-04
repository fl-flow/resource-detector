from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src import settings


engine = create_engine(settings.LOCAL_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
