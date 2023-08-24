from rest_framework import viewsets
from .project import ProjectViewSet
from .contributor import ContributorViewSet


class CommentViewSet(viewsets.ModelViewSet):
    pass


class IssueViewSet(viewsets.ModelViewSet):
    pass
