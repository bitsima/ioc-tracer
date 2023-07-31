from sqlalchemy import orm

from ..models import file_hash_model
from ..api import schemas


async def create_hash(
    file_hash: schemas.FileHash, session: orm.Session
) -> schemas.FileHash:
    hash = file_hash_model.FileHash(**file_hash.model_dump())
    session.add(hash)
    session.commit()
    session.refresh(hash)

    return schemas.FileHash(**hash.__dict__)


async def get_hashes(fetch_size: int, session: orm.Session) -> list[schemas.FileHash]:
    hashes = session.query(file_hash_model.FileHash).limit(fetch_size).all()

    return list(map(schemas.FileHash.model_validate, hashes))


async def get_hash(hash_value: str, session: orm.Session) -> file_hash_model.FileHash:
    file_hash = (
        session.query(file_hash_model.FileHash)
        .filter(file_hash_model.FileHash.hash_value == hash_value)
        .first()
    )
    return file_hash


async def delete_hash(
    file_hash: file_hash_model.FileHash, session: orm.Session
) -> None:
    session.delete(file_hash)
    session.commit()
