from flask import Blueprint, jsonify

from app.services.node_metrics_service import NodeMetricsService
from app.services.pod_metrics_service import PodMetricsService

metrics_bp = Blueprint("metrics", __name__)


@metrics_bp.route("/metrics/nodes")
def node_metrics():

    return jsonify({

        "count": len(NodeMetricsService.get_metrics()),

        "nodes": NodeMetricsService.get_metrics()

    })


@metrics_bp.route("/metrics/pods")
def pod_metrics():

    return jsonify({

        "count": len(PodMetricsService.get_metrics()),

        "pods": PodMetricsService.get_metrics()

    })