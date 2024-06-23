from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Pet


class RegisterPetInterface(ABC):
    """Interface to FindPet use case"""

    @abstractmethod
    def registry(
        cls, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pet]:
        raise NotImplementedError()
