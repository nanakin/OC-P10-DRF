from rest_framework import viewsets
from django.db import transaction
from users.models import User


class AutoFillAuthorMixin:

    @transaction.atomic  # required ?
    def perform_create(self, serializer):
        user = User.objects.get(username="anna")  # to be changed by self.request.user
        serializer.validated_data["author"] = user
        return serializer.save()
