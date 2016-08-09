from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    anwser_text = models.CharField(max_length=200)
    session = models.CharField(max_length=200, default='')
