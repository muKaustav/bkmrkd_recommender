from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery("worker")

app.conf.broker_url = "amqp://rabbitmq:5672"

app.autodiscover_tasks(["worker.tasks"], force=True)

if __name__ == "__main__":
    get_task_logger(__name__).info("Starting Celery worker.")
    app.start()
