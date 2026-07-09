from apscheduler.schedulers.background import BackgroundScheduler
from app.services.metric_collector import MetricCollector

scheduler = BackgroundScheduler()


def start_scheduler():

    if scheduler.running:
        return

    scheduler.add_job(
        func=MetricCollector.collect,
        trigger="interval",
        seconds=30,
        id="metrics_collector",
        replace_existing=True,
        max_instances=1,
    )

    scheduler.start()

    print("KubeWatch Scheduler Started")