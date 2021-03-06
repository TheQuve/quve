from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserClass(TimeStampedModel):
    name = models.CharField(max_length=64)
    rank = models.IntegerField()


class User(AbstractUser, TimeStampedModel):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not_specified', 'not specified')
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    profile_image = models.ImageField(null=True)
    point = models.IntegerField(default=500000000)
    user_class = models.ForeignKey(
        UserClass, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.email
