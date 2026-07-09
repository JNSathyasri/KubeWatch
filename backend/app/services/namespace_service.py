from app.extensions.kubernetes import get_core_api


class NamespaceService:
    @staticmethod
    def list_namespaces():
        api = get_core_api()

        namespaces = api.list_namespace()

        result = []

        for ns in namespaces.items:
            result.append({
                "name": ns.metadata.name,
                "status": ns.status.phase,
                "created_at": ns.metadata.creation_timestamp.isoformat(),
                "labels": ns.metadata.labels or {}
            })

        return result