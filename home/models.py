from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime

from .managers import VsaitUserManager

# User class which implements AbstractBaseUser
class VsaitUser(AbstractBaseUser, PermissionsMixin):
    username = None # Django by default needs this parameter for auth, will be hidden
    firstname = models.CharField(_('firstname'), max_length=64)
    lastname = models.CharField(_('lastname'), max_length=64)
    email = models.EmailField(_('email'), max_length=240,unique=True)
    date_of_birth = models.DateTimeField(default=timezone.now)
    password = models.CharField(_('password'),max_length=240)

    food_needs = models.CharField(_('food_needs'), max_length=240, blank=True) # Allergies and such
    student = models.BooleanField(default=False)

    # The tags below will be hidden on user registration
    is_staff = models.BooleanField(default=False) # Marks the user to be a normal user
    date_joined = models.DateTimeField(default=timezone.now)
    membership = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','date_of_birth','password']

    objects = VsaitUserManager()

    def __str__(self):
        return self.email
