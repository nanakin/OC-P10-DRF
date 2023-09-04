from .shared import AuthoredAndTimestamped
import uuid
from django.db import models


class Comment(AuthoredAndTimestamped):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(max_length=2048)
    issue = models.ForeignKey(to="Issue", on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.uuid}"

    @property
    def users_contributors(self):
        return self.issue.users_contributors
