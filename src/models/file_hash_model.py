from sqlalchemy import Column, Integer, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from ..database_setup import Base


class FileHash(Base):
    __tablename__ = "file_hashes"

    file_hash_id = Column(Integer, primary_key=True)

    hash_type = Column(
        Enum("MD5", "SHA-1", "SHA-256", name="hash_types"), nullable=False
    )
    file_name = Column(Text, ForeignKey("files.file_name"))

    hash_value = Column(Text, nullable=False)

    file = relationship("File", back_populates="file_hashes")
