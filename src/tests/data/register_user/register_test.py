from faker import Faker
from src.data.register_user.register import RegisterUserImpl
from src.infra.repo.user_repository import UserRepository
from src.domain.models import User
from src.tests.infra.repo.factories import clear_db_data, generate_cpf

faker = Faker()
user_repo = UserRepository()


def test_register_success():
    register_user = RegisterUserImpl(user_repo)
    name = faker.name()
    password = faker.password()
    cpf = generate_cpf()

    expected_response = {
        "Success": True,
        "Data": User(id=1, name=name, password=password, cpf=cpf),
    }
    response = register_user.register(name, password, cpf)

    assert response == expected_response

    clear_db_data()


def test_register_fail():
    register_user = RegisterUserImpl(user_repo)
    name = faker.name()
    password = 12345
    cpf = "10020030088"

    expected_response = {"Success": False, "Data": None}
    response = register_user.register(name, password, cpf)

    assert response == expected_response

    clear_db_data()
