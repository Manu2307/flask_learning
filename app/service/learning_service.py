from app.repository import LearningRepo
from app.lib.custom_exceptions import DuplicateRecordException, CreateRecordFailed
from flask import current_app as cdp_app
from app.schema.learning_schema import CreateLearningRequest, CreateLearningResponse


class LearningService:
    @staticmethod
    def create_learning(learning_data: CreateLearningRequest) -> CreateLearningResponse:
        cdp_app.logger.info('Called Learning Service - create_learning')
        try:
            learning = LearningRepo.create_learning(learning_data)
        except Exception as ex:
            cdp_app.logger.error(f'DB Record creation failed | {ex}')
            raise CreateRecordFailed

        cdp_app.logger.info('Service call create_learning_record created successfully')

        return learning

    @staticmethod
    def create_learning_record(learning_data):
        cdp_app.logger.info('Called Learning Service - create_learning_record')
        learning = LearningRepo.get_learning_record(
            learning_data["associate_id"], learning_data["skill_name"])
        if learning:
            msg = (f'Duplicate Record for associate_id {learning_data["associate_id"]}'
                   f' and {learning_data["skill_name"]}')
            cdp_app.logger.error(msg)
            raise DuplicateRecordException(msg)

        try:
            learning = LearningRepo.create_learning_record(learning_data)
        except Exception as ex:
            cdp_app.logger.error(f'DB Record creation failed | {ex}')
            raise CreateRecordFailed

        cdp_app.logger.info('Service call create_learning_record created successfully')

        return learning
