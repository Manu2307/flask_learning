from flask import Flask
from app.models import DB, MIGRATE


def create_app(app_config):
    flask_app = Flask(__name__)
    config = app_config()
    flask_app.config.from_object(config)

    DB.init_app(flask_app)
    MIGRATE.init_app(flask_app, DB)

    return flask_app
