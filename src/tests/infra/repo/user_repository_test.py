import random

from faker import Faker
from src.infra.entities.user import User
from src.infra.repo.user_repository import UserRepository
from src.tests.infra.repo.factories import delete_data_from_user_table, generate_cpf
from src.infra.entities import User as UserModel
from sqlalchemy import select, insert


user_repo = UserRepository()
faker = Faker()


def test_insert_user(db_session):
    name = faker.name()
    password = faker.password()
    cpf = generate_cpf()

    new_user = user_repo.insert_user(name=name, password=password, cpf=cpf)

    stmt = select(User.name, User.password, User.cpf).where(User.id == new_user.id)
    result = db_session.execute(statement=stmt).one()

    assert new_user.name == result.name
    assert new_user.password == result.password
    assert new_user.cpf == result.cpf

    delete_data_from_user_table(new_user.id)


def test_select_user(db_session):
    user_id = random.randint(1, 50)
    name = faker.name()
    password = faker.password()
    cpf = generate_cpf()
    data = UserModel(id=user_id, name=name, password=password, cpf=cpf)

    stmt = insert(UserModel).values(id=user_id, name=name, password=password, cpf=cpf)
    db_session.execute(statement=stmt)
    db_session.commit()

    query_user1 = user_repo.select_user(user_id=user_id)
    query_user2 = user_repo.select_user(name=name)
    query_user3 = user_repo.select_user(user_id=user_id, name=name)

    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    delete_data_from_user_table(user_id)
