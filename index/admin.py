from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserRegistrationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserRegistrationForm
    form = CustomUserChangeForm
    model = CustomUser
    ordering = ('email',)
    list_display = ['firstname','lastname','email','date_of_birth','date_joined','student','membership']
    list_filter = ('student',)
    fieldsets = (
        (None, {'fields': ('email', 'new_password', 'new_password2')}),
        ('Personal Information', {'fields': ('firstname', 'lastname', 'date_of_birth')}),
        ('Membership Information', {'fields': ('membership',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password', 'password2')}),
        ('Personal Information', {'fields': ('firstname', 'lastname', 'date_of_birth')}),
        #('Company Information', {'fields': ('company',)}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
