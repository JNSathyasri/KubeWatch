from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class KubernetesClient:

    api = None

    @classmethod
    def connect(cls):

        if cls.api is not None:
            return cls.api

        try:
            # Local development (Windows / Docker with mounted kubeconfig)
            config.load_kube_config()

        except ConfigException:
            # Running inside a Kubernetes cluster
            config.load_incluster_config()

        cls.api = client.CoreV1Api()

        return cls.api