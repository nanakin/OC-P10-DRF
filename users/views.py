from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserCreateSerializer, UserListSerializer, UserDetailSerializer
from .permissions import UnauthenticatedCreation, OwnerEdition


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    permission_classes = [UnauthenticatedCreation | (permissions.IsAuthenticated & OwnerEdition)]

    def get_serializer_class(self):
        print(f"{self.action=} {self.queryset.model}")
        if self.action == "create":
            return UserCreateSerializer
        elif self.action == "list":
            return UserListSerializer
        else:
            return UserDetailSerializer
