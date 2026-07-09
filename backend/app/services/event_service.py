from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class EventService:

    @staticmethod
    def list_events():

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.CoreV1Api()

        events = api.list_event_for_all_namespaces()

        result = []

        for event in events.items:

            result.append(
                {
                    "type": event.type,
                    "reason": event.reason,
                    "message": event.message,
                    "namespace": event.metadata.namespace,
                    "object": event.involved_object.name,
                    "kind": event.involved_object.kind,
                    "creation_time": event.metadata.creation_timestamp.isoformat(),
                }
            )

        return result