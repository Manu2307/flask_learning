from typing import List
from uuid import uuid4

from flask import current_app as cdp_app
from app.models import Learning
from app.repository import LearningRepo
from app.lib.custom_exceptions import DuplicateRecordException, CreateRecordFailed
from app.schema.learning_schema import CreateLearningRequest, CreateLearningResponse, EditLearningRequest


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
    def get_all_learnings() -> List[Learning]:
        cdp_app.logger.info('Called learning service - get_all_learnings')
        try:
            learnings = LearningRepo.get_all_learnings()
        except Exception as ex:
            error_msg = 'Unable to get learnings'
            cdp_app.logger.error(f"{error_msg} - {ex}", exc_info=True)

        return learnings

    @staticmethod
    def get_learning_by_id(learning_id) -> CreateLearningResponse:
        cdp_app.logger.info('Called learning service - get_learning_by_id')
        try:
            learning = LearningRepo.get_learning_by_id(learning_id)
        except Exception as ex:
            error_msg = "Unexpected error occured"
            cdp_app.logger.info(f'{error_msg} - {ex}', exc_info=True)

        return learning

    @staticmethod
    def update_learning(learning_id: uuid4, learning_data: EditLearningRequest) -> CreateLearningResponse:
        cdp_app.logger.info('Called Service - update_learning')
        learning_record = LearningRepo.get_learning_by_id(learning_id)

        if not learning_record:
            cdp_app.logger.info(f"No record exists with Learning Id - {learning_id}")

        try:
            response = LearningRepo.update_learning(learning_record, learning_data)
        except Exception as ex:
            error_msg = f'Unable to update Learning record - {learning_record.id}'
            cdp_app.logger.error(f'{error_msg} - {ex}', exc_info=True)

        return response

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
