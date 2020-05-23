from django.urls import path
from .views import UserDetailAPIView, UserQuizAPIView

urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view()),
    path('<str:username>/quizs/', UserQuizAPIView.as_view()),

]