from flask import Blueprint, jsonify, request
from src.infra.entities.pet import Pet
from src.main.composer import (
    register_user_composer,
    register_pet_composer,
    # find_user_composer,
    find_pet_composer,
)
from src.main.adapter import flask_adapter
from src.main.composer.find_user_composite import find_user_composer


api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """teste"""

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    if response.status_code < 300:
        message = {
            "type": "users",
            "id": response.body.id,
            "attributes": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets", methods=["POST"])
def register_pets():
    """teste"""

    message = {}
    response = flask_adapter(request=request, api_route=register_pet_composer())

    if response.status_code < 300:
        message = {
            "type": "pets",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
                "specie": response.body.specie,
                "age": response.body.age,
            },
            "relationships": {"owner": {"type": "users", "id": response.body.user_id}},
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/pets", methods=["GET"])
def finder_pets():
    """teste"""

    message = {}
    response = flask_adapter(request=request, api_route=find_pet_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            if isinstance(element, Pet):
                message.append(
                    {
                        "type": "pets",
                        "id": element.id,
                        "attributes": {
                            "name": element.name,
                            "specie": element.specie.value,
                            "age": element.age,
                        },
                        "relationships": {
                            "owner": {"type": "users", "id": element.user_id}
                        },
                    }
                )
            else:
                if len(element) > 0:
                    for item in element:
                        message.append(
                            {
                                "type": "pets",
                                "id": item.id,
                                "attributes": {
                                    "name": item.name,
                                    "specie": item.specie.value,
                                    "age": item.age,
                                },
                                "relationships": {
                                    "owner": {"type": "users", "id": item.user_id}
                                },
                            }
                        )

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {
                "error": {
                    "status_code": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )


@api_routes_bp.route("/api/users", methods=["GET"])
def finder_users():
    """teste"""

    message = {}
    response = flask_adapter(request=request, api_route=find_user_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "users",
                    "id": element.id,
                    "attributes": {"name": element.name},
                }
            )

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {
                "error": {
                    "status_code": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )
