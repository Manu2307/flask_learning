from flask_httpauth import HTTPTokenAuth
from flask import current_app as cdp_app
from app.lib.jwt_token_verifier import JwtToken
from flask import jsonify, g
from functools import wraps
from http import HTTPStatus

token_auth = HTTPTokenAuth(scheme='bearer')


@token_auth.error_handler
def auth_error_handler(status):
    return jsonify(
        {'status': 'error', 'data': 'Access Denied. Invalid Auth Token. Unauthorized Access' }
    ), status


@token_auth.verify_token
def verify_token(token):
    client_id = cdp_app.config.get('CLIENT_ID')
    client_secret = cdp_app.config.get('CLIENT_SECRET')
    jwt_payload = JwtToken.validate_token(token, client_id, client_secret)
    if not jwt_payload:
        return False

    g.jwt_payload = jwt_payload
    g.token = token
    return True


def authorize_admin(api_method):
    @wraps(api_method)
    @token_auth.login_required
    def wrapper(*args, **kwargs):
        if 'SuperAdmin' not in g.jwt_payload.get('roles', []):
            return jsonify(
                {
                    'status': 'error', 'message': 'Access restricted because you are not an SuperAdmin'
                }
            ), HTTPStatus.FORBIDDEN
        return api_method(*args, **kwargs)
    return wrapper

