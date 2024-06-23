import random
from faker import Faker
from src.data.find_user.find import FindUserImpl
from src.data.register_pet.register import RegisterPetImpl
from src.data.register_user.register import RegisterUserImpl
from src.domain.models.pet import Pet
from src.infra.entities.pet import AnimalTypes
from src.infra.repo.user_repository import UserRepository
from src.infra.repo.pet_repository import PetRepository
from src.tests.infra.repo.factories import (
    delete_data_from_pet_table,
    delete_data_from_user_table_by_cpf,
    generate_cpf,
)


faker = Faker()
pet_repo = PetRepository()
user_repo = UserRepository()
find_user = FindUserImpl(user_repo)


def test_register_success():
    register_pet = RegisterPetImpl(pet_repo, find_user)
    register_user = RegisterUserImpl(user_repo)
    name = faker.name()
    specie = AnimalTypes.TURTLE
    password = faker.password()
    cpf = generate_cpf()
    age = random.randint(1, 100)

    new_user = register_user.register(name, password, cpf)

    user_information = {
        "user_id": new_user["Data"].id,
        "user_name": new_user["Data"].name,
    }

    expected_response = {
        "Success": True,
        "Data": Pet(
            id=1,
            name=name,
            specie=specie.value,
            age=age,
            user_id=user_information["user_id"],
        ),
    }

    response = register_pet.registry(
        name=name, specie=specie, user_information=user_information, age=age
    )

    assert response == expected_response

    delete_data_from_user_table_by_cpf(cpf)
    delete_data_from_pet_table(response["Data"].id)
