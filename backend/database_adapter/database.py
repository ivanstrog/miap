import databases
import sqlalchemy
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util.compat import contextmanager

DATABASE_URL = "sqlite:///./backend/app.db"
database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

Session = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base: DeclarativeMeta = declarative_base()


@contextmanager
def create_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


get_session = create_session
