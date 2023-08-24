from rest_framework import serializers
from ..models import Comment
from .shared import ReadOnlyAuthor


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentListSerializer(CommentSerializer):
    class Meta(CommentSerializer.Meta):
        fields = ["uuid"]


class CommentDetailSerializer(CommentSerializer, ReadOnlyAuthor):
    class Meta(CommentSerializer.Meta, ReadOnlyAuthor.Meta):
        pass
