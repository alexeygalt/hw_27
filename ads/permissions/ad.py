from rest_framework import permissions

from users.models import User


class AuthorAdminModeratorPermission(permissions.BasePermission):
    message = "Only author or admin and moderator can change this ad"

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMIN or request.user.role == User.MODERATOR:
            return True
        if obj.author == request.user:
            return True
        return False
