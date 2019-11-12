from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum

class UserType(Enum):
    STUDENT = 1
    NON_STUDENT = 2

class CustomUser(AbstractUser):
    id = models.IntegerField()
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length = 50)
    date_of_birth = models.DateField()
    food_needs = models.ArrayField(models.CharField(max_length = 50))
    type = models.CharField(
        max_length = 2,
        choices=[(tag, tag.value) for tag in UserType])
    has_vietnamese_background = models.BooleanField()

    def __str__(self):
        return self.username
