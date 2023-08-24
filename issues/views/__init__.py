from rest_framework import viewsets
from .project import ProjectViewSet
from .contributor import ContributorViewSet
from .issue import IssueViewSet

class CommentViewSet(viewsets.ModelViewSet):
    pass
