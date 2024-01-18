import logging
from app import create_app
from config import DevConfig
from flask import request
import json

cdp_app = create_app(DevConfig)
req_logger = logging.getLogger('RequestLogger')

@cdp_app.before_request
def cdp_app_before_request():
    log_params = {
        'ip': request.headers.get('X-Forwarded-For', request.remote_addr),
        'device_type': request.headers.get('User-Agent'),
        'method': request.method,
        'path': request.path,
    }
    if request.args:
        log_params['args'] = request.args
    if request.is_json:
        log_params['json'] = request.is_json

    req_logger.info(json.dumps(log_params))


@cdp_app.route("/welcome", methods=["GET"])
def welcome_method():
    return "Hello flask learners"


if __name__ == "__main__":
    cdp_app.run()
