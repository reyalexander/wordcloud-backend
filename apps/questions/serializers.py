from apps.questions.models import Question
from rest_framework import serializers
from apps.answers.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','text_answer']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'text_question', 'created', 'updated', 'answers']