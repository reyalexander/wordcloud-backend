from django.db import models
from apps.questions.models import Question

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True,verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='fecha de actualización')

