import logging
import random

from sqlalchemy import delete
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities.pet import Pet
from src.infra.entities.user import User


logger = logging.getLogger(__name__)


def clear_db_data():
    with DBConnectionHandler() as db_connection:
        print("LIMPANDO A TABELA PET...")
        stmt = delete(Pet).where(Pet.id >= 1)
        res = db_connection.session.execute(stmt)
        db_connection.session.commit()
        print("TABELA PET LIMPA :)")
        print(f"Rows affected: {res.rowcount}\n\n")

        print("LIMPANDO A TABELA USER...")
        stmt = delete(User).where(User.id >= 1)
        res = db_connection.session.execute(stmt)
        db_connection.session.commit()
        print("TABELA USER LIMPA :)")
        print(f"Rows affected: {res.rowcount}\n\n")


def generate_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]

    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)

    return "%s%s%s.%s%s%s.%s%s%s-%s%s" % tuple(cpf)
