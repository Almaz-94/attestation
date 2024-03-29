from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """ Проверка пользователя на активность """
    def has_object_permission(self, request, view, obj):
        if request.user.is_active:
            return True
        return False
