# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
# # Create your models here.
#
#
# class MyUser(AbstractUser):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         nome: models.CharField = models.CharField(max_length=50)
#         email: models.EmailField = models.EmailField(max_length=100, unique=True)
#         nota: models.DecimalField = models.DecimalField(max_digits=5, decimal_places=2)
#         cpf: models.CharField = models.CharField(max_length=11, unique=True)
#         admin: models.BooleanField = models.BooleanField(default=False)
#         is_active = models.BooleanField(default=True)
#
#         USERNAME_FIELD = "cpf"
#         REQUIRED_FIELDS = ["nome", "email", "nota"]
#
#     def __str__(self):
#         return self.nome
