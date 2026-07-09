from flask import Blueprint, jsonify

from app.services.history_service import HistoryService

history_bp = Blueprint("history", __name__)


@history_bp.route("/history")
def history():

    return jsonify(
        HistoryService.latest()
    )