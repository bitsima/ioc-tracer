from sqlalchemy import Column, Integer, Text, JSON
from sqlalchemy.orm import relationship
from ..database_setup import Base


class File(Base):
    __tablename__ = "files"
    file_id = Column(Integer, primary_key=True)
    file_name = Column(Text, nullable=False)
    file_path = Column(Text, nullable=False)

    analysis_results = Column(JSON, nullable=True)

    file_hashes = relationship(
        "Hash", back_populates="file", cascade="all, delete-orphan"
    )
