from typing import List
from src.domain.models import User
from src.infra.config import DBConnectionHandler
from src.infra.entities import User as UserModel


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

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UserModel(name=name, password=password, cpf=cpf)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return User(
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

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[User]:
        """
        Select data in user entity by id and/or name
        :param  - user_id: Id of the registry
                - name: User name
        :return - List with User selected
        """

        try:
            query_data = None

            if user_id and not name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UserModel)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]

            elif not user_id and name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UserModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif user_id and name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UserModel)
                        .filter_by(id=user_id, name=name)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except:
            db_connection.session.rollback()
            raise

        finally:
            db_connection.session.close()
