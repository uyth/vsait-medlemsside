from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'name', 'date_of_birth', 'food_needs', 'is_student', 'has_vietnamese_background')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'name', 'date_of_birth', 'food_needs', 'is_student', 'has_vietnamese_background')