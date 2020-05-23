from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from accounts.api.permissions import IsOwnerOrReadOnly, QuizRelatedQuestion

from question.models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionPostSerializer


class QuizAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def get_queryset(self):
        request = self.request
        qs = Quiz.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(name_icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuizDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class QuestionAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, QuizRelatedQuestion]
    serializer_class = QuestionPostSerializer

    def get_queryset(self, *args, **kwargs):
        quiz = self.kwargs.get("id", None)
        if quiz is None:
            return Question.objects.none()
        return Question.objects.filter(quiz__id=quiz)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        path_quiz_id = self.request.path[-12:-11]
        quiz_name = Quiz.objects.filter(id=path_quiz_id)[0]
        serializer.save(quiz=quiz_name)


# class QuestionDetialAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     serializer_class = QuestionPostSerializer
#     queryset = Question.objects.all()

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
