from django.shortcuts import render
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from .models import Question, Answer
from .serilaizers import QuestionSerializer, AnswerSerializer, AnswerUpdateSerializer

# Create your views here.
