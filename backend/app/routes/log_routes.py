from flask import Blueprint, jsonify

from app.services.log_service import LogService

log_bp = Blueprint("logs", __name__)


@log_bp.route("/logs/<namespace>/<pod>")
def logs(namespace, pod):

    return jsonify({

        "namespace": namespace,

        "pod": pod,

        "logs": LogService.get_logs(namespace, pod)

    })