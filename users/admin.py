from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

''' 
Superuser info:
email: admin@admin.no
name: admin
Date of birth: 2000-01-01
Food needs:
Is student: True
Has vietnamese background: True
password: admin

'''

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ()  # Contain only fields in your `custom-user-model`
    list_filter = ()  # Contain only fields in your `custom-user-model` intended for filtering. Do not include `groups`since you do not have it
    search_fields = ()  # Contain only fields in your `custom-user-model` intended for searching
    ordering = ()  # Contain only fields in your `custom-user-model` intended to ordering
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)