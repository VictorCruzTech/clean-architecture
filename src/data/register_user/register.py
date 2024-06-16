from typing import Dict, Type
from src.domain.models import User
from src.domain.use_cases.register_user import RegisterUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository


class RegisterUserImpl(RegisterUserInterface):
    """Class to define usercase"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def register(self, name: str, password: str, cpf: str) -> Dict[str, User]:
        """Register user use_case
        :param  - name: person name
                - password: password of the person
                - cpf: cpf of the person
        :return: Dictionary with informations of the process
        """

        response = None
        validate_entry = all(
            [isinstance(name, str), isinstance(password, str), isinstance(cpf, str)]
        )

        if validate_entry:
            response = self.user_repository.insert_user(name, password, cpf)

        return {"Success": validate_entry, "Data": response}
