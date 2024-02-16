from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.answers.serializers import AnswerSerializer
from rest_framework.response import Response

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
