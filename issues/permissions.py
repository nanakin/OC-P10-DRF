from rest_framework.permissions import BasePermission, SAFE_METHODS


class CreationOK(BasePermission):

    def has_permission(self, request, view):
        return view.action == "create"


class IsAuthor(BasePermission):

    message = "Only the author of the resource can modify it."

    def has_permission(self, request, view):
        # print("has_permission (author)")
        # return request.method in SAFE_METHODS
        return True

    def has_object_permission(self, request, view, obj):
        # print("has_obj_permission (author)", obj, request.user, obj.author)
        return bool(request.user == obj.author)


class ReadOnlyContributor(BasePermission):

    message = "Only a contributor of the project can see its resources."

    def has_permission(self, request, view):
        # print("has_permission (contributor)")
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        # print("has_obj_permission (contributor)", obj, request.user, obj.contributors.filter(id=request.user.id))
        return bool(request.method in SAFE_METHODS
                    and len(obj.contributors.filter(id=request.user.id)))
