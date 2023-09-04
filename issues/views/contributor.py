from rest_framework import mixins, viewsets, permissions
from ..models import Contributor
from ..serializers import ContributorSerializer
from issues.permissions import IsAuthor, ReadOnlyContributor, CreationOK
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
