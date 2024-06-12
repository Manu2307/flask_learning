import jwt
import hashlib


class JwtToken:

    @staticmethod
    def create_sha256_hash(text):
        hash = hashlib.sha256()
        hash.update(text.encode())
        return hash.hexdigest()

    @staticmethod
    def validate_token(token, client_id, client_secret):
        try:
            key_text = f'{client_id}:{client_secret}'
            jwt_key = JwtToken.create_sha256_hash(key_text)
            jwt_payload = jwt.decode(token, jwt_key)
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError as e:
            print(e)
            return False

        return jwt_payload

