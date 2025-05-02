from config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# MySQL connection string format:
# dialect+driver://username:password@host:port/database
# DATABASE_URL = "mysql+pymysql://your_user:your_password@localhost:3306/your_database"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Base model
Base = declarative_base()
