from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import User


class UserRepository:
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str, cpf: str) -> User:
        """Insert data in user entity
        :param  -   name: person name
                -   password: user password
                -   cpf: user cpf
        :return - tuple with new user inserted
        """

        InsertData = namedtuple("User", "id, name, password, cpf")

        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(name=name, password=password, cpf=cpf)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return InsertData(
                    id=new_user.id,
                    name=new_user.name,
                    password=new_user.password,
                    cpf=new_user.cpf,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None
