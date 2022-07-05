import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

REMOTE_DATABASE_USER = ''
REMOTE_DATABASE_PASSWORD = ''
REMOTE_DATABASE_HOST = ''
REMOTE_DATABASE_PORT = ''
REMOTE_DATABASE_DB = ''
REMOTE_DATABASE_URL = f'mysql+mysqlconnector://{REMOTE_DATABASE_USER}:{REMOTE_DATABASE_PASSWORD}@{REMOTE_DATABASE_HOST}:{REMOTE_DATABASE_PORT}/{REMOTE_DATABASE_DB}'

LOCAL_DATABASE_URL = f'sqlite:///{BASE_DIR.joinpath("db.sqlite3")}'
