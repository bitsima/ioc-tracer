from sqlalchemy import create_engine
from sqlalchemy import orm

from models.file_model import File
from models.file_hash_model import FileHash
from models.domain_model import Domain
from models.ip_address_model import IPAddress
from ..config import DATABASE_URL

Base = orm.declarative_base()

engine = create_engine(DATABASE_URL)

SessionLocal = orm.sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base.metadata.create_all(engine, checkfirst=True)


def get_session() -> orm.Session:
    """Used to get new local session instances for the database.

    Yields:
        orm.Session: a new local session instance
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
