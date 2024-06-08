import random

from faker import Faker
from sqlalchemy import insert, select
from src.infra.entities.pet import AnimalTypes, Pet
from src.infra.entities import Pet as PetModel
from src.infra.repo.pet_repository import PetRepository
from src.infra.repo.user_repository import UserRepository
from src.tests.infra.repo.factories import delete_data_from_pet_table


user_repo = UserRepository()
pet_repo = PetRepository()
faker = Faker()


def test_insert_pet(db_session):
    name = faker.name()
    age = random.randint(1, 50)
    specie = AnimalTypes.FISH

    new_pet = pet_repo.insert_pet(name=name, specie=specie, age=age, user_id=10)

    stmt = select(Pet.name, Pet.age, Pet.specie, Pet.user_id).where(
        Pet.name == name, Pet.age == age
    )
    result = db_session.execute(statement=stmt).one()

    assert new_pet.name == result.name
    assert new_pet.specie == result.specie.value
    assert new_pet.age == result.age
    assert new_pet.user_id == result.user_id

    delete_data_from_pet_table(new_pet.id)


def test_select_user(db_session):
    pet_id = random.randint(1, 50)
    user_id = random.randint(1, 50)
    age = random.randint(1, 50)
    specie = AnimalTypes.DOG
    name = faker.name()
    data = PetModel(id=pet_id, name=name, age=age, specie=specie, user_id=user_id)

    stmt = insert(PetModel).values(
        id=pet_id, name=name, age=age, specie=specie, user_id=user_id
    )
    db_session.execute(statement=stmt)
    db_session.commit()

    query_pet1 = pet_repo.select_pet(pet_id=pet_id)
    query_pet2 = pet_repo.select_pet(user_id=user_id)
    query_pet3 = pet_repo.select_pet(pet_id=pet_id, user_id=user_id)

    assert data in query_pet1
    assert data in query_pet2[0]
    assert data in query_pet3

    delete_data_from_pet_table(pet_id)
