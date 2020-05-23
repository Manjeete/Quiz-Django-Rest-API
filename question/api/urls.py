from django.urls import path
from .views import QuizAPIView, QuizDetailAPIView, QuestionAPIView

urlpatterns = [
    path('', QuizAPIView.as_view()),
    path('<int:id>/', QuizDetailAPIView.as_view()),
    path('<int:id>/questions/', QuestionAPIView.as_view()),

]
