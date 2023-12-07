from app.repository.sql_context import SqlContext
from app.models import Learning

class LearningRepo:
    @staticmethod
    def get_learning_record(associate_id, skill_name):
        query = Learning.query.filter(
            Learning.associate_id == associate_id,
            Learning.skill_name == skill_name
        )

        return query.scalar() #returns one if exists else None


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
