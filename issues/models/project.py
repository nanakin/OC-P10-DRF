from django.db import models
from .shared import AuthoredAndTimestamped


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
        return f"{self.title} [{self.type}]"
