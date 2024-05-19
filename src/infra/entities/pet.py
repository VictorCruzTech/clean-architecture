import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from src.infra.config.db_base import Base


class AnimalTypes(enum.Enum):
    """Defining animals types"""

    DOG = "dog"
    CAT = "cat"
    FISH = "fish"
    TURTLE = "turtle"


class Pet(Base):
    """Pets Entity"""

    __tablename__ = "pet"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}]"
