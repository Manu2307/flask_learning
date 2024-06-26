from uuid import uuid4
from datetime import datetime
import json

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

DB = SQLAlchemy()
MIGRATE = Migrate()


class BaseModel(DB.Model):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    def set_attributes(self, values):
        if not isinstance(values, dict):
            values = json.loads(values.json())
        for key, value in values.items():
            if hasattr(self, key) and (
                    (isinstance(value, str) and value)
                    or (isinstance(value, (bool, int, float, list)))
            ):
                setattr(self, key, value)


class AuditMixin(DB.Model):
    __abstract__ = True

    created_on = Column(DateTime(timezone=True), default=datetime.now)
    modified_on = Column(DateTime(timezone=True), default=datetime.now, onupdate=True)
