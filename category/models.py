from django.db import models

# Create your models here.
from user.models import TimeStampedModel, User


class Category(TimeStampedModel):
    contents = models.CharField(max_length=64)

    def __str__(self):
        return self.contents


class CategoryMapping(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
