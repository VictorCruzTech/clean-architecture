from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import User


class RegisterUserInterface(ABC):
    """Interface to RegisterUser use case"""

    @abstractmethod
    def register(cls, name: str, password: str, cpf: str) -> Dict[bool, User]:
        raise NotImplementedError()
