import pytest
import random
from sqlalchemy.orm.exc import NoResultFound

from faker import Faker
from src.data.find_pet.find import FindPetImpl
from src.infra.entities.pet import AnimalTypes
from src.infra.repo.pet_repository import PetRepository
from src.tests.infra.repo.factories import clear_db_data


faker = Faker()
pet_repo = PetRepository()


def test_find_by_id():
    name = faker.name()
    specie = AnimalTypes.CAT
    age = random.randint(1, 50)
    find_pet = FindPetImpl(pet_repo)

    new_pet = pet_repo.insert_pet(name=name, specie=specie, age=age, user_id=10)

    response = find_pet.by_pet_id(pet_id=new_pet.id)

    assert response["Success"] is True
    assert response["Data"][0].name == name

    clear_db_data()


def test_find_by_user_id():
    name = faker.name()
    specie = AnimalTypes.CAT
    age = random.randint(1, 50)
    find_pet = FindPetImpl(pet_repo)

    new_pet = pet_repo.insert_pet(name=name, specie=specie, age=age, user_id=10)

    response = find_pet.by_user_id(user_id=new_pet.user_id)

    assert response["Success"] is True
    assert response["Data"][0][0].name == name

    clear_db_data()


def test_find_by_pet_id_and_user_id():
    name = faker.name()
    specie = AnimalTypes.CAT
    age = random.randint(1, 50)
    find_pet = FindPetImpl(pet_repo)

    new_pet = pet_repo.insert_pet(name=name, specie=specie, age=age, user_id=10)

    response = find_pet.by_pet_id_and_user_id(
        pet_id=new_pet.id, user_id=new_pet.user_id
    )

    assert response["Success"] is True
    assert response["Data"][0].name == name

    clear_db_data()


def test_find_by_non_existent_pet_id():
    name = faker.name()
    specie = AnimalTypes.CAT
    age = random.randint(1, 50)
    find_pet = FindPetImpl(pet_repo)

    pet_repo.insert_pet(name=name, specie=specie, age=age, user_id=10)

    with pytest.raises(NoResultFound):
        response = find_pet.by_pet_id(pet_id=500)

        assert response["Success"] is False
        assert response["Data"][0] is None

    clear_db_data()
