from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class PodMetricsService:

    @staticmethod
    def get_metrics():

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.CustomObjectsApi()

        metrics = api.list_cluster_custom_object(
            group="metrics.k8s.io",
            version="v1beta1",
            plural="pods"
        )

        result = []

        for pod in metrics["items"]:

            cpu = "0"

            memory = "0"

            for container in pod["containers"]:

                cpu = container["usage"]["cpu"]

                memory = container["usage"]["memory"]

            result.append({

                "namespace": pod["metadata"]["namespace"],

                "name": pod["metadata"]["name"],

                "cpu": cpu,

                "memory": memory

            })

        return result