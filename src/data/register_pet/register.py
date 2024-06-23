from typing import Dict, List, Type
from src.data.find_user import FindUserImpl
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pet
from src.domain.models import User
from src.domain.use_cases import RegisterPetInterface
from src.infra.entities.pet import AnimalTypes


class RegisterPetImpl(RegisterPetInterface):
    """Class to define use case: Register Pet"""

    def __init__(
        self,
        pet_repository: Type[PetRepositoryInterface],
        find_user: Type[FindUserImpl],
    ):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def registry(
        self, name: str, specie: str, user_information: Dict[str, int], age: int = None
    ) -> Dict[bool, Pet]:
        """Registry Pet
        :param  - name: pet name
                - specie: type of the specie
                - user_information: Dictionary with user_id and/or user_name
                - age = age of the pet
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = all(
            [
                isinstance(name, str),
                isinstance(specie, AnimalTypes),
                isinstance(user_information, dict),
                isinstance(age, int),
            ]
        )
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(
                name=name, specie=specie, age=age, user_id=user_information["user_id"]
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[User]]:
        """Check user Infos and select user
        :param  - user_information: Dictionary with user_id and/or user_name
        :return -   Dictionary with the response of find_use use case
        """

        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_id_and_name(
                user_id=user_information["user_id"], name=user_information["user_name"]
            )

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_name(name=user_information["user_name"])

        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = self.find_user.by_id(user_id=user_information["user_id"])

        else:
            return {"Success": False, "Data": None}

        return user_founded
