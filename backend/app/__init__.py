from flask import Flask
from flask_cors import CORS
from app.middleware.error_handler import register_error_handlers
from app.config.settings import Config
from app.api.routes import api_bp
from app.database.mongodb import MongoDB
from app.utils.logger import setup_logger
from app.kubernetes.client import KubernetesClient
from app.routes.namespace_routes import namespace_bp
from app.routes.pod_routes import pod_bp
from app.routes.deployment_routes import deployment_bp
from app.routes.service_routes import service_bp
from app.routes.statefulset_routes import statefulset_bp
from app.routes.daemonset_routes import daemonset_bp
from app.routes.job_routes import job_bp
from app.routes.cronjob_routes import cronjob_bp
from app.routes.event_routes import event_bp
from app.routes.dashboard_routes import dashboard_bp
from app.routes.node_metrics_routes import node_metrics_bp
from app.routes.metrics_routes import metrics_bp
from app.routes.log_routes import log_bp
from app.routes.dashboard_extra_routes import dashboard_extra_bp
from app.routes.history_routes import history_bp
from app.routes.test_routes import test_bp
from app.routes.verify_routes import verify_bp
from app.scheduler import start_scheduler

def create_app():
    app = Flask(__name__)
    setup_logger()

    app.logger.info("KubeWatch Backend Started")
    app.config.from_object(Config)
    register_error_handlers(app)
    CORS(app)
    MongoDB.connect()
    app.logger.info("MongoDB Connected Successfully")
    try:
        KubernetesClient.connect()
        app.logger.info("Connected to Kubernetes Cluster")
    except Exception as e:
        app.logger.warning(f"Kubernetes not available: {e}")
    start_scheduler()
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(pod_bp, url_prefix="/api")
    app.register_blueprint(namespace_bp, url_prefix="/api")
    app.register_blueprint(deployment_bp, url_prefix="/api")
    app.register_blueprint(service_bp, url_prefix="/api")
    app.register_blueprint(statefulset_bp, url_prefix="/api")
    app.register_blueprint(daemonset_bp, url_prefix="/api")
    app.register_blueprint(job_bp, url_prefix="/api")
    app.register_blueprint(cronjob_bp, url_prefix="/api")
    app.register_blueprint(dashboard_bp, url_prefix="/api")
    app.register_blueprint(node_metrics_bp, url_prefix="/api")
    app.register_blueprint(metrics_bp, url_prefix="/api")
    app.register_blueprint(log_bp, url_prefix="/api")
    app.register_blueprint(dashboard_extra_bp, url_prefix="/api")
    app.register_blueprint(history_bp, url_prefix="/api")
    app.register_blueprint(test_bp, url_prefix="/api")
    app.register_blueprint(verify_bp, url_prefix="/api")

    return app