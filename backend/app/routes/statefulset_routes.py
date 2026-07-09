from flask import Blueprint, jsonify

from app.services.statefulset_service import StatefulSetService

statefulset_bp = Blueprint("statefulsets", __name__)


@statefulset_bp.route("/statefulsets", methods=["GET"])
def get_statefulsets():

    data = StatefulSetService.list_statefulsets()

    return jsonify(
        {
            "count": len(data),
            "statefulsets": data
        }
    )