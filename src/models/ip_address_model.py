from sqlalchemy import Column, Integer, Text

from ..database_setup import Base


class IPAddress(Base):
    __tablename__ = "ip_addresses"

    ip_address_id = Column(Integer, primary_key=True)
    ip_address = Column(Text, nullable=False)
    benign = Column(Integer, nullable=True)
