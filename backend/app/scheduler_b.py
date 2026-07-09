from apscheduler.schedulers.background import BackgroundScheduler

from app.services.metric_collector import MetricCollector

scheduler = BackgroundScheduler()


def start_scheduler():

    scheduler.add_job(

        MetricCollector.collect,

        trigger="interval",

        seconds=30,

        id="metric_collector",

        replace_existing=True

    )

    scheduler.start()

    print("Metric Scheduler Started")