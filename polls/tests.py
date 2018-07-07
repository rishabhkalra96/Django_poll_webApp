from django.test import TestCase
from django.urls import reverse
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

def create_question(questoin_text, days):
    """ Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published in the past,
    positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=questoin_text, published_date=time)


class QuestionIndeViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, display appropriate message
        """
        response = self.client.get(reverse('polls:index_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available" )
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
