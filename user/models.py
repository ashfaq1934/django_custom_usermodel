from email.policy import default
from enum import unique
from gettext import gettext
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError('Yo must provide an email')
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, 
                        first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(email, user_name, first_name, password, **other_fields)

class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext('email_address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    about = models.TextField(gettext('about'), blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self) -> str:
        return self.user_name