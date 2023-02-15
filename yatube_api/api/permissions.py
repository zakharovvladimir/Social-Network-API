"""Permissions."""
from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    """Users permission class."""

    def has_object_permission(self, request, view, obj):
        """Permission clause function."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
