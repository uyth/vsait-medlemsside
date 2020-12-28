from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import CustomUser

class CustomUserRegistrationForm(forms.ModelForm):
    firstname = forms.CharField(max_length=20, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'Firstname*'}))
    lastname = forms.CharField(max_length=20, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'Lastname*'}))
    email = forms.EmailField(max_length=20, widget=forms.widgets.EmailInput(attrs={'class': 'inp','placeholder':'Email*'}))
    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d','%d/%m/%Y','%m/%d/%Y'],widget=forms.widgets.DateInput(format=('%d/%m/%Y'), attrs={'placeholder':'Date of birth*','type':'date'}))
    password = forms.CharField(min_length = 8, max_length=50, widget=forms.widgets.PasswordInput(attrs={'class': 'inp','placeholder':'Password*'}))
    password2 = forms.CharField(min_length = 8, max_length=50, widget=forms.widgets.PasswordInput(attrs={'class': 'inp','placeholder':'Confirm Password*'}))

    class Meta:
        model = CustomUser
        fields = ('firstname','lastname','email','date_of_birth','password')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        user_list = CustomUser.objects.filter(email=email)
        if user_list.count():
            raise ValidationError('There is already an account associated with that email.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

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
        }
        custom_user = CustomUser.objects.create_user(
            context['email'],
            context['firstname'],
            context['lastname'],
            context['date_of_birth'],
            context['password']
        )
        return custom_user

class CustomUserChangeForm(UserChangeForm):
    firstname = forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'First name*'}))
    lastname = forms.CharField(max_length=50, widget=forms.widgets.TextInput(attrs={'class': 'inp','placeholder':'Last name*'}))
    email = forms.EmailField(max_length=120, widget=forms.widgets.EmailInput(attrs={'class': 'inp','placeholder':'Email*'}))
    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d','%d/%m/%Y','%m/%d/%Y'],widget=forms.widgets.DateInput(format=('%d/%m/%Y'), attrs={'placeholder':'Date of birth*','type':'date'}))
    new_password = ReadOnlyPasswordHashField(label=("Password"),help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"../password/\">this form</a>."))
    
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        email = str(self).split("value")[1].split("\"")[1]
        email_list = CustomUser.objects.filter(email=email)
        date = str(email_list.get().date_of_birth).split()[0]
        kwargs.update(initial={'date_of_birth': date}) # Updates the datetime
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    class Meta:
        model = CustomUser
        fields = ('firstname','lastname','email','date_of_birth','new_password')
        #fields = '__all__'
        exclude = ['date_of_birth']

    def clean_email(self):
        email = self.cleaned_data['email']
        email_list = CustomUser.objects.filter(email=email)
        sameUser = CustomUser.objects.get(email=email).id == email_list.get().id
        if email_list.count() and not sameUser:
            raise ValidationError('There is already an account associated with that email.')
        return email

class LoginForm(AuthenticationForm):
    # Username here is hidden/gets skipped
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
        print(11,self.cleaned_data)
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
