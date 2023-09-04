from rest_framework import serializers

from ..models import Issue
from .shared import ReadOnlyAuthor


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"


class IssueCreateSerializer(IssueSerializer):
    def validate(self, data):
        if "assigned_to" in data and data["assigned_to"].contribute_to != data["project"]:
            raise serializers.ValidationError(
                {
                    "assigned_to": 'Invalid assignment, the assignee is not contributing to the project',
                    "project": 'The project is not compatible with the assigned contributor',
                }
            )
        return data

    def validate_project(self, project):
        user = self.context.get("request").user
        if project not in user.projects.all():
            raise serializers.ValidationError("Author of the issue isn't a contributors of the project")
        return project


class IssueListSerializer(IssueSerializer):
    class Meta(IssueSerializer.Meta):
        fields = ["id", "title", "project"]


class IssueDetailSerializer(IssueSerializer, ReadOnlyAuthor):
    class Meta(IssueSerializer.Meta, ReadOnlyAuthor.Meta):
        pass

    def validate(self, data):
        project = data["project"] if "project" in data else self.instance.project
        assigned_to = data["assigned_to"] if "assigned_to" in data else self.instance.assigned_to

        if assigned_to and assigned_to.contribute_to != project:
            raise serializers.ValidationError(
                {
                    "assigned_to": 'Invalid assignment, the assignee is not contributing to the project',
                    "project": 'The project is not compatible with the assigned contributor',
                }
            )
        return data
