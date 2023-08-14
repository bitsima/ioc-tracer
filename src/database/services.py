from sqlalchemy import orm

from typing import Dict, Any, Optional

from .models import IOC
from ..api import schemas


async def create_hash(
    ioc: schemas.IOCCreate, session: orm.Session
) -> schemas.IOCCreate:
    ioc_model = IOC(**ioc.model_dump())
    session.add(ioc_model)
    session.commit()
    session.refresh(ioc_model)

    return schemas.FileHash(**ioc_model.__dict__)


async def get_iocs(fetch_size: int, session: orm.Session) -> list[schemas.IOCUpdate]:
    iocs = session.query(IOC).limit(fetch_size).all()

    return list(map(IOC.model_validate, iocs))


async def get_ioc(ioc_id: int, session: orm.Session) -> IOC:
    file_hash = session.query(IOC).filter(IOC.id == ioc_id).first()
    return file_hash


async def delete_hash(file_hash: IOC, session: orm.Session) -> None:
    session.delete(file_hash)
    session.commit()


async def update_analysis_results(
    ioc_id: int, analysis_results: Dict[str, Any], session: orm.Session
) -> Optional[IOC]:
    ioc = session.query(IOC).filter(IOC.id == ioc_id).first()
    if ioc:
        ioc.analysis_results = analysis_results
        session.commit()
        session.refresh(ioc)
        return ioc
