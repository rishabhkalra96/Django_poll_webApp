import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=250)
    published_date = models.DateTimeField('date_published_on')

    def __str__(self):
        return self.question_text

    def published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

