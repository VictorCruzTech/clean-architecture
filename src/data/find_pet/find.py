from typing import Dict, List, Type
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pet
from src.domain.use_cases import FindPetInterface


class FindPetImpl(FindPetInterface):
    """Class to define use case FindPet"""

    def __init__(self, pet_repository: Type[PetRepositoryInterface]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pet]]:
        """Select Pet By Id
        :param  - pet_id: Id of the pet
        return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pet]]:
        """Select Pet By Id
        :param  - user_id: Id of the user
        return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_user_id(self, pet_id: int, user_id: int) -> Dict[bool, List[Pet]]:
        """Select Pet By Id
        :param  - pet_id: Id of the pet
        :param  - user_id: Id of the user
        return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

        return {"Success": validate_entry, "Data": response}
