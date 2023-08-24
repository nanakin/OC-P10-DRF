from django.db import models
from django.conf import settings


class AuthoredAndTimestamped(models.Model):
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
