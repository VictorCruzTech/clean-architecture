import random

from sqlalchemy import delete
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.user import User


def delete_data_from_user_table(user_id):
    with DBConnectionHandler() as db_connection:
        stmt = delete(User).where(User.id == user_id)
        res = db_connection.session.execute(stmt)
        db_connection.session.commit()

        print(f"Rows affected: {res.rowcount}")


def generate_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]

    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)

    return "%s%s%s.%s%s%s.%s%s%s-%s%s" % tuple(cpf)
