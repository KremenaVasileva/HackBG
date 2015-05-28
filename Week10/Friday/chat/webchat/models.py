from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
