from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=25)
