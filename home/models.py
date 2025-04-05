from django.db import models

from users.models import MyUser

# Create your models here.


class Cursos(models.Model):
    faculdade: models.CharField = models.CharField(max_length=200, default="")
    curso: models.CharField = models.CharField(max_length=200, default="")
    numero_vagas: models.IntegerField = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.curso} - {self.faculdade.split('-')[1]}"


class CursoUsuario(models.Model):
    user: models.ForeignKey = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, blank=True
    )
    curso: models.ForeignKey = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def get_faculdade(self):
        return self.curso.faculdade

    def get_curso(self):
        return self.curso.curso

    def get_numero_vagas(self):
        return self.curso.numero_vagas

    def get_nota_user(self):
        return float(self.user.nota)

    def __str__(self):
        return f"{self.user} - {self.curso}"
