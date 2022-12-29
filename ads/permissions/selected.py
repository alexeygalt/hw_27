from rest_framework import permissions


class SelectedByOwner(permissions.BasePermission):
    message = 'Only user who created the selection can change and delete it'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False

