from flask import Blueprint, jsonify

from app.services.cronjob_service import CronJobService

cronjob_bp = Blueprint("cronjobs", __name__)


@cronjob_bp.route("/cronjobs", methods=["GET"])
def get_cronjobs():

    data = CronJobService.list_cronjobs()

    return jsonify(
        {
            "count": len(data),
            "cronjobs": data
        }
    )