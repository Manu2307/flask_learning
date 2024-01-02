from flask import Blueprint
from flask import request
from http import HTTPStatus
from flask import jsonify
from app.service import LearningService
from app.lib.custom_exceptions import DuplicateRecordException, CreateRecordFailed
from flask import current_app as cdp_app
from app.schema import CREATE_lEARNING_SCHEMA, UPDATE_lEARNING_SCHEMA
from app.lib.json_validator import validate_json_schema
from app.tasks import send_new_learning_email
from flask_dantic import pydantic_validator, serialize

from app.schema import CreateLearningRequest, CreateLearningResponse

learning_bp = Blueprint('learning_bp', __name__)


@learning_bp.route('/learning/create', methods=['POST'])
@pydantic_validator(body=CreateLearningRequest)
def create_learning():
    cdp_app.logger.info('API called - /learning/create')
    response = LearningService.create_learning(request.body_model)
    data = serialize(response, CreateLearningResponse, json_dump=False)

    return {"status": "success", "data": data}, HTTPStatus.CREATED


# @learning_bp.route('/learning/create', methods=['POST'])
# @validate_json_schema(CREATE_lEARNING_SCHEMA)
# def create_learning():
#     cdp_app.logger.info('API called - /learning/create')
#     learning_data = request.json
#
#     try:
#         learning = LearningService.create_learning_record(learning_data)
#         learning_schema = LearningSchema()
#         learning_serializer = learning_schema.dump(learning)
#
#     except DuplicateRecordException as ex:
#         return jsonify({'status': 'error', 'data': str(ex)}), HTTPStatus.BAD_REQUEST
#
#     except CreateRecordFailed as ex:
#         return jsonify({'status': 'error', 'data': str(ex)}), HTTPStatus.INTERNAL_SERVER_ERROR
#
#     except Exception as ex:
#         cdp_app.logger.error(str(ex))
#         return jsonify({'status': 'error', 'data': 'Unexpected error'}), HTTPStatus.INTERNAL_SERVER_ERROR
#     recipient_name = ' '.join(map(lambda item: item.capitalize(), learning_data['email'].split('@')[0].split('.')))
#     send_new_learning_email.s(learning_data['email'], recipient_name, learning_data['skill_name']).apply_async()
#     return jsonify({'status': 'success', 'data': learning_serializer}), HTTPStatus.CREATED
#
#
# @learning_bp.route('/learning/update', methods=['POST'])
# @validate_json_schema(UPDATE_lEARNING_SCHEMA)
# def update_learning():
#     cdp_app.logger.info('API called - /learning/create')
#     learning_data = request.json
#     try:
#         learning = LearningService.create_learning_record(learning_data)
#         learning_schema = LearningSchema()
#         learning_serializer = learning_schema.dump(learning)
#
#     except DuplicateRecordException as ex:
#         return jsonify({'status': 'error', 'data': str(ex)}), HTTPStatus.BAD_REQUEST
#
#     except CreateRecordFailed as ex:
#         return jsonify({'status': 'error', 'data': str(ex)}), HTTPStatus.INTERNAL_SERVER_ERROR
#
#     except Exception as ex:
#         cdp_app.logger.error(str(ex))
#         return jsonify({'status': 'error', 'data': 'Unexpected error'}), HTTPStatus.INTERNAL_SERVER_ERROR
#
#     return jsonify({'status': 'success', 'data': learning_serializer}), HTTPStatus.CREATED
