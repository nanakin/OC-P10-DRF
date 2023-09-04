from rest_framework import viewsets, permissions
from issues.models import Issue
from issues.serializers import IssueListSerializer, IssueDetailSerializer, IssueCreateSerializer
from .shared import AutoFillAuthorMixin
from issues.permissions import IsAuthor, ReadOnlyContributor, CreationOK


class IssueViewSet(AutoFillAuthorMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & (IsAuthor | ReadOnlyContributor | CreationOK)]

    def get_queryset(self):
        user = self.request.user
        return Issue.objects.filter(project__contributors=user)

    def get_serializer_class(self):
        if self.action == "list":
            return IssueListSerializer
        elif self.action == "create":
            return IssueCreateSerializer
        else:
            return IssueDetailSerializer
