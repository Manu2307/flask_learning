import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    FLASK_ENV = os.environ.get('FLASK_ENV')

    # DB Credentials
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')
    DB_DRIVER = os.environ.get('DB_DRIVER')

    SQLALCHEMY_DATABASE_URI = f'{DB_DRIVER}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_PORT = os.environ.get('REDIS_PORT')

    CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/1'
    CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/2'

    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    MAIL_USE_SSL = True if os.environ.get('MAIL_USE_SSL') == 'True' else False
    MAIL_USE_TLS = True if os.environ.get('MAIL_USE_TLS') == 'True' else False

    CLIENT_ID = os.environ.get('AUTH_CLIENT_ID')
    CLIENT_SECRET = os.environ.get('AUTH_CLIENT_SECRET')


class DevConfig(BaseConfig):
    pass
