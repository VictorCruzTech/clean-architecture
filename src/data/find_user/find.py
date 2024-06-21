from typing import Dict, List, Type
from src.data.interfaces import UserRepositoryInterface
from src.domain.models import User
from src.domain.use_cases import FindUserInterface


class FindUserImpl(FindUserInterface):
    """Class to define use case FindUser"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[User]]:
        """Select User By Id
        :param  - user_id: Id of the user
        return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: int) -> Dict[bool, List[User]]:
        """Select User By Id
        :param  - name: Name of the user
        return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[User]]:
        """Select User By Id
        :param  - user_id: Id of the user
        :param  - name: Name of the user
        return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id, name=name)

        return {"Success": validate_entry, "Data": response}
