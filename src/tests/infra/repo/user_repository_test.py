from faker import Faker
from src.infra.entities.user import User
from src.infra.repo.user_repository import UserRepository
from src.tests.infra.repo.factories import delete_data_from_user_table, generate_cpf

from sqlalchemy import select


user_repo = UserRepository()
faker = Faker()


def test_insert_user(db_session):
    name = faker.name()
    password = faker.password()
    cpf = generate_cpf()

    new_user = user_repo.insert_user(name=name, password=password, cpf=cpf)
    print(new_user)

    stmt = select(User.name, User.password, User.cpf).where(User.id == new_user.id)
    result = db_session.execute(stmt).one()

    assert new_user.name == result.name
    assert new_user.password == result.password
    assert new_user.cpf == result.cpf

    delete_data_from_user_table(new_user.id)
