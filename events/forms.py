from django import forms
from django.db import models
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Event

class CustomDateTimeField(models.DateTimeField):
    widget = forms.widgets.DateTimeInput(format="%d %b %Y %H:%M:%S %Z")
    def to_python(self, value):
        print(value)
        if value is None:
            return value

# Add and change form to use custom javascript
class EventForm(forms.ModelForm):
    class Media:
        js = ('admin/js/vendor/jquery/jquery.min.js',
                'admin/js/jquery.init.js',
                'admin/js/draft.js',
                'admin/js/image_upload.js',
                'admin/js/datetime_field.js',)

class EventChangeForm(forms.ModelForm):
    endTime = CustomDateTimeField
    class Media:
        js = ('admin/js/vendor/jquery/jquery.min.js',
                'admin/js/jquery.init.js',
                'admin/js/draft.js',
                'admin/js/image_upload.js',
                'admin/js/datetime_field.js',)

    def __init__(self, *args, **kwargs):
        """ Quickfix for initialization of last edited on change"""
        super(EventChangeForm, self).__init__(*args, **kwargs) # Init and loads all fields
        date = timezone.now();
        list(kwargs.values())[0].last_edited = date; # Updates the last edited
        super(EventChangeForm, self).__init__(*args, **kwargs) # Updates all fields

"""
class DateTimeField(BaseTemporalField):
    widget = DateTimeInput
    input_formats = formats.get_format_lazy('DATETIME_INPUT_FORMATS')
    default_error_messages = {
        'invalid': _('Enter a valid date/time.'),
    }

    def prepare_value(self, value):
        if isinstance(value, datetime.datetime):
            value = to_current_timezone(value)
        return value

    def to_python(self, value):
        # Validates that the input can be converted to a datetime. Returns a
        # Python datetime.datetime object.
        if value in self.empty_values:
            return None
        if isinstance(value, datetime.datetime):
            return from_current_timezone(value)
        if isinstance(value, datetime.date):
            result = datetime.datetime(value.year, value.month, value.day)
            return from_current_timezone(result)
        if isinstance(value, list):
            # Input comes from a SplitDateTimeWidget, for example. So, it's two
            # components: date and time.
            warnings.warn(
                'Using SplitDateTimeWidget with DateTimeField is deprecated. '
                'Use SplitDateTimeField instead.',
                RemovedInDjango19Warning, stacklevel=2)
            if len(value) != 2:
                raise ValidationError(self.error_messages['invalid'], code='invalid')
            if value[0] in self.empty_values and value[1] in self.empty_values:
                return None
            value = '%s %s' % tuple(value)
        result = super(DateTimeField, self).to_python(value)
        return from_current_timezone(result)

    def strptime(self, value, format):
        return datetime.datetime.strptime(force_str(value), format)
"""
