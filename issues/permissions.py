from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):

    message = "Only the author of the resource can modify it."

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.author)


class ReadOnlyContributor(BasePermission):

    message = "Only a contributor of the project can see its resources."

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS
                    and obj.contributors.filter(id=request.user.id))
