from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import UserManager


class MyUser(AbstractBaseUser, PermissionsMixin):
    nome: models.CharField = models.CharField(max_length=50)
    email: models.EmailField = models.EmailField(max_length=100, unique=True)
    nota: models.DecimalField = models.DecimalField(max_digits=5, decimal_places=2)
    cpf: models.CharField = models.CharField(max_length=11, unique=True)
    admin: models.BooleanField = models.BooleanField(default=False)
    is_active: models.BooleanField = models.BooleanField(default=True)
    is_staff: models.BooleanField = models.BooleanField(default=False)
    date_joined: models.DateTimeField = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["nome", "email", "nota"]

    objects = UserManager()

    def __str__(self):
        return self.nome
