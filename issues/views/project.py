from django.db import transaction
from rest_framework import permissions, viewsets

from issues.models import Contributor
from issues.permissions import CreationOK, IsAuthor, ReadOnlyContributor

from ..serializers import ProjectDetailSerializer, ProjectListSerializer, ProjectSerializer
from .shared import AutoFillAuthorMixin


class ProjectViewSet(AutoFillAuthorMixin, viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated & (IsAuthor | ReadOnlyContributor | CreationOK)]

    def get_queryset(self):
        return self.request.user.projects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        elif self.action == "create":
            return ProjectSerializer
        else:
            return ProjectDetailSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        project = super().perform_create(serializer)
        Contributor.objects.create(user=self.request.user, contribute_to=project)
