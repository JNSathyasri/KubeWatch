from flask import Blueprint, jsonify

from app.services.job_service import JobService

job_bp = Blueprint("jobs", __name__)


@job_bp.route("/jobs", methods=["GET"])
def get_jobs():

    data = JobService.list_jobs()

    return jsonify(
        {
            "count": len(data),
            "jobs": data
        }
    )