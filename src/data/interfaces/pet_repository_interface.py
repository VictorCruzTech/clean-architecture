from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pet


class PetRepositoryInterface(ABC):
    """Interface to Pet Repository."""

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pet:
        raise NotImplementedError()

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pet]:
        raise NotImplementedError()
