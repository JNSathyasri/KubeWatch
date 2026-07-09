from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class PodService:

    @staticmethod
    def list_pods():

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.CoreV1Api()

        pods = api.list_pod_for_all_namespaces(watch=False)

        result = []

        for pod in pods.items:

            restart_count = sum(
                c.restart_count
                for c in (pod.status.container_statuses or [])
            )

            images = [
                c.image
                for c in pod.spec.containers
            ]

            ready = sum(
                1
                for c in (pod.status.container_statuses or [])
                if c.ready
            )

            total = len(pod.spec.containers)

            result.append(
                {
                    "name": pod.metadata.name,
                    "namespace": pod.metadata.namespace,
                    "status": pod.status.phase,
                    "node": pod.spec.node_name,
                    "pod_ip": pod.status.pod_ip,
                    "host_ip": pod.status.host_ip,
                    "images": images,
                    "restart_count": restart_count,
                    "ready": f"{ready}/{total}",
                    "creation_time": pod.metadata.creation_timestamp.isoformat(),
                }
            )

        return result