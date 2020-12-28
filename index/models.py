from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
import datetime
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager
# Create your models here.
#from events.models import Event

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    firstname = models.CharField(_('firstname'), max_length=64)
    lastname = models.CharField(_('lastname'), max_length=64)
    email = models.EmailField(_('email'), max_length=240,unique=True)
    date_of_birth = models.DateTimeField(default=timezone.now)
    password = models.CharField(_('password'),max_length=240)

    student = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    membership = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','date_of_birth','password']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
