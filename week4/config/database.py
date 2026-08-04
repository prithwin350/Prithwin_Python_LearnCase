import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from config.settings import DATABASE_NAME

engine = db.create_engine(f"sqlite:///{DATABASE_NAME}")
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


def check_connection():
    try:
        with engine.connect():
            return True
    except Exception:
        return False