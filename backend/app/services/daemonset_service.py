from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class DaemonSetService:

    @staticmethod
    def list_daemonsets():

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.AppsV1Api()

        daemonsets = api.list_daemon_set_for_all_namespaces()

        result = []

        for ds in daemonsets.items:

            result.append(
                {
                    "name": ds.metadata.name,
                    "namespace": ds.metadata.namespace,
                    "desired": ds.status.desired_number_scheduled,
                    "ready": ds.status.number_ready,
                    "available": ds.status.number_available,
                    "creation_time": ds.metadata.creation_timestamp.isoformat(),
                }
            )

        return result