from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Event

# Add and change form to use custom javascript
class EventForm(forms.ModelForm):
    class Media:
        js = ('admin/js/vendor/jquery/jquery.min.js',
                'admin/js/jquery.init.js',
                'admin/js/draft.js',)
class EventChangeForm(forms.ModelForm):
    class Media:
        js = ('admin/js/vendor/jquery/jquery.min.js',
                'admin/js/jquery.init.js',
                'admin/js/draft.js',)
