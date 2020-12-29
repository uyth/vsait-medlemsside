from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class VsaitUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email,firstname,lastname,date_of_birth,password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        # Normalize the inputs, gives inputvalidation respectively
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            firstname=firstname,
            lastname=lastname,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,firstname,lastname,date_of_birth,password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        # Set default parameters to true for a superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email,firstname,lastname,date_of_birth,password, **extra_fields)
