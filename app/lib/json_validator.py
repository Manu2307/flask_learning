from functools import wraps
from http import HTTPStatus
from flask import current_app as cdp_app

from cerberus import Validator, errors
from flask import request, jsonify



class CustomErrorHandler(errors.BasicErrorHandler):
    def __init__(self, schema):
        super().__init__()
        self.custom_schema = schema

    def _format_message(self, field, error):
        error_msg = self.custom_schema[field].get('meta', {}).get('custom_message').get(error.rule)
        if error_msg:
            return error_msg

        return super()._format_message(field, error)


def validate_json_schema(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                validator = Validator(schema, error_handler=CustomErrorHandler(schema))
                validator.allow_unknown = True
                is_valid = validator.validate(request.json)
                if not is_valid:
                    return jsonify({'status': 'error', 'data': validator.errors}), HTTPStatus.UNPROCESSABLE_ENTITY
            except Exception as ex:
                cdp_app.logger.error(str(ex))
                return jsonify({'status': 'error', 'data': 'Unexpected Error'}), HTTPStatus.INTERNAL_SERVER_ERROR

            return func(*args, **kwargs)
        return wrapper
    return decorator
