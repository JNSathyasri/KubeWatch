from app.kubernetes.client import KubernetesClient


class ClusterService:

    @staticmethod
    def get_nodes():

        api = KubernetesClient.connect()

        result = []

        for node in api.list_node().items:

            ready = "Unknown"

            for condition in node.status.conditions:
                if condition.type == "Ready":
                    ready = condition.status

            result.append(
                {
                    "name": node.metadata.name,
                    "ready": ready,
                    "kubelet_version": node.status.node_info.kubelet_version,
                    "os": node.status.node_info.os_image,
                }
            )

        return result