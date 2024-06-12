from functools import wraps
from http import HTTPStatus

from flask import current_app as cdp_app
from app.lib.constants import DEFAULT_ERROR_MESSAGE
from app.lib.custom_exceptions import (DBRecordNotFoundException)


def error_handler(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

        except DBRecordNotFoundException as ex:
            return {'status': "error", "message": str(ex)}, HTTPStatus.BAD_REQUEST

        except Exception as ex:
            import traceback
            traceback.print_exc()
            cdp_app.logger.error(str(ex))
            return {'status': 'error', 'message': DEFAULT_ERROR_MESSAGE}, HTTPStatus.INTERNAL_SERVER_ERROR

        return result

    return inner
