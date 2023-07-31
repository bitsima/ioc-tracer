from sqlalchemy import Column, Integer, Text
from ..database_setup import Base


class Domain(Base):
    __tablename__ = "domains"
    domain_id = Column(Integer, primary_key=True)
    domain_name = Column(Text, nullable=False)
    benign = Column(Integer, nullable=True)
