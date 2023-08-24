from rest_framework import mixins, viewsets
from ..models import Contributor
from ..serializers import ContributorSerializer


class ContributorViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                         mixins.ListModelMixin, viewsets.GenericViewSet):  # disable update

    # permission_classes = to be defined
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
