from django.conf import settings
from django.db import models


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contribute_to = models.ForeignKey(to="Project", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'contribute_to')

    def __str__(self):
        return f"{self.user} > {self.contribute_to}"
