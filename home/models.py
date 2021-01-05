from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime

from .managers import VsaitUserManager

YEAR_CHOICES = [
    ("2019","2019"),
    ("2020","2020"),
    ("2021","2021"),
    ("2022","2022"),
    ("2023","2023"),
    ("2024","2024"),
    ("2025","2025"),
    ("2026","2026"),
    ("2027","2027"),
    ("2028","2028"),
    ("2029","2029"),
    ("2030","2030"),
]
# Membership class
class Membership(models.Model):
    year = models.CharField(max_length=5, choices=YEAR_CHOICES, default=str(timezone.now().year))
    
    def __str__(self):
        return self.year

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
    
    # New membership
    memberships = models.ManyToManyField(Membership, related_name='memberships', blank=True)
    pending_membership = models.BooleanField(default=False) # Used to temporary assign own memberships

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','date_of_birth','password']

    objects = VsaitUserManager()

    def __str__(self):
        return self.email
    # Membership display
    def has_membership(self):
        return str(timezone.now().year) in [x.year for x in self.memberships.all()]
    # Dates
    def date_of_birth_display(self):
        return self.date_of_birth.strftime("%d.%b %Y")
    def date_joined_display(self):
        return self.date_joined.strftime("%d.%b %Y")
    date_of_birth_display.admin_order_field = 'date_of_birth'
    date_joined_display.admin_order_field = 'date_joined'
    has_membership.boolean = True
