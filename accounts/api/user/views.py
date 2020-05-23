from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .serializers import UserDetailSerializer
from question.api.serializers import QuizInlineUserSerializer
from question.models import Quiz

User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

class UserQuizAPIView(generics.ListAPIView):
    serializer_class = QuizInlineUserSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username", None)
        if username is None:
            return Quiz.objects.none()
        return Quiz.objects.filter(user__username=username)        