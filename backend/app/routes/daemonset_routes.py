from flask import Blueprint, jsonify

from app.services.daemonset_service import DaemonSetService

daemonset_bp = Blueprint("daemonsets", __name__)


@daemonset_bp.route("/daemonsets", methods=["GET"])
def get_daemonsets():

    data = DaemonSetService.list_daemonsets()

    return jsonify(
        {
            "count": len(data),
            "daemonsets": data
        }
    )