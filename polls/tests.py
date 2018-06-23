from django.test import TestCase

import datetime
from django.utils import timezone
from .models import Question


class QuestionModelTests(TestCase):
    def test_published_recently_with_future_question(self):
        """
        published_recently() will return false for dates of the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(published_date=time)
        self.assertIs(future_question.published_recently(), False)

    def test_published_recently_with_old_question(self):
        """
        published_recently() will return false for question whose
        published_date is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(seconds=1, days=1)
        old_question = Question(published_date=time)
        self.assertIs(old_question.published_recently(), False)

    def test_published_recently_with_recent_question(self):
        """
        published_recently() will return true for dates within last day
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(published_date=time)
        self.assertIs(recent_question.published_recently(), True)
