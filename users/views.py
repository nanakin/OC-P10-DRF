from rest_framework import viewsets
from .models import User
from .serializers import UserCreateSerializer, UserListSerializer, UserDetailSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    # permission_classes = to be defined

    def get_serializer_class(self):
        print(f"{self.action=} {self.queryset.model}")
        if self.action == "create":
            return UserCreateSerializer
        elif self.action == "list":
            return UserListSerializer
        elif self.action in ("retrieve", "update", "partial_update"):
            return UserDetailSerializer
        else:
            return UserDetailSerializer
