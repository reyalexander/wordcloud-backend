from apps.answers.models import Answer
from apps.answers.serializers import AnswerSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend]