from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .managers import UserManager
from django.db import models

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length = 254, unique=True, blank=False)
    name = models.CharField(max_length = 254, blank=False)
    date_of_birth = models.DateField(blank=False)
    food_needs = models.TextField(blank=True)
    is_student = models.BooleanField(blank=False)
    has_vietnamese_background = models.BooleanField(blank=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'date_of_birth', 'is_student', 'has_vietnamese_background']

    def __str__(self):
        return self.username
