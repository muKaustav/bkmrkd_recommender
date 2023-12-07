from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(bind=True, name="ml_task")
def ml_task(self, book_id):
    try:
        logger = get_task_logger(self.name)
        logger.info("Starting ML task.")

        try:
            logger.info("ML task successful.")
            return {"status": "success", "book_id": book_id}
        except Exception as e:
            logger.error("ML task failed.")
            return {"status": "error", "book_id": book_id}

    except Exception as e:
        logger.error("ML task failed.")
        return {"status": "error", "book_id": book_id}
