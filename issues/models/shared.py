from django.db import models


class AuthoredAndTimestamped(models.Model):
    author = models.ForeignKey("Contributor", on_delete=models.CASCADE, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
