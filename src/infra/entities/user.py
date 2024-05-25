from sqlalchemy import Column, String, Integer, Table, Float
from sqlalchemy.orm import relationship
from src.infra.config import Base
from src.infra.config.db_base import Metadata


class User(Base):
    """Users Entity"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=False)
    password = Column(String(255), nullable=False)
    cpf = Column(String(length=14), nullable=False, unique=True)
    id_pet = relationship("Pet")

    def __repr__(self):
        return f"User [name={self.name}]"


test_table = Table(
    "test_table",
    Metadata,
    Column("id", Integer, primary_key=True),
    Column("color", String(length=100), nullable=False),
    Column("year", Integer, unique=True, nullable=False),
    Column("value", Float(precision=2), nullable=False),
)
