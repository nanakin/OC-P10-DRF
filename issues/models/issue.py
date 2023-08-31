from django.db import models
from .shared import AuthoredAndTimestamped


class Issue(AuthoredAndTimestamped):

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
    project = models.ForeignKey(to="Project", on_delete=models.CASCADE, related_name="issues")
    assigned_to = models.ForeignKey(to="Contributor", on_delete=models.SET_NULL, null=True,
                                    related_name="issues_assigned")

    def __str__(self):
        return f"[{self.tag} | {self.status} | {self.priority}] {self.title}"

    @property
    def users_contributors(self):
        return self.project.users_contributors
