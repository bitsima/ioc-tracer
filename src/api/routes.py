import fastapi
from sqlalchemy import orm

from schemas import IOCCreate, IOCUpdate
from ..database.database_setup import get_session
from ...celery import tasks

app = fastapi.FastAPI()


@app.post("/search/domain", response_model=dict)
async def search_domain(ioc: IOCCreate, db: orm.Session = fastapi.Depends(get_session)):
    pass


@app.post("/search/ip", response_model=dict)
async def search_ip(ioc: IOCCreate, db: orm.Session = fastapi.Depends(get_session)):
    pass


@app.post("/search/hash", response_model=dict)
async def search_hash(ioc: IOCCreate, db: orm.Session = fastapi.Depends(get_session)):
    pass


@app.post("/search/url", response_model=dict)
async def search_url(ioc: IOCCreate, db: orm.Session = fastapi.Depends(get_session)):
    pass


@app.get("/iocs/{task_id}", response_model=dict)
async def get_analysis_results():
    pass
