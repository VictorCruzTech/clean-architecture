import logging
import random

from sqlalchemy import delete
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.pet import Pet
from src.infra.entities.user import User


logger = logging.getLogger(__name__)


def delete_data_from_user_table(user_id):
    with DBConnectionHandler() as db_connection:
        stmt = delete(User).where(User.id == user_id)
        res = db_connection.session.execute(stmt)
        db_connection.session.commit()

        logger.info(f"Rows affected: {res.rowcount}")


def delete_data_from_pet_table(pet_id):
    with DBConnectionHandler() as db_connection:
        stmt = delete(Pet).where(Pet.id == pet_id)
        res = db_connection.session.execute(stmt)
        db_connection.session.commit()

        logger.info(f"Rows affected: {res.rowcount}")


def generate_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]

    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)

    return "%s%s%s.%s%s%s.%s%s%s-%s%s" % tuple(cpf)
