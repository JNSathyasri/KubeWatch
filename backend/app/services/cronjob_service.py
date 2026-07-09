from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class CronJobService:

    @staticmethod
    def list_cronjobs():

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.BatchV1Api()

        cronjobs = api.list_cron_job_for_all_namespaces()

        result = []

        for cj in cronjobs.items:

            result.append(
                {
                    "name": cj.metadata.name,
                    "namespace": cj.metadata.namespace,
                    "schedule": cj.spec.schedule,
                    "suspend": cj.spec.suspend,
                    "creation_time": cj.metadata.creation_timestamp.isoformat(),
                }
            )

        return result