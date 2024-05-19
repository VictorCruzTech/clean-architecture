from src.infra.config import DBConnectionHandler
from src.infra.entities import User, Pet, AnimalTypes
from typing import Union


class FakerRepo:
    """A simple Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str, cpf: str) -> None:
        """something"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(name=name, password=password, cpf=cpf)
                print(f"Criando novo User com o nome: {name} e CPF: {cpf}")
                db_connection.session.add(new_user)
                db_connection.session.flush()
                db_connection.session.commit()
            except Exception as exc:
                print(str(exc))
                print(f"Erro ao criar User com o CPF: {cpf}")
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def insert_pet(
        cls, name: str, specie: Union[AnimalTypes], age: int, user_id: int
    ) -> None:
        """another thing"""
        with DBConnectionHandler() as db_connection:
            try:
                new_pet = Pet(name=name, specie=specie, age=age, user_id=user_id)
                print(
                    f"Criando novo Pet com o nome: {name} cujo dono tem o ID: {user_id}"
                )
                db_connection.session.add(new_pet)
                db_connection.session.flush()
                db_connection.session.commit()
            except Exception as exc:
                print(str(exc))
                print(
                    f"Erro ao criar novo Pet com o nome: {name} cujo dono tem o ID: {user_id}"
                )
                db_connection.session.rollback()
            finally:
                db_connection.session.close()
