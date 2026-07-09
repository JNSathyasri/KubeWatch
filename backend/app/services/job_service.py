from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class JobService:

    @staticmethod
    def list_jobs():

        try:
            config.load_kube_config()
        except ConfigException:
            config.load_incluster_config()

        api = client.BatchV1Api()

        jobs = api.list_job_for_all_namespaces()

        result = []

        for job in jobs.items:

            result.append(
                {
                    "name": job.metadata.name,
                    "namespace": job.metadata.namespace,
                    "completions": job.spec.completions,
                    "succeeded": job.status.succeeded or 0,
                    "failed": job.status.failed or 0,
                    "active": job.status.active or 0,
                    "creation_time": job.metadata.creation_timestamp.isoformat(),
                }
            )

        return result