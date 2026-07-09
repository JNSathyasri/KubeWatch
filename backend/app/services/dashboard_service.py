from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class DashboardService:

    @staticmethod
    def get_summary():
        try:
            try:
                config.load_kube_config()
            except ConfigException:
                config.load_incluster_config()
        except Exception:
            return {
                "nodes": 0,
                "namespaces": 0,
                "pods": 0,
                "running_pods": 0,
                "pending_pods": 0,
                "failed_pods": 0,
                "deployments": 0,
                "services": 0,
                "daemonsets": 0,
                "statefulsets": 0,
                "jobs": 0,
                "cronjobs": 0,
            }
        core = client.CoreV1Api()
        apps = client.AppsV1Api()
        batch = client.BatchV1Api()

        nodes = core.list_node().items
        namespaces = core.list_namespace().items
        pods = core.list_pod_for_all_namespaces().items
        services = core.list_service_for_all_namespaces().items

        deployments = apps.list_deployment_for_all_namespaces().items
        daemonsets = apps.list_daemon_set_for_all_namespaces().items
        statefulsets = apps.list_stateful_set_for_all_namespaces().items

        jobs = batch.list_job_for_all_namespaces().items
        cronjobs = batch.list_cron_job_for_all_namespaces().items

        running = 0
        pending = 0
        failed = 0

        for pod in pods:

            if pod.status.phase == "Running":
                running += 1

            elif pod.status.phase == "Pending":
                pending += 1

            elif pod.status.phase == "Failed":
                failed += 1

        return {

            "nodes": len(nodes),

            "namespaces": len(namespaces),

            "pods": len(pods),

            "running_pods": running,

            "pending_pods": pending,

            "failed_pods": failed,

            "deployments": len(deployments),

            "services": len(services),

            "daemonsets": len(daemonsets),

            "statefulsets": len(statefulsets),

            "jobs": len(jobs),

            "cronjobs": len(cronjobs)

        }