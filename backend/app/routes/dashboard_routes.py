from flask import Blueprint, jsonify

from app.services.dashboard_service import DashboardService

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():

    return jsonify(
        DashboardService.get_summary()
    )