from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name, date_of_birth, is_student, has_vietnamese_background, password=None):
        if not email or name or date_of_birth or is_student or has_vietnamese_background:
            raise ValueError('Users must have an email, name, dob, student status, viet background status')

        user = self.model(
            email = email,
            name = name,
            date_of_birth = date_of_birth,
            is_student = is_student,
            has_vietnamese_background = has_vietnamese_background
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, date_of_birth, is_student, has_vietnamese_background, password):
        user = self.model(
            email=email,
            name=name,
            date_of_birth=date_of_birth,
            is_student=is_student,
            has_vietnamese_background=has_vietnamese_background
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

