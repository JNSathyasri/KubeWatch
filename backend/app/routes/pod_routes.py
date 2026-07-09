from flask import Blueprint, jsonify

from app.services.pod_service import PodService

pod_bp = Blueprint("pods", __name__)


@pod_bp.route("/pods", methods=["GET"])
def get_pods():

    pods = PodService.list_pods()

    return jsonify(
        {
            "count": len(pods),
            "pods": pods
        }
    )