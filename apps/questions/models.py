from django.db import models

class Question(models.Model):
    text_question = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True,verbose_name='fecha de creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='fecha de actualización')

