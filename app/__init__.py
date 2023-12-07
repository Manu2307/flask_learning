import logging
import logging.config
import time

from app.logging_config import config as log_config
from flask import Flask
from app.models import DB, MIGRATE
from app.api.learning import learning_bp
from app.serializers.base_schema import marshmallow

def create_app(app_config):
    logging.config.dictConfig(log_config.LOGGING_CONF)
    logging.Formatter.converter = time.localtime

    flask_app = Flask(__name__)
    config = app_config()
    flask_app.config.from_object(config)

    DB.init_app(flask_app)
    MIGRATE.init_app(flask_app, DB)
    marshmallow.init_app(flask_app)

    flask_app.register_blueprint(learning_bp)

    return flask_app
