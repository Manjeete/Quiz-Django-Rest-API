from rest_framework import permissions
from question.models import Quiz
from django.contrib.auth import get_user_model
import re

User = get_user_model()


class BlacklistPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted


class AnonPermissionOnly(permissions.BasePermission):
    message = 'You are already authenticated. Please logout to try again !'
    """
    Non aauthenticated user only !
    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class QuizRelatedQuestion(permissions.BasePermission):
    message = 'You are not owner of this quiz!'
    """
    Non aauthenticated user only !
    """

    def has_permission(self, request, view):
        path_id = re.search(r"/.*/(.*)/.*/", request.path)
        path_quiz_id = path_id.group(1)
        user = User.objects.filter(quiz__id=path_quiz_id)[0]
        print(user)
        print(request.user)
        return user == request.user


# class QuizRelatedSingleQuestion(permissions.BasePermission):
#     message = 'You are not owner of this quiz!'
#     """
#     Non aauthenticated user only !
#     """

#     def has_permission(self, request, view):
#         path_quiz_id = request.path[-12:-11]
#         user = User.objects.filter(quiz__id=path_quiz_id)[0]
#         return user == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
