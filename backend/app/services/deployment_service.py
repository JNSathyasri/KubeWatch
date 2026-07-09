from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class DeploymentService:

    @staticmethod
    def list_deployments():

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.AppsV1Api()

        deployments = api.list_deployment_for_all_namespaces()

        result = []

        for dep in deployments.items:

            status = dep.status

            spec = dep.spec

            result.append(
                {
                    "name": dep.metadata.name,
                    "namespace": dep.metadata.namespace,
                    "desired_replicas": spec.replicas,
                    "ready_replicas": status.ready_replicas or 0,
                    "available_replicas": status.available_replicas or 0,
                    "updated_replicas": status.updated_replicas or 0,
                    "strategy": spec.strategy.type,
                    "creation_time": dep.metadata.creation_timestamp.isoformat(),
                }
            )

        return result