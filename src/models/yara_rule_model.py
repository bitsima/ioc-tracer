from sqlalchemy import Column, Integer, Text
from ..database_setup import Base


class YaraRule(Base):
    __tablename__ = "yara_rules"
    rule_id = Column(Integer, primary_key=True)
    rule_name = Column(Text, nullable=False)
    rule_content = Column(Text, nullable=False)
