from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import User


class FindUserInterface(ABC):
    """Interface to Find User use_case"""

    @abstractmethod
    def by_id(cls, user_id: int) -> Dict[bool, List[User]]:
        raise NotImplementedError()

    @abstractmethod
    def by_name(cls, name: int) -> Dict[bool, List[User]]:
        raise NotImplementedError()

    @abstractmethod
    def by_id_and_name(cls, user_id: int, name: str) -> Dict[bool, List[User]]:
        raise NotImplementedError()
