from django.db import transaction


class AutoFillAuthorMixin:

    @transaction.atomic
    def perform_create(self, serializer):
        user = self.request.user
        serializer.validated_data["author"] = user
        return serializer.save()
