from django.db import models

# Create your models here.
from user.models import TimeStampedModel, User


class Category(TimeStampedModel):
    contents = models.CharField(max_length=64)

    def __str__(self):
        return self.contents


class Region(TimeStampedModel):
    name = models.CharField(max_length=64)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return self.name


class CategoryMapping(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('category', 'user')
