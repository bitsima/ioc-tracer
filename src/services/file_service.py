from sqlalchemy import orm

from ..helpers import file_hashing
from ..models import file_model
from ..models import file_hash_model
from ..api import schemas


async def create_file(file: schemas.File, session: orm.Session) -> schemas.File:
    file = file_model.File(**file.model_dump())
    md5_hash = file_hashing.hash_with_MD5(file.file_path)
    sha1_hash = file_hashing.hash_with_SHA1(file.file_path)
    sha256_hash = file_hashing.hash_with_SHA256(file.file_path)
    file.file_hashes.append(md5_hash)
    file.file_hashes.append(sha1_hash)
    file.file_hashes.append(sha256_hash)

    session.add(file)
    session.commit()
    session.refresh(file)

    return schemas.File(**file.__dict__)


async def get_files(fetch_size: int, session: orm.Session) -> list[schemas.File]:
    files = session.query(file_model.File).limit(fetch_size).all()

    return list(map(schemas.File.model_validate, files))


async def get_file(file_name: str, session: orm.Session) -> file_model.File:
    file = (
        session.query(file_model.File)
        .filter(file_model.File.file_name == file_name)
        .first()
    )
    return file


async def get_file_hash(file_name: str, session: orm.Session) -> str:
    file_hash = (
        session.query(file_hash_model.FileHash)
        .filter(file_hash_model.FileHash.file_name == file_name)
        .first()
    )
    return file_hash


async def delete_file(file: file_model.File, session: orm.Session) -> None:
    session.delete(file)
    session.commit()
