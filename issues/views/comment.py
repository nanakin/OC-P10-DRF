from rest_framework import viewsets, permissions
from issues.models import Comment
from issues.serializers import CommentListSerializer, CommentDetailSerializer, CommentSerializer
from .shared import AutoFillAuthorMixin
from issues.permissions import IsAuthor, ReadOnlyContributor, CreationOK


class CommentViewSet(AutoFillAuthorMixin, viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated & (IsAuthor | ReadOnlyContributor | CreationOK)]

    def get_queryset(self):
        queryset = Comment.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return CommentListSerializer
        elif self.action == "create":
            return CommentSerializer
        else:
            return CommentDetailSerializer
