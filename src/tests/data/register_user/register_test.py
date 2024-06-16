from faker import Faker
from src.data.register_user.register import RegisterUserImpl
from src.infra.repo.user_repository import UserRepository
from src.domain.models import User
from src.tests.infra.repo.factories import delete_data_from_user_table_by_cpf

faker = Faker()
repository = UserRepository()


def test_register_success():
    register_user = RegisterUserImpl(repository)
    name = "Victor Cruz"
    password = "Senha123"
    cpf = "10020030088"

    expected_response = {
        "Success": True,
        "Data": User(id=1, name="Victor Cruz", password="Senha123", cpf="10020030088"),
    }
    response = register_user.register(name, password, cpf)

    assert response == expected_response

    delete_data_from_user_table_by_cpf(cpf)


def test_register_fail():
    register_user = RegisterUserImpl(repository)
    name = "Victor Cruz"
    password = 12345
    cpf = "10020030088"

    expected_response = {"Success": False, "Data": None}
    response = register_user.register(name, password, cpf)

    assert response == expected_response

    delete_data_from_user_table_by_cpf(cpf)
