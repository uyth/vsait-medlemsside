from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'email', 'password', 'date_of_birth', 'food_needs', 'type', 'has_vietnamese_background',]

admin.site.register(CustomUser, CustomUserAdmin)