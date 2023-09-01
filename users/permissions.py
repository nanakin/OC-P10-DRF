from rest_framework import permissions


class UnauthenticatedCreation(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(not request.user.is_authenticated and request.method == "POST")


class Owner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user
                    and request.user.is_authenticated
                    and request.user == obj)
