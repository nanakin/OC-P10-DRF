from rest_framework import permissions, viewsets

from issues.models import Comment
from issues.permissions import CreationOK, IsAuthor, ReadOnlyContributor
from issues.serializers import CommentDetailSerializer, CommentListSerializer, CommentSerializer

from .shared import AutoFillAuthorMixin


class CommentViewSet(AutoFillAuthorMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & (IsAuthor | ReadOnlyContributor | CreationOK)]

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(issue__project__contributors=user)

    def get_serializer_class(self):
        if self.action == "list":
            return CommentListSerializer
        elif self.action == "create":
            return CommentSerializer
        else:
            return CommentDetailSerializer
