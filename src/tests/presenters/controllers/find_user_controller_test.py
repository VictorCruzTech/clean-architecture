from src.data.find_user.find import FindUserImpl
from src.infra.repo.user_repository import UserRepository
from src.presenters.controllers.find_user_controller import FindUserController
from src.presenters.helpers.http_models import HttpRequest
from src.tests.infra.repo.factories import delete_data_from_user_table_by_cpf


user_repo = UserRepository()
find_user_interface = FindUserImpl(user_repo)


def test_handle_with_user_id_and_user_name(create_user):
    user_id = create_user[0]
    user_name = create_user[1]
    request = HttpRequest(query={"user_id": user_id, "user_name": user_name})

    find_user = FindUserController(find_user_interface)

    response = find_user.handle(request)
    print(response)

    assert response.status_code == 200
    assert response.body

    delete_data_from_user_table_by_cpf(create_user[2])


def test_handle_no_query_param(create_user):
    request = HttpRequest()

    find_user = FindUserController(find_user_interface)

    response = find_user.handle(request)
    print(response)

    assert response.status_code == 400
    assert response.body == {"error": "Bad Request"}

    delete_data_from_user_table_by_cpf(create_user[2])


def test_handle_query_without_expected_keys(create_user):
    request = HttpRequest(query={"one_key": 1, "another_key": "teste"})

    find_user = FindUserController(find_user_interface)

    response = find_user.handle(request)
    print(response)

    assert response.status_code == 422
    assert response.body == {"error": "Unprocessable Entity"}

    delete_data_from_user_table_by_cpf(create_user[2])
