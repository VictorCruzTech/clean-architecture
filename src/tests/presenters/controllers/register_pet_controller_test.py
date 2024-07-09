from src.data.find_user.find import FindUserImpl
from src.data.register_pet.register import RegisterPetImpl

from src.infra.entities.pet import AnimalTypes
from src.infra.repo.pet_repository import PetRepository
from src.infra.repo.user_repository import UserRepository

from src.presenters.controllers.register_pet_controller import RegisterPetController
from src.presenters.helpers.http_models import HttpRequest

from src.tests.infra.repo.factories import clear_db_data


pet_repo = PetRepository()
user_repo = UserRepository()
find_user = FindUserImpl(user_repo)
register_pet = RegisterPetImpl(pet_repo, find_user)


def test_register_pet_controller(create_user):
    user_id = create_user[0]
    user_name = create_user[1]
    user_information = {"user_id": user_id, "user_name": user_name}

    request = HttpRequest(
        body={
            "name": "Feinho",
            "specie": AnimalTypes.DOG.value,
            "user_information": user_information,
            "age": 13,
        }
    )

    register_pet_controller = RegisterPetController(register_pet)

    response = register_pet_controller.route(request)

    assert response.status_code == 200
    assert response.body

    clear_db_data()
