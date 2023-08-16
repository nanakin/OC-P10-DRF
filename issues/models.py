from django.db import models
from django.conf import settings
import uuid


class AuthoredAndTimestamped:
    author = models.ForeignKey("Contributor", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Project(models.Model, AuthoredAndTimestamped):
    TYPE_CHOICES = [
        ("BE", "Backend"),
        ("FE", "Frontend"),
        ("i", "iOS"),
        ("A", "Android"),
    ]

    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=2048, blank=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.title} [{self.type.name}]"


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to="Project", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user} > {self.project}"


class Issue(models.Model, AuthoredAndTimestamped):

    TAG_CHOICES = [
        ("BUG", "Bug"),
        ("TASK", "Task"),
        ("FEAT", "Feature")
    ]
    STATUS_CHOICES = [
        ("TODO", "To Do"),
        ("PROG", "In Progress"),
        ("FINI", "Finished")
    ]
    PRIORITY_CHOICES = [
        ("L", "LOW"),
        ("M", "MEDIUM"),
        ("H", "HIGH")
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="TODO")
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=4, choices=TAG_CHOICES)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(to=Contributor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"[{self.tag.name} | {self.status.name} | {self.priority.name}] {self.title}"


class Comment(models.Model, AuthoredAndTimestamped):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(max_length=2048)
    project = models.ForeignKey(to=Issue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.uuid}"
