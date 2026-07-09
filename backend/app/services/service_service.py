from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class ServiceService:

    @staticmethod
    def list_services():

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.CoreV1Api()

        services = api.list_service_for_all_namespaces()

        result = []

        for svc in services.items:

            ports = []

            for port in svc.spec.ports:
                ports.append({
                    "port": port.port,
                    "target_port": str(port.target_port),
                    "protocol": port.protocol,
                    "node_port": port.node_port
                })

            external_ips = []

            if svc.spec.external_i_ps:
                external_ips.extend(svc.spec.external_i_ps)

            if svc.status.load_balancer.ingress:
                for ingress in svc.status.load_balancer.ingress:
                    external_ips.append(
                        ingress.ip or ingress.hostname
                    )

            result.append(
                {
                    "name": svc.metadata.name,
                    "namespace": svc.metadata.namespace,
                    "type": svc.spec.type,
                    "cluster_ip": svc.spec.cluster_ip,
                    "external_ips": external_ips,
                    "ports": ports,
                    "selector": svc.spec.selector or {},
                    "creation_time": svc.metadata.creation_timestamp.isoformat(),
                }
            )

        return result