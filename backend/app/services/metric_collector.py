from datetime import datetime

from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException

from app.database.mongodb import MongoDB

metrics_collection = MongoDB.metrics_collection()


class MetricCollector:

    @staticmethod
    def collect():

        try:
            try:
                config.load_kube_config()
            except ConfigException:
                config.load_incluster_config()

            core = client.CoreV1Api()
            custom = client.CustomObjectsApi()

            pods = core.list_pod_for_all_namespaces().items

            metrics = custom.list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural="nodes",
            )

            cpu_total = 0
            memory_total = 0

            for node in metrics["items"]:

                cpu = node["usage"]["cpu"]
                memory = node["usage"]["memory"]

                if cpu.endswith("n"):
                    cpu_total += int(cpu[:-1]) / 1_000_000

                elif cpu.endswith("m"):
                    cpu_total += float(cpu[:-1])

                if memory.endswith("Ki"):
                    memory_total += float(memory[:-2]) / 1024

                elif memory.endswith("Mi"):
                    memory_total += float(memory[:-2])

            metrics_collection.insert_one({

                "timestamp": datetime.utcnow(),

                "cpu_usage": round(cpu_total, 2),

                "memory_usage": round(memory_total, 2),

                "pods": len(pods)

            })

        except Exception as e:
            print(f"Metric collection skipped: {e}")