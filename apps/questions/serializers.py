from apps.questions.models import Question
from rest_framework import serializers
from apps.answers.serializers import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['__all__']