from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class LogService:

    @staticmethod
    def get_logs(namespace, pod):

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.CoreV1Api()

        return api.read_namespaced_pod_log(

            name=pod,

            namespace=namespace,

            tail_lines=200

        )