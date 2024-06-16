from abc import ABC, abstractmethod
from typing import List
from src.domain.models import User


class UserRepositoryInterface(ABC):
    """Interface to Pet Repository."""

    @abstractmethod
    def insert_user(self, name: str, password: str, cpf: str) -> User:
        raise NotImplementedError()

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[User]:
        raise NotImplementedError()
