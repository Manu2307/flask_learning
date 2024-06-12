import logging
import logging.config
import time

from flasgger import Swagger
from app.logging_config import config as log_config
from flask import Flask
from app.models import DB, MIGRATE
from app.api.learning import learning_bp
from app.serializers.base_schema import marshmallow
from app.mailer import mail


swagger_template = {
    "info": {
        "title": "CDP App",
        "description": "An APP to manage the CDP's",
        "version": "0.1.1",
        "contact": {
            "name": "Manoj Kumar Andhrapu",
            "email": "manojkumar.andhrapu@senecaglobal.com"
        }
    },
}

# swagger_template = {
#     "info": {
#         "title": "CDP APP",
#         "description": "An APP to manage the CDP's",
#         "version": "0.1.1",
#         "contact": {
#             "name": "Manoj Kumar Andhrapu",
#             "email": "manojkumar.andhrapu@senecaglobal.com"
#         }
#     },
#     "components": {
#         "securitySchemes": {
#             "bearerAuth": {
#                 "type": "http",
#                 "scheme": "bearer",
#                 "bearerFormat": "JWT"
#             }
#         }
#     },
#     "security": [
#         {
#             "bearerAuth": []
#         }
#     ]
# }


def create_app(app_config):
    logging.config.dictConfig(log_config.LOGGING_CONF)
    logging.Formatter.converter = time.localtime

    flask_app = Flask(__name__, template_folder='email_templates')
    config = app_config()
    flask_app.config.from_object(config)

    # Configuring and initializing swagger
    flask_app.config['SWAGGER'] = {
        'title': 'CDP APP APIs',
        'openapi': '3.0.2',
        'uiversion': 3,
        'specs_route': '/swagger/'
    }
    unused_swagger = Swagger(flask_app, template=swagger_template)

    DB.init_app(flask_app)
    MIGRATE.init_app(flask_app, DB)
    marshmallow.init_app(flask_app)
    mail.init_app(flask_app)

    flask_app.register_blueprint(learning_bp)

    return flask_app
