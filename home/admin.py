from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import VsaitUserRegistrationForm, VsaitUserChangeForm
from .models import VsaitUser

# https://django.readthedocs.io/en/stable/ref/contrib/admin/actions.html
# Implements the UserAdmin
class VsaitUserAdmin(UserAdmin):
    add_form = VsaitUserRegistrationForm # Add new user form
    form = VsaitUserChangeForm # Edit user form
    model = VsaitUser
    # Filtering and ordering of users, marks which tags to be shown
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    list_display = ['firstname','lastname','email','date_of_birth','date_joined','student','membership','is_staff']
    list_filter = ('student','membership','is_staff')
    # Fieldset for the user forms
    fieldsets = (
        (None, {'fields': ('email', 'new_password')}),
        ('Personal Information', {'fields': ('firstname', 'lastname', 'date_of_birth')}),
        ('Membership Information', {'fields': ('membership',)}),
        ('Account information', {'fields': ['is_staff','is_superuser'], 'classes': ['collapse']}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password', 'password2')}),
        ('Personal Information', {'fields': ('firstname', 'lastname', 'date_of_birth')}),
        ('Membership Information', {'fields': ('membership',)}),
    )

admin.site.register(VsaitUser, VsaitUserAdmin)
admin.site.unregister(Group)
