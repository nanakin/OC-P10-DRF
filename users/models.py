from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    # fields required for admin compliant permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.CharField(default="", max_length=80)

    username = models.CharField(max_length=150, unique=True, validators=[UnicodeUsernameValidator])
    can_be_contracted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    birth_date = models.DateField()
    created_time = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["birth_date"]  # for createsuperuser
