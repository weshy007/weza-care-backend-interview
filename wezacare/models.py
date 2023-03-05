from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TimeBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Question(TimeBaseModel):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.text
