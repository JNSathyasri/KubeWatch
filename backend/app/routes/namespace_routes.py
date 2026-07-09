from flask import Blueprint, jsonify

from app.services.namespace_service import NamespaceService

namespace_bp = Blueprint("namespace", __name__)


@namespace_bp.route("/namespaces", methods=["GET"])
def get_namespaces():

    data = NamespaceService.list_namespaces()

    return jsonify(
        {
            "count": len(data),
            "namespaces": data
        }
    )