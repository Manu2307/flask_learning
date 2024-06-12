from pydantic import Field
from typing import Optional
from datetime import datetime
from pydantic import UUID4

from app.lib.constants import UUID_REGEX
from app.schema.base_schema import BaseSchema


class CreateLearningRequest(BaseSchema):
    associate_id: str
    email: str
    skill_name: str
    duration: float
    learning_resource: str
    resource_link: str
    start_datetime: datetime
    end_datetime: datetime
    status: str


class CreateLearningResponse(BaseSchema):
    id: Optional[UUID4]
    associate_id: UUID4
    email: str
    skill_name: str
    duration: float
    learning_resource: str
    resource_link: str
    start_datetime: datetime
    end_datetime: datetime
    status: str


class BaseLearningRequest(BaseSchema):
    learning_id: str = Field(..., regex=UUID_REGEX)


class EditLearningRequest(BaseSchema):
    associate_id: Optional[str]
    email: Optional[str]
    skill_name: Optional[str]
    duration: Optional[float]
    learning_resource: Optional[str]
    resource_link: Optional[str]
    start_datetime: Optional[datetime]
    end_datetime: Optional[datetime]
    status: Optional[str]


CREATE_lEARNING_SCHEMA = {
    'associate_id' : {
        'type': 'string',
        'regex': '[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',
        'required': True,
        'meta': {
            'custom_message': {
                'regex': 'Associate Id is not in valid format'
            }
        }
    },
    'email': {
        'type': 'string',
        'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$',
        'required': True,
        'minlength': 3,
        'maxlength': 255,
        'meta': {
            'custom_message': {
                'regex': 'Email id is not in valid format',
                'minlength': 'Email id cannot be less than 3 characters',
                'maxlength': 'Email id cannot be greater than 255 characters'
            }
        }
    },
    'skill_name': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 255,
        'required': True,
        'meta': {
            'custom_message': {
                'minlength': 'Skill Name id cannot be less than 3 characters',
                'maxlength': 'Skill Name cannot be greater than 255 characters'
            }
        }
    },
    'duration': {
        'type': 'float',
        'required': True,
        'min': 0.0,
        'max': 10.0
    }
}

UPDATE_lEARNING_SCHEMA = {
    'associate_id' : {
        'type': 'string',
        'regex': '[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}',
        'required': True,
        'meta': {
            'custom_message': {
                'regex': 'Associate Id is not in valid format'
            }
        }
    },
    'email': {
        'type': 'string',
        'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$',
        'required': True,
        'minlength': 3,
        'maxlength': 255,
        'meta': {
            'custom_message': {
                'regex': 'Email id is not in valid format',
                'minlength': 'Email id cannot be less than 3 characters',
                'maxlength': 'Email id cannot be greater than 255 characters'
            }
        }
    },
    'skill_name': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 255,
        'required': True,
        'meta': {
            'custom_message': {
                'minlength': 'Skill Name id cannot be less than 3 characters',
                'maxlength': 'Skill Name cannot be greater than 255 characters'
            }
        }
    },
    'duration': {
        'type': 'float',
        'required': True,
        'min': 0.0,
        'max': 10.0,
        'meta': {
            'custom_message': {
                'minlength': 'duration id cannot be less than 0',
                'maxlength': 'duration cannot be more than 10.0'
            }
        }
    }
}
