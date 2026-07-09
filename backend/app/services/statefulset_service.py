from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class StatefulSetService:

    @staticmethod
    def list_statefulsets():

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.AppsV1Api()

        statefulsets = api.list_stateful_set_for_all_namespaces()

        result = []

        for sts in statefulsets.items:

            result.append(
                {
                    "name": sts.metadata.name,
                    "namespace": sts.metadata.namespace,
                    "service_name": sts.spec.service_name,
                    "desired_replicas": sts.spec.replicas,
                    "ready_replicas": sts.status.ready_replicas or 0,
                    "creation_time": sts.metadata.creation_timestamp.isoformat(),
                }
            )

        return result