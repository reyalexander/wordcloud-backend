from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]