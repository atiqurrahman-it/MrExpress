# Create your models here.
from django.db import models

# to create a custom User model and admin panel (Start)
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from django.utils import timezone
from django.utils.translation import ugettext_lazy
from django.utils.translation import gettext_lazy as _


# Create your models here.
class MyCustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('The Username must be set'))
        email = email.lower()
        first_name = first_name.title()  # the first character in every word is upper case
        last_name = last_name.title()

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


# Create User model
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    username = models.CharField(max_length=55, unique=True)
    phone_number = models.CharField(max_length=55)

    email = models.EmailField(_('email address'), unique=True, null=False)
    is_staff = models.BooleanField(ugettext_lazy('staff status'), default=False,
                                   help_text=ugettext_lazy('Designates whether the user can log in this site'))
    is_active = models.BooleanField(ugettext_lazy('active'), default=True,
                                    help_text='Designates whether this user should be treated as active. Unselect '
                                              'this instead of deleting accounts')
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    objects = MyCustomUserManager()

    def __str__(self):
        return self.email

    # optional
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

# to create a custom User model and admin panel (End)
