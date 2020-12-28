from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .forms import CustomUserRegistrationForm, CustomUserChangeForm
from .models import CustomUser

# https://django.readthedocs.io/en/stable/ref/contrib/admin/actions.html
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserRegistrationForm
    form = CustomUserChangeForm
    model = CustomUser
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    list_display = ['firstname','lastname','email','date_of_birth','date_joined','student','membership','is_staff']
    list_filter = ('student','membership','is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'new_password')}),
        ('Personal Information', {'fields': ('firstname', 'lastname', 'date_of_birth')}),
        ('Membership Information', {'fields': ('membership',)}),
        #('Account information', {'fields': ['description'], 'classes': ['collapse']}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password', 'password2')}),
        ('Personal Information', {'fields': ('firstname', 'lastname', 'date_of_birth')}),
        ('Membership Information', {'fields': ('membership',)}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
