from sqlalchemy import Column, Integer, Text, JSON


from .database_setup import Base


class IOC(Base):
    __tablename__ = "ioc"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ioc_type = Column(Text, nullable=False)
    ioc_detail = Column(Text, nullable=False)

    analysis_result = Column(JSON, nullable=True)
