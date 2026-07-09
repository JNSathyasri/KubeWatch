from flask import Blueprint, jsonify
from app.database.mongodb import MongoDB

verify_bp = Blueprint("verify", __name__)

@verify_bp.route("/test/history")
def history():

    db = MongoDB.connect()

    document = db["metrics_history"].find_one(
        {},
        {"_id": 0}
    )

    return jsonify(document)