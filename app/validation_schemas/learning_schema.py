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
        'max': 10.0,
        'meta': {
            'custom_message': {
                'minlength': 'duration id cannot be less than 0',
                'maxlength': 'duration cannot be more than 10.0'
            }
        }
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
