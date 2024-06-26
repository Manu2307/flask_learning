from typing import List

from sqlalchemy import delete
from app.repository.sql_context import SqlContext
from app.models import Learning
from app.schema import CreateLearningRequest, CreateLearningResponse, EditLearningRequest


class LearningRepo:
    @staticmethod
    def get_all_learnings() -> List[Learning]:
        query = Learning.query.all()

        return query

    @staticmethod
    def get_learning_by_id(learning_id) -> Learning:
        query = Learning.query.filter(Learning.id == learning_id).one_or_none()

        return query

    @staticmethod
    def update_learning(learning_record: Learning,
                        learning_data: EditLearningRequest) -> CreateLearningResponse:
        learning_record.set_attributes(learning_data)
        with SqlContext() as sql_context:
            sql_context.session.add(learning_record)

        return learning_record



    @staticmethod
    def get_learning_record(associate_id, skill_name):
        query = Learning.query.filter(
            Learning.associate_id == associate_id,
            Learning.skill_name == skill_name
        )

        return query.scalar() #returns one if exists else None

    @staticmethod
    def create_learning(learning_data: CreateLearningRequest) -> CreateLearningResponse:
        learning = Learning()
        learning.set_attributes(learning_data)

        with SqlContext() as sql_context:
            sql_context.session.add(learning)

        return learning

    @staticmethod
    def delete_learning(learning_record):
        with SqlContext() as sql_context:
            sql_context.session.delete(learning_record)
        message = f"{learning_record.skill_name} - deleted successfully."
        return message

    @staticmethod
    def create_learning_record(learning_data):
        learning = Learning()
        learning.associate_id = learning_data['associate_id']
        learning.email = learning_data['email']
        learning.skill_name = learning_data['skill_name']
        learning.learning_resource = learning_data['learning_resource']
        learning.resource_link = learning_data['resource_link']
        learning.duration = learning_data['duration']
        learning.start_datetime = learning_data['start_datetime']
        learning.end_datetime = learning_data['end_datetime']
        learning.status = learning_data['status']

        with SqlContext() as sql_context:
            sql_context.session.add(learning)

        return learning
