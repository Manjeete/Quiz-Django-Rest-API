from rest_framework import serializers
from django.contrib.auth import get_user_model
from question.api.serializers import QuizInlineUserSerializer

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    quizs = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'uri', 'quizs']

    def get_uri(self, obj):
        return "api/users/{id}".format(id=obj.id)    

    def get_quizs(self, obj):
        qs = obj.quiz_set.all()
        return QuizInlineUserSerializer(qs, many=True).data