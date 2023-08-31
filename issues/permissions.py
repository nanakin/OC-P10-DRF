from rest_framework.permissions import BasePermission, SAFE_METHODS


class CreationOK(BasePermission):

    def has_permission(self, request, view):
        return view.action == "create"


class IsAuthor(BasePermission):

    message = "Only the author of the resource can modify it."

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.author)


class ReadOnlyContributor(BasePermission):

    message = "Only a contributor of the project can see its resources."

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return bool(bool(request.method in SAFE_METHODS)
                    and len(obj.users_contributors.filter(id=request.user.id)))
