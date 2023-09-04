from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .permissions import Owner, UnauthenticatedCreation
from .serializers import PasswordSerializer, UserCreateSerializer, UserDetailSerializer, UserListSerializer


class UserViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

    def get_permissions(self):
        if self.action in ('set_password', "change_password") or self.action != "create":
            self.permission_classes = [permissions.IsAuthenticated & Owner]
        else:
            self.permission_classes = [UnauthenticatedCreation]
        return super(UserViewSet, self).get_permissions()

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        elif self.action == "list":
            return UserListSerializer
        else:
            return UserDetailSerializer

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        return self.set_password(request, pk)
