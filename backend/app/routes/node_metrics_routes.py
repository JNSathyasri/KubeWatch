from flask import Blueprint, jsonify

from app.services.node_metrics_service import NodeMetricsService

node_metrics_bp = Blueprint("node_metrics", __name__)


@node_metrics_bp.route("/metrics/nodes", methods=["GET"])
def get_node_metrics():

    data = NodeMetricsService.get_node_metrics()

    return jsonify(
        {
            "count": len(data),
            "nodes": data
        }
    )