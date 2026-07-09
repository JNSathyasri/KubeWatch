from flask import Blueprint, jsonify
from app.services.metric_collector import MetricCollector

test_bp = Blueprint("test", __name__)

@test_bp.route("/test/collect")
def test_collect():
    MetricCollector.collect()
    return jsonify({"message": "Metrics collected successfully"})