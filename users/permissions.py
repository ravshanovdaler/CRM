from rest_framework.permissions import BasePermission


class HasUserPermission(BasePermission):
    def has_permission(self, request, view):
        allowed_roles = ["C", "AS", "MA"]
        user_job = request.user.job_type

        return user_job in allowed_roles
