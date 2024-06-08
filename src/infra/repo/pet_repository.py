from typing import List
from src.domain.models.pet import Pet
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pet as PetModel


class PetRepository:
    """Class to manage Pet Repository"""

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, user_id: int) -> Pet:
        """
        Insert data in PetEntity entity
        :param  - name: name of the pet
                - specie: Enum with species accepted
                - age: pet age
                - user_id: id of the Owner (FK)
        :return - tuple with new pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetModel(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pet(
                    id=new_pet.id,
                    name=new_pet.name,
                    age=new_pet.age,
                    user_id=new_pet.user_id,
                    specie=new_pet.specie.value,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pet]:
        """
        Select data in user entity by id and/or name
        :param  - pet_id: Id of the registry
                - name: User name
        :return - List with User selected
        """

        try:
            query_data = None

            if pet_id and not user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetModel).filter_by(id=pet_id).one()
                    )
                    query_data = [data]

            elif not pet_id and user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = [data]

            elif pet_id and user_id:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(PetModel)
                        .filter_by(id=pet_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except:
            db_connection.session.rollback()
            raise

        finally:
            db_connection.session.close()
