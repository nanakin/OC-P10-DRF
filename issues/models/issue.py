from django.db import models
from .shared import AuthoredAndTimestamped


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
    project = models.ForeignKey(to="Project", on_delete=models.CASCADE, related_name="issues")
    assigned_to = models.ForeignKey(to="Contributor", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"[{self.tag} | {self.status} | {self.priority}] {self.title}"
