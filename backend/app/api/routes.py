from flask import Blueprint, jsonify
from app.services.cluster_service import ClusterService
api_bp = Blueprint("api", __name__)


@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify(
        {
            "success": True,
            "message": "KubeWatch Backend Running",
            "version": "1.0.0",
        }
    )


@api_bp.route("/info", methods=["GET"])
def info():
    return jsonify(
        {
            "application": "KubeWatch",
            "framework": "Flask",
            "language": "Python",
        }
    )

@api_bp.route("/nodes", methods=["GET"])
def nodes():
    return ClusterService.get_nodes()