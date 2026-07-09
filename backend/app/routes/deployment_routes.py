from flask import Blueprint, jsonify

from app.services.deployment_service import DeploymentService

deployment_bp = Blueprint("deployment", __name__)


@deployment_bp.route("/deployments", methods=["GET"])
def get_deployments():

    data = DeploymentService.list_deployments()

    return jsonify(
        {
            "count": len(data),
            "deployments": data
        }
    )