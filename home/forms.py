from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import VsaitUser

# Registration form
class VsaitUserRegistrationForm(forms.ModelForm):
    firstname = forms.CharField(max_length=100, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'Firstname*'}))
    lastname = forms.CharField(max_length=100, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'Lastname*'}))
    email = forms.EmailField(max_length=256, widget=forms.widgets.EmailInput(attrs={'class': 'inp','placeholder':'Email*'}))
    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d','%d/%m/%Y','%m/%d/%Y'],widget=forms.widgets.DateInput(format=('%d/%m/%Y'), attrs={'placeholder':'Date of birth*','type':'date','min':str(timezone.now().year-100)+'-01-01','max':str(timezone.now().year-18)+'-01-01'}))
    password = forms.CharField(min_length = 8, max_length=100, widget=forms.widgets.PasswordInput(attrs={'class': 'inp','placeholder':'Password*'}))
    password_confirmation = forms.CharField(min_length = 8, max_length=100, widget=forms.widgets.PasswordInput(attrs={'class': 'inp','placeholder':'Confirm Password*'}))
    food_needs = forms.CharField(max_length=240, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'If any allergies, write them down here.'}), required=False)
    student = forms.BooleanField(required=False)
    class Meta:
        model = VsaitUser
        fields = ('firstname','lastname','email','date_of_birth','password','password_confirmation','food_needs','student')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        user_list = VsaitUser.objects.filter(email=email)
        if user_list.count():
            raise ValidationError('There is already an account associated with that email.')
        return email

    def clean_password_confirmation(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password_confirmation']

        if (password1 and password2) and (password1 != password2):
            raise ValidationError('Passwords do not match.')
        return password2

    def save_m2m(self):
        # Quickfix for admin add forms
        return None

    def save(self, commit=True):
        context = {
            'firstname':self.cleaned_data['firstname'],
            'lastname':self.cleaned_data['lastname'],
            'email':self.cleaned_data['email'],
            'date_of_birth':self.cleaned_data['date_of_birth'],
            'password':self.cleaned_data['password'],
            'food_needs':self.cleaned_data['food_needs'],
            'student':self.cleaned_data['student'],
        }
        vsait_user = VsaitUser.objects.create_user(
            context['email'],
            context['firstname'],
            context['lastname'],
            context['date_of_birth'],
            context['password'],
            context['food_needs'],
            context['student'],
        )
        return vsait_user

# Edit form
class VsaitUserChangeForm(UserChangeForm):
    firstname = forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'First name*'}))
    lastname = forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'Last name*'}))
    email = forms.EmailField(max_length=120, widget=forms.widgets.EmailInput(attrs={'class': 'inp','placeholder':'Email*'}))
    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d','%d/%m/%Y','%m/%d/%Y'],widget=forms.widgets.DateInput(format=('%d/%m/%Y'), attrs={'placeholder':'Date of birth*','type':'date'}))
    # Might be changing this under
    new_password = ReadOnlyPasswordHashField(label=("Password"),help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"../password/\">this form</a>."))
    
    def __init__(self, *args, **kwargs):
        """ Quickfix for initialization of visible information shown on admin panel"""
        super(UserChangeForm, self).__init__(*args, **kwargs)
        email = str(self).split("value")[1].split("\"")[1] # Get email string
        user = VsaitUser.objects.filter(email=email).get() # Get user from email string
        date = str(user.date_of_birth).split()[0] # Parse date
        kwargs.update(initial={'date_of_birth': date}) # Updates the datetime
        # kwargs.update(initial={'food_needs': user.food_needs}) # Updates the food_needs
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    class Meta:
        model = VsaitUser
        fields = ('firstname','lastname','email','date_of_birth','new_password')
        exclude = ['date_of_birth']

    def clean_email(self):
        email = self.cleaned_data['email']
        email_list = VsaitUser.objects.filter(email=email)
        sameUser = VsaitUser.objects.get(email=email).id == email_list.get().id
        if email_list.count() and not sameUser:
            raise ValidationError('There is already an account associated with that email.')
        return email

# Profile
class VsaitUserProfileChangeForm(UserChangeForm):
    firstname = forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'First name*'}))
    lastname = forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'Last name*'}))
    email = forms.EmailField(max_length=120, widget=forms.widgets.EmailInput(attrs={'class': 'inp','placeholder':'Email*'}))
    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d','%d/%m/%Y','%m/%d/%Y'],widget=forms.widgets.DateInput(format=('%d/%m/%Y'), attrs={'placeholder':'Date of birth*','type':'date'}))
    # Might be changing this under
    password = forms.CharField(min_length = 8, max_length=50, widget=forms.widgets.PasswordInput(attrs={'class': 'inp','placeholder':'Password*'}))
    password_confirmation = forms.CharField(min_length = 8, max_length=50, widget=forms.widgets.PasswordInput(attrs={'class': 'inp','placeholder':'Confirm Password*'}))
    
    class Meta:
        model = VsaitUser
        fields = ('firstname','lastname','email','date_of_birth','password','password_confirmation')
        exclude = ['date_of_birth']

    def clean_email(self):
        email = self.cleaned_data['email']
        email_list = VsaitUser.objects.filter(email=email)
        sameUser = VsaitUser.objects.get(email=email).id == email_list.get().id
        if email_list.count() and not sameUser:
            raise ValidationError('There is already an account associated with that email.')
        return email

# Profile food_needs form change
class VsaitUserFoodNeedsChangeForm(forms.Form):
    food_needs = forms.CharField(max_length=240, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'Food needs*'}))
    class Meta:
        model = VsaitUser
        fields = ('food_needs',)
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(VsaitUserFoodNeedsChangeForm, self).__init__(*args, **kwargs)
        kwargs.update(initial={'food_needs': self.user.food_needs}) # Updates the food_needs
        super(VsaitUserFoodNeedsChangeForm, self).__init__(*args, **kwargs)

# Profile is_student
class VsaitUserIsStudent(forms.Form):
    is_student = forms.BooleanField(required=False)
    class Meta:
        model = VsaitUser
        fields = ('student',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(VsaitUserIsStudent, self).__init__(*args, **kwargs)
        kwargs.update(initial={'is_student': self.user.student}) # Updates the student
        super(VsaitUserIsStudent, self).__init__(*args, **kwargs)

# The login form shown on the homepage/index
class LoginForm(AuthenticationForm):
    # Quickfix: Since the parameter username has to be sent, username here is hidden
    username = forms.CharField(max_length=5, widget=forms.widgets.TextInput(attrs={'class': 'this_does_nothing','value':'VSAIT','hidden':True}))
    email = forms.CharField(max_length=20, widget=forms.widgets.EmailInput(attrs={'class': 'inp','placeholder':'Email'}))
    password = forms.CharField(max_length=32, widget=forms.widgets.PasswordInput(attrs={'class': 'inp','placeholder':'Password'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                pass # render index
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            pass # render index

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        if self.user_cache:
            return self.user_cache
        return None

