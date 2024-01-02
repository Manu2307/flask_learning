from flask_httpauth import HTTPTokenAuth
from flask import current_app as cdp_app

token_auth = HTTPTokenAuth(scheme='bearer')

@token_auth.verify_token
def verify_token(token):
    client_id = cdp_app.config.get('CLIENT_ID')
    client_secret = cdp_app.config.get('CLIENT_SECRET')


