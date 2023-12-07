from app.serializers.base_schema import BaseSchema


class LearningSchema(BaseSchema):
    class Meta:
        fields = (
            'associate_id', 'email', 'skill_name', 'status'
        )
