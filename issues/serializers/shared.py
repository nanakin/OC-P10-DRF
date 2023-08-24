from rest_framework import serializers


class ReadOnlyAuthor(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ["author"]
