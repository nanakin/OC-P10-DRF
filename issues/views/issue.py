from rest_framework import permissions, viewsets

from issues.models import Issue
from issues.permissions import CreationOK, IsAuthor, ReadOnlyContributor
from issues.serializers import IssueCreateSerializer, IssueDetailSerializer, IssueListSerializer

from .shared import AutoFillAuthorMixin


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
