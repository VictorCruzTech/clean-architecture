from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.config import Base


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
