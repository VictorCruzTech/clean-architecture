import pytest


from faker import Faker
from src.data.register_user.register import RegisterUserImpl
from src.infra.repo.user_repository import UserRepository
from src.tests.infra.repo.factories import generate_cpf


@pytest.fixture()
def create_user():
    faker = Faker()
    user_repo = UserRepository()

    register_user = RegisterUserImpl(user_repo)
    name = faker.name()
    password = faker.password()
    cpf = generate_cpf()

    response = register_user.register(name, password, cpf)

    return response["Data"].id, response["Data"].name, response["Data"].cpf
