from celery.utils.log import get_task_logger
from flask import render_template
from app.mailer import Mailer, mail
from flask_mail import Message

logger = get_task_logger(__name__)

class LearningMailer(Mailer):
    def send_new_learning_email(self, to_email, recipient_name, skill_name):
        logger.info(f'Received request to send_new_learning_email to {to_email}')
        subject = 'Welcome - New Learning created'
        msg = Message(
            subject=subject,
            sender=self.sender_email,
            recipients=[to_email]
        )
        msg.html = render_template(
            'new_learning_email.html',
            name=recipient_name,
            skill_name=skill_name
        )
        mail.send(msg)
