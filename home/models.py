from django.db import models

from users.models import MyUser

# Create your models here.


class Cursos(models.Model):
    nome: models.CharField = models.CharField(max_length=100)


class CursoUsuario(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
