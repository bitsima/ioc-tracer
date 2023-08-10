from sqlalchemy import Column, Integer, Text
from ..database_setup import Base


class UrlAddress(Base):
    __tablename__ = "url_addresses"

    url_address_id = Column(Integer, primary_key=True)
    url_address = Column(Text, nullable=False)
    benign = Column(Integer, nullable=True)
