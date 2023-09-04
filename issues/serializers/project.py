from rest_framework import serializers

from ..models import Project
from .shared import ReadOnlyAuthor


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectListSerializer(ProjectSerializer):
    class Meta(ProjectSerializer.Meta):
        fields = ["id", "title", "type"]


class ProjectDetailSerializer(ProjectSerializer, ReadOnlyAuthor):
    class Meta(ProjectSerializer.Meta, ReadOnlyAuthor.Meta):
        pass
