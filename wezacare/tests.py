from django.test import TestCase, Client
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Question, Answer
from .serilaizers import QuestionSerializer


class QuestionModelTestCase(TestCase):
    def setUp(self):
        self.question = Question.objects.create(title='Test Question', text='Test Body', author=User.objects.create(username='testuser'))

    def test_question_title(self):
        self.assertEqual(str(self.question), 'Test Question')


class QuestionListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('question_list')
        self.question = Question.objects.create(title='Test Question', text='Test Body', author=User.objects.create(username='testuser'))

    def test_question_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = QuestionSerializer(Question.objects.all(), many=True).data
        self.assertEqual(response.data, serializer_data)


class QuestionCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('question_create')
        self.user = User.objects.create(username='testuser', password='password')

    def test_question_create_view(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Test Question', 'text': 'Test Body'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(Question.objects.get().title, 'Test Question')


class QuestionRetrieveViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.question = Question.objects.create(title='Test Question', text='Test Body', author=User.objects.create(username='testuser'))
        self.url = reverse('question_detail', kwargs={'pk': self.question.id})

    def test_question_retrieve_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = QuestionSerializer(self.question).data
        self.assertEqual(response.data, serializer_data)


class QuestionDeleteViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.question = Question.objects.create(title='Test Question', text='Test Body', author=User.objects.create(username='testuser'))
        self.url = reverse('question_delete', kwargs={'pk': self.question.id})
        self.user = User.objects.create(username='testuser1', password='password')

    def test_question_delete_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Question.objects.count(), 1)


class AnswerCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.question = Question.objects.create(title='Test Question', text='Test Body', author=User.objects.create(username='testuser'))
        self.url = reverse('answer_create', kwargs={'pk': self.question.id})
        self.user = User.objects.create(username='testuser2', password='password')

    def test_answer_create_view(self):
        self.client.force_authenticate(user=self.user)
        data = {'text': 'Test Answer Body'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.count(), 1)
