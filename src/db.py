# src/db.py
# src/db.py
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


DATABASE_URL = "sqlite:///tasks.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
