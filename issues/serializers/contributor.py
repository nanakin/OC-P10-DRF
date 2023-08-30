from rest_framework import serializers
from issues.models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"

    def validate_contribute_to(self, contribute_to):
        user = self.context.get("request").user
        if contribute_to not in user.projects.all():
            raise serializers.ValidationError("Only a contributor can add contributors to a project")
        return contribute_to
