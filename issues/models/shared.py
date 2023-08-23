from django.db import models


class AuthoredAndTimestamped:
    author = models.ForeignKey("Contributor", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
