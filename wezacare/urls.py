from django.urls import path

from . import views

urlpatterns = [
    path('questions/', views.QuestionListAPIView.as_view(), name='question_list'),
    path('questions/create/', views.QuestionCreateAPIView.as_view(), name='question_create'),
    path('questions/<int:pk>/', views.QuestionRetrieveAPIView.as_view(), name='question_detail'),
    path('questions/<int:pk>/delete/', views.QuestionDeleteAPIView.as_view(), name='question_delete'),
    path('questions/<int:pk>/answers/create/', views.AnswerCreateAPIView.as_view(), name='answer_create'),
    path('answers/<int:pk>/', views.AnswerRetrieveAPIView.as_view(), name='answer_detail'),
    path('answers/<int:pk>/update/', views.AnswerUpdateAPIView.as_view(), name='answer_update'),
    path('answers/<int:pk>/delete/', views.AnswerDeleteAPIView.as_view(), name='answer_delete'),
]
