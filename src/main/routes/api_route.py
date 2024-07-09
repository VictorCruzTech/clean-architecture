from flask import Blueprint, jsonify, request
from src.main.composer import register_user_composer
from src.main.adapter import flask_adapter


api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/users", methods=["POST"])
def register_user():
    """teste"""

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    if response.status_code < 300:
        message = {
            "Type": "users",
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
