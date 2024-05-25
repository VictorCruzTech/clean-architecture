import pytest

from src.infra.config.db_config import DBConnectionHandler
from sqlalchemy.orm import Session


@pytest.fixture(scope="function", autouse=True)
def db_session():
    db_connection_handler = DBConnectionHandler()

    engine = db_connection_handler.get_engine()
    session = Session(engine)

    return session


# @pytest.fixture
# def get_fixture(*args, **kwargs):
#     def _get_fixture(*args, **kwargs):
#         with open(kwargs["path"], "r") as f:
#             return json.loads(f.read())

#     yield _get_fixture
