from django import forms
from django.db import models
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Event
from home.models import VsaitUser

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, VsaitUser):
        return VsaitUser.firstname + " ; " + VsaitUser.lastname + " ; " +VsaitUser.email

# Add and change form to use custom javascript
class EventForm(forms.ModelForm):
    class Media:
        css = {
            'all': ('admin/css/events.css',)
        }
        js = ('admin/js/vendor/jquery/jquery.min.js',
                'admin/js/jquery.init.js',
                'admin/js/draft.js',
                'admin/js/image_upload.js',
                'admin/js/event_registrations.js',
                'admin/js/datetime_field.js',)

class EventChangeForm(forms.ModelForm):
    class Media:
        css = {
            'all': ('admin/css/events.css',)
        }
        js = ('admin/js/vendor/jquery/jquery.min.js',
                'admin/js/jquery.init.js',
                'admin/js/draft.js',
                'admin/js/image_upload.js',
                'admin/js/event_registrations.js',
                'admin/js/datetime_field.js',)

    registrations = CustomMMCF(
        queryset=VsaitUser.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    waiting_list = CustomMMCF(
        queryset=VsaitUser.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    """
    def __init__(self, *args, **kwargs):
        # Quickfix for initialization of last edited on change
        super(EventChangeForm, self).__init__(*args, **kwargs) # Init and loads all fields
        date = timezone.now();
        list(kwargs.values())[0].last_edited = date; # Updates the last edited
        super(EventChangeForm, self).__init__(*args, **kwargs) # Updates all fields
    """
