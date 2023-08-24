from rest_framework import serializers
from ..models import Project  # tester sans l'import


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectListSerializer(ProjectSerializer):
    class Meta(ProjectSerializer.Meta):
        fields = ["id", "title", "type"]


class ProjectDetailSerializer(ProjectSerializer):
    class Meta(ProjectSerializer.Meta):
        read_only_fields = ["author"]
