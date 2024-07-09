from typing import Type

from src.domain.use_cases import RegisterUserInterface
from src.main.interface import RouteInterface
from src.presenters.errors.http_errors import HttpErrors
from src.presenters.helpers import HttpRequest, HttpResponse


class RegisterUserController(RouteInterface):
    """Class to define route to register_pet use case"""

    def __init__(self, register_user_use_case: Type[RegisterUserInterface]) -> None:
        self.register_user_use_case = register_user_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if "name" in body_params and "password" in body_params:
                name = http_request.body["name"]
                password = http_request.body["password"]
                cpf = http_request.body["cpf"]
                response = self.register_user_use_case.register(
                    name=name, password=password, cpf=cpf
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()

                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
