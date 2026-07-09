from flask import Blueprint, jsonify

from app.services.service_service import ServiceService

service_bp = Blueprint("services", __name__)


@service_bp.route("/services", methods=["GET"])
def get_services():

    data = ServiceService.list_services()

    return jsonify(
        {
            "count": len(data),
            "services": data
        }
    )