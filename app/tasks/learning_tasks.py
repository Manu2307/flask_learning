import time
from celery.utils.log import get_task_logger
from app.tasks.base_celery import cdp_app_celery
from app.mailer.learning_mailer import LearningMailer

logger = get_task_logger(__name__)


@cdp_app_celery.task(bind=True, queue='send_new_learning_email')
def send_new_learning_email(unused_arg, to_email, recipient_name, skill_name):
    try:
        logger.info('Received task - send_new_learning_email')
        learning_mailer = LearningMailer()
        learning_mailer.send_new_learning_email(to_email, recipient_name, skill_name)
    except Exception as ex:
        logger.error(ex, exc_info=True)
        raise ex
