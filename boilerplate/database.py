from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import logging
from pathlib import Path

logger = logging.getLogger(__file__)

path_dir = Path(os.path.dirname(__file__))

databasename = os.environ.get("config.sqlite.database.name")

sqlitedb_path = str(path_dir) + '/' + databasename

# create sqlite database in current folder i.e., /config
SQLALCHAMY_DATABASE_URL = 'sqlite:///' + sqlitedb_path

logger.info('sqlite database created/reopend in . folder = %s', SQLALCHAMY_DATABASE_URL)

if ('dev' == os.environ.get('configEnvironment')):
    engine = create_engine(SQLALCHAMY_DATABASE_URL, pool_size=10, max_overflow=20, pool_timeout=6, connect_args={"check_same_thread": False}, echo=True)
else:
    # Hide database query logs (echo=False)
    engine = create_engine(SQLALCHAMY_DATABASE_URL, pool_size=10, max_overflow=0,connect_args={"check_same_thread": False}, echo=False)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        logger.info('session is closed.')
        session.close()








