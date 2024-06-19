from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Pet


class FindPetInterface(ABC):
    """Interface to FindPet use case"""

    @abstractmethod
    def by_pet_id(cls, pet_id: int) -> Dict[bool, List[Pet]]:
        raise NotImplementedError()

    @abstractmethod
    def by_user_id(cls, user_id: int) -> Dict[bool, List[Pet]]:
        raise NotImplementedError()

    @abstractmethod
    def by_pet_id_and_user_id(cls, pet_id: int, user_id: int) -> Dict[bool, List[Pet]]:
        raise NotImplementedError()
