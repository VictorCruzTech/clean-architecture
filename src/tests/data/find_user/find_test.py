import pytest
from sqlalchemy.orm.exc import NoResultFound

from faker import Faker
from src.data.find_user.find import FindUserImpl
from src.data.register_user.register import RegisterUserImpl
from src.infra.repo.user_repository import UserRepository
from src.tests.infra.repo.factories import (
    delete_data_from_user_table_by_cpf,
    generate_cpf,
)


faker = Faker()
user_repo = UserRepository()


def test_find_by_id():
    find_user = FindUserImpl(user_repo)
    register_user = RegisterUserImpl(user_repo)
    name = faker.name()
    password = faker.password()
    cpf = generate_cpf()

    register_user.register(name, password, cpf)

    response = find_user.by_id(user_id=1)

    assert response["Success"] is True
    assert response["Data"][0].name == name

    delete_data_from_user_table_by_cpf(cpf)


def test_find_by_name():
    find_user = FindUserImpl(user_repo)
    register_user = RegisterUserImpl(user_repo)
    name = faker.name()
    password = faker.password()
    cpf = generate_cpf()

    register_user.register(name, password, cpf)

    response = find_user.by_name(name=name)

    assert response["Success"] is True
    assert response["Data"][0].name == name

    delete_data_from_user_table_by_cpf(cpf)


def test_find_by_id_and_name():
    find_user = FindUserImpl(user_repo)
    register_user = RegisterUserImpl(user_repo)
    name = faker.name()
    password = faker.password()
    cpf = generate_cpf()

    register_user.register(name, password, cpf)

    response = find_user.by_id_and_name(user_id=1, name=name)

    assert response["Success"] is True
    assert response["Data"][0].name == name

    delete_data_from_user_table_by_cpf(cpf)


def test_find_with_non_existent_name():
    find_user = FindUserImpl(user_repo)
    register_user = RegisterUserImpl(user_repo)
    name = faker.name()
    password = faker.password()
    cpf = generate_cpf()

    with pytest.raises(NoResultFound):
        register_user.register(name, password, cpf)

        response = find_user.by_name(name="Other Name")

        assert response["Success"] is False
        assert response["Data"][0] is None

    delete_data_from_user_table_by_cpf(cpf)
