from django.urls import path
from .views import QuizAPIView, QuizDetailAPIView, QuestionAPIView

urlpatterns = [
    path('', QuizAPIView.as_view()),
    path('<int:id>/', QuizDetailAPIView.as_view()),
    path('<int:id>/questions/', QuestionAPIView.as_view()),

    # path('question/', QuestionAPIView.as_view()),
    # path('question/<int:id>/', QuestionDetialAPIView.as_view()),


]
