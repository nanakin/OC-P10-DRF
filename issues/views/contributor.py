from rest_framework import mixins, permissions, viewsets

from issues.permissions import CreationOK, IsAuthor, ReadOnlyContributor

from ..models import Contributor
from ..serializers import ContributorSerializer
from .shared import AutoFillAuthorMixin


class ContributorViewSet(
    AutoFillAuthorMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):  # disable update
    permission_classes = [permissions.IsAuthenticated & (IsAuthor | ReadOnlyContributor | CreationOK)]

    def get_queryset(self):
        return Contributor.objects.filter(contribute_to__in=self.request.user.projects.all())

    serializer_class = ContributorSerializer
