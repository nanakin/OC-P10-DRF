from rest_framework import permissions


class UnauthenticatedCreation(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(not request.user.is_authenticated and request.method == "POST")


class Owner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # print("has_obj_permission (owner)", request.user, obj)
        return bool(request.user
                    and request.user.is_authenticated
                    and request.user == obj)

    def has_permission(self, request, view):
        # print("has_permission (owner)")
        if view.action in ("list", "create"):
            return False
        else:
            return True
