from django.conf import settings
from django.db import models


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributing_to")
    project = models.ForeignKey(to="Project", on_delete=models.CASCADE, related_name="contributors")

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user} > {self.project}"
