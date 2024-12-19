from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from auth_email.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class SensitiveData:
        include: list[str] = ["email", "password"]
        exclude: list[str] = [
            "last_login",
            "is_superuser",
            "is_active",
            "is_staff",
            "created",
            "changed_at",
        ]

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    changed_at = models.DateTimeField(auto_now=True, null=True, blank=True)
