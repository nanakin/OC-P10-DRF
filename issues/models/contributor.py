from django.conf import settings
from django.db import models

from issues.models.shared import AuthoredAndTimestamped


class Contributor(AuthoredAndTimestamped):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributions")
    contribute_to = models.ForeignKey(to="Project", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'contribute_to')

    def __str__(self):
        return f"{self.user} > {self.contribute_to}"

    @property
    def users_contributors(self):
        return self.contribute_to.users_contributors
