from rest_framework import mixins, viewsets, permissions
from ..models import Contributor
from ..serializers import ContributorSerializer
from issues.permissions import IsAuthor, ReadOnlyContributor, CreationOK


class ContributorViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                         mixins.ListModelMixin, viewsets.GenericViewSet):  # disable update

    permission_classes = [permissions.IsAuthenticated & (IsAuthor | ReadOnlyContributor | CreationOK)]

    def get_queryset(self):
        return self.request.user.contributions.all()

    serializer_class = ContributorSerializer
