""""Objects needed to connect and work with database"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import settings

# get database url from the config
SQLALCHEMY_DATABASE_URL = settings.db_url.unicode_string()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for models or classes(ORM models) to inherit
Base = declarative_base()

# todo: change it to service
