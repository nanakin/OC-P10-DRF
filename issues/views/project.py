from ..serializers import ProjectListSerializer, ProjectDetailSerializer, ProjectCreateSerializer
from ..models import Project
from users.models import User  # to be removed
from issues.models import Contributor
from rest_framework import viewsets
from django.db import transaction


class ProjectViewSet(viewsets.ModelViewSet):

    # permission_classes = to be defined
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        elif self.action == "create":
            return ProjectSerializer
        else:
            return ProjectDetailSerializer

    @transaction.atomic  # required ?
    def perform_create(self, serializer):
        user = User.objects.get(username="anna")  # to be changed by self.request.user
        serializer.validated_data["author"] = user
        project = serializer.save()
        Contributor.objects.create(user=user, contribute_to=project)

