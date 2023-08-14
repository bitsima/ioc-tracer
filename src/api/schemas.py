from enum import Enum
from pydantic import BaseModel


# Enum for IOC types
class IOCTypes(str, Enum):
    file_hash = "file_hash"
    domain = "domain"
    ip_address = "ip_address"
    url_address = "url_address"


class IOCCreate(BaseModel):
    ioc_type: IOCTypes
    ioc_detail: str


class IOCUpdate(IOCCreate):
    analysis_result: dict
