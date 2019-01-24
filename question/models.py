from django.db import models

from category.models import Category
from user.models import TimeStampedModel, User


class Question(TimeStampedModel):
    title = models.CharField(max_length=255)
    contents = models.TextField()
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True
    )
    point = models.IntegerField(default=0)
    limit = models.IntegerField(default=1800)
    is_open = models.BooleanField(default=True)
    user_class = models.CharField(blank=True)
    region = models.CharField(blank=True)

    def __str__(self):
        return self.title
