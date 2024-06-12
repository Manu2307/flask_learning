from flask_mail import Mail
from flask import current_app

mail = Mail()


class Mailer:
    def __init__(self):
        self.email = mail
        self.msg = None
        self.env = current_app.config.get('ENV', 'dev')
        self.sender_email = current_app.config.get('MAIL_DEFAULT_SENDER')
