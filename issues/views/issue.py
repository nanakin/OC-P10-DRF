from rest_framework import viewsets
from issues.models import Issue
from issues.serializers import IssueListSerializer, IssueDetailSerializer, IssueCreateSerializer
from .shared import AutoFillAuthorMixin


class IssueViewSet(AutoFillAuthorMixin, viewsets.ModelViewSet):

    # permission_classes = to be defined

    def get_queryset(self):
        queryset = Issue.objects.all()
        # user = User.objects.get(username="anna")  # to be changed by self.request.user
        #if user.is_authenticated:  # utiliser les permission_classes ?
        #queryset = queryset.filter(project__in=user.con.all())
        #queryset = user.contributions.all() values_list("projects")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return IssueListSerializer
        elif self.action == "create":
            return IssueCreateSerializer
        else:
            return IssueDetailSerializer
