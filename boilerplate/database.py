from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import logging

logger = logging.getLogger(__file__)

databasename = os.environ.get("config.sqlite.database.name")

# create sqlite database in current folder i.e., /config
SQLALCHAMY_DATABASE_URL = 'sqlite:///./' + databasename

logger.info('sqlite database created/reopend in . folder = %s', databasename)

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        logger.info('session is closed.')
        session.close()








