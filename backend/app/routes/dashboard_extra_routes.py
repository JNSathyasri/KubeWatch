from flask import Blueprint, jsonify

from app.services.resource_summary_service import ResourceSummaryService
from app.services.top_pods_service import TopPodsService

dashboard_extra_bp = Blueprint("dashboard_extra", __name__)


@dashboard_extra_bp.route("/dashboard/resources")
def resources():

    return jsonify(

        ResourceSummaryService.get_resources()

    )


@dashboard_extra_bp.route("/dashboard/top-pods")
def top_pods():

    return jsonify(

        TopPodsService.get_top()

    )