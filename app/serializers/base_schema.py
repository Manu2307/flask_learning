from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()

class BaseSchema(marshmallow.Schema):
    __abstract__ = True
