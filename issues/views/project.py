from ..serializers import ProjectListSerializer, ProjectDetailSerializer, ProjectSerializer
from ..models import Project
from users.models import User  # to be removed
from issues.models import Contributor
from rest_framework import viewsets
from django.db import transaction
from .shared import AutoFillAuthorMixin
from issues.permissions import IsAuthor, ReadOnlyContributor, CreationOK
from rest_framework import permissions


class ProjectViewSet(AutoFillAuthorMixin, viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated & (IsAuthor | ReadOnlyContributor | CreationOK)]

    def get_queryset(self):
        return Project.objects.all()
        # return self.request.user.projects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        elif self.action == "create":
            return ProjectSerializer
        else:
            return ProjectDetailSerializer

    @transaction.atomic  # required ?
    def perform_create(self, serializer):
        project = super().perform_create(serializer)
        Contributor.objects.create(user=self.request.user, contribute_to=project)

