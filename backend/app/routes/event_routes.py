from flask import Blueprint, jsonify

from app.services.event_service import EventService

event_bp = Blueprint("events", __name__)


@event_bp.route("/events", methods=["GET"])
def get_events():

    data = EventService.list_events()

    return jsonify(
        {
            "count": len(data),
            "events": data
        }
    )