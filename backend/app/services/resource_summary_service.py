from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class ResourceSummaryService:

    @staticmethod
    def get_resources():
        try:
            try:
                config.load_kube_config()
            except ConfigException:
                config.load_incluster_config()
        except Exception:
            return {
                "total_nodes": 0,
                "ready_nodes": 0,
                "total_pods": 0,
                "cpu_usage": 0,
                "cpu_unit": "mCPU",
                "memory_usage": 0,
                "memory_unit": "MiB"
            }
        core = client.CoreV1Api()
        custom = client.CustomObjectsApi()

        nodes = core.list_node().items
        pods = core.list_pod_for_all_namespaces().items

        ready = 0

        for node in nodes:

            if any(
                c.type == "Ready" and c.status == "True"
                for c in node.status.conditions
            ):
                ready += 1

        cpu_total = 0
        memory_total = 0

        try:

            metrics = custom.list_cluster_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                plural="nodes",
            )

            for node in metrics["items"]:

                cpu = node["usage"]["cpu"]
                memory = node["usage"]["memory"]

                # CPU comes as nanocores (e.g. 299362266n)
                if cpu.endswith("n"):
                    cpu_total += int(cpu[:-1]) / 1_000_000

                elif cpu.endswith("u"):
                    cpu_total += int(cpu[:-1]) / 1000

                elif cpu.endswith("m"):
                    cpu_total += float(cpu[:-1])

                else:
                    cpu_total += float(cpu) * 1000

                # Memory conversions
                if memory.endswith("Ki"):
                    memory_total += float(memory[:-2]) / 1024

                elif memory.endswith("Mi"):
                    memory_total += float(memory[:-2])

                elif memory.endswith("Gi"):
                    memory_total += float(memory[:-2]) * 1024

        except Exception as e:

            print("Metrics API Error:", e)

        return {

            "total_nodes": len(nodes),

            "ready_nodes": ready,

            "total_pods": len(pods),

            "cpu_usage": round(cpu_total, 2),

            "cpu_unit": "mCPU",

            "memory_usage": round(memory_total, 2),

            "memory_unit": "MiB"

        }