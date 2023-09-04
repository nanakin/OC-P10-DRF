from rest_framework import serializers

from ..models import Comment, Issue
from .shared import ReadOnlyAuthor


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def validate_issue(self, issue):
        user = self.context.get("request").user
        if issue not in Issue.objects.filter(project__contributors=user):
            raise serializers.ValidationError("Author of the comment isn't a contributors of the project")
        return issue


class CommentListSerializer(CommentSerializer):
    class Meta(CommentSerializer.Meta):
        fields = ["uuid"]


class CommentDetailSerializer(CommentSerializer, ReadOnlyAuthor):
    class Meta(CommentSerializer.Meta, ReadOnlyAuthor.Meta):
        pass
