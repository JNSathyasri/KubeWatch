from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class NodeMetricsService:

    @staticmethod
    def get_node_metrics():

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.CustomObjectsApi()

        metrics = api.list_cluster_custom_object(
            group="metrics.k8s.io",
            version="v1beta1",
            plural="nodes"
        )

        result = []

        for node in metrics["items"]:

            result.append(
                {
                    "name": node["metadata"]["name"],
                    "cpu": node["usage"]["cpu"],
                    "memory": node["usage"]["memory"]
                }
            )

        return result