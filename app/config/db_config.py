from app.config.vars_config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = settings.SQLALCHEMY_DATABASE_URI
engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    try:
        print("Trying to get the db cursor...")
        db = SessionLocal()
        yield db
    except:
        print("Database connection failed...")
    finally:
        print("Closing the connection...")
        db.close()
        print("Closed!")
