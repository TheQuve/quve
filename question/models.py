from django.db import models

from user.models import TimeStampedModel, User


class Question(TimeStampedModel):
    title = models.CharField(max_length=255)
    contents = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
