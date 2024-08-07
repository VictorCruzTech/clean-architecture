from src.data.register_user.register import RegisterUserImpl
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterUserController
from src.infra.repo.user_repository import UserRepository


def register_user_composer() -> RouteInterface:
    """Composing Register User Route
    :param  - None
    :return - Object with Register User Route
    """
    repository = UserRepository()
    use_case = RegisterUserImpl(repository)
    register_user_route = RegisterUserController(use_case)

    return register_user_route
