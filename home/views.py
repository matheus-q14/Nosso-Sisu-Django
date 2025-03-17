from django.shortcuts import render

from users.models import MyUser

from .models import Cursos, CursoUsuario

# Create your views here.


def home_page(request, user_id):
    user = MyUser.objects.get(pk=user_id)
    if not user.admin:
        return home_common_user(request, user)
    else:
        return home_admin_user(request, user)


def home_common_user(request, user):
    cursos = CursoUsuario.objects.filter(user=user)
    curso1 = cursos[0]
    curso2 = cursos[1]
    posicao1 = calcular_posicao(Cursos.objects.get(curso=curso1.get_curso()), user.nota)
    posicao2 = calcular_posicao(Cursos.objects.get(curso=curso2.get_curso()), user.nota)
    context = {
        "user_id": user.pk,
        "faculdade": curso1.get_faculdade(),
        "curso": curso1.get_curso(),
        "vagas": curso1.get_numero_vagas(),
        "nota_posicao": posicao1,
        "faculdade2": curso2.get_faculdade(),
        "curso2": curso2.get_curso(),
        "vagas2": curso2.get_numero_vagas(),
        "nota_posicao2": posicao2,
    }
    return render(
        request,
        "common_user/home.html",
        context,
    )


def calcular_posicao(curso, nota):
    notas_gerais = {float(nota)}
    for curso in CursoUsuario.objects.filter(curso=curso):
        notas_gerais.add(curso.get_nota_user())
    notas_ordenadas = sorted(notas_gerais, reverse=True)
    return f"Nota: {nota}. Posição {notas_ordenadas.index(float(nota)) + 1} de {curso.get_numero_vagas()} vagas"


def home_admin_user(request, user):
    pass
