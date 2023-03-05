from django.shortcuts import render
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from .models import Question, Answer
from .serilaizers import QuestionSerializer, AnswerSerializer, AnswerUpdateSerializer


# Create your views here.
class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDeleteAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        question = get_object_or_404(Question, id=self.kwargs['pk'])
        serializer.save(author=self.request.user, question=question)


class AnswerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerUpdateAPIView(generics.UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class AnswerDeleteAPIView(generics.DestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
