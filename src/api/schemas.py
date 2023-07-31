from enum import Enum
from typing import Optional
from pydantic import BaseModel


# Enum for IOC types
class IOCTypes(str, Enum):
    file = "file"
    file_hash = "file_hash"
    domain = "domain"
    ip_address = "ip_address"


class IOCCreate(BaseModel):
    ioc_type: IOCTypes
    benign: Optional[bool] = None


class IOCUpdate(BaseModel):
    benign: Optional[bool] = None


class File(BaseModel):
    file_name: str
    file_path: str


class FileHash(BaseModel):
    hash_type: str
    hash_value: str

    class Config:
        from_attributes = True


class Domain(BaseModel):
    domain_name: str


class IPAddress(BaseModel):
    ip_address: str


class YaraRule(BaseModel):
    rule_name: str
    rule_content: str
