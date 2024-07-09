from src.infra.repo.pet_repository import PetRepository
from src.infra.repo.user_repository import UserRepository
from src.data.register_pet import RegisterPetImpl
from src.data.find_user import FindUserImpl
from src.presenters.controllers import RegisterPetController


def register_pet_composer() -> RegisterPetController:
    """Composing Register Pet Route
    :param  - None
    :return - Object with Register Pet Route
    """

    repository = PetRepository()
    find_user_use_case = FindUserImpl(UserRepository())
    use_case = RegisterPetImpl(repository, find_user_use_case)
    register_pet_route = RegisterPetController(use_case)

    return register_pet_route
