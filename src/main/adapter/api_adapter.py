from typing import Type
from sqlalchemy.exc import IntegrityError, NoResultFound
from src.main.interface import RouteInterface as Route
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """Adapter patter to Flask
    :param  - Flask Request
    :api_route  - Composite Routes
    """

    try:
        query_string = request.args.to_dict()

        if "pet_id" in query_string.keys():
            query_string["pet_id"] = int(query_string["pet_id"])

        if "user_id" in query_string.keys():
            query_string["user_id"] = int(query_string["user_id"])
    except:
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    if request.method == "GET":
        http_request = HttpRequest(header=request.headers, query=query_string)

    else:
        http_request = HttpRequest(header=request.headers, body=request.json)

    try:
        response = api_route.route(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
    except NoResultFound:
        http_error = HttpErrors.error_404()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
    except:
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
