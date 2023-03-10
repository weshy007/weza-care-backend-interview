from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    """
    The author field in the serializers is a read - only field that is automatically
    populated with the username of the user who created the question or answer
    """

    class Meta:
        model = Answer
        fields = "__all__"


class AnswerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['text']
