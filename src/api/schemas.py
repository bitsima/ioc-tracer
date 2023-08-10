from enum import Enum
from typing import Optional, Dict
from pydantic import BaseModel


# Enum for IOC types
class IOCTypes(str, Enum):
    file = "file"
    file_hash = "file_hash"
    domain = "domain"
    ip_address = "ip_address"
    url_address = "url_address"


class IOCCreate(BaseModel):
    ioc_type: IOCTypes
    benign: Optional[bool] = None


class IOCUpdate(BaseModel):
    benign: Optional[bool] = None


class File(BaseModel):
    file_name: str
    file_path: str

    analysis_results = Dict


class FileHash(BaseModel):
    hash_type: str
    hash_value: str

    class Config:
        from_attributes = True


class Domain(BaseModel):
    domain_name: str


class IPAddress(BaseModel):
    ip_address: str


class UrlAddress(BaseModel):
    url_address_id = int
    url_address = str
