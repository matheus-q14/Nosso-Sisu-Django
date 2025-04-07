from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ChooseCourseForm, CreateCourseForm
from .models import Cursos, CursoUsuario

# Create your views here.


def home_page(request, user_id):
    if not request.user.admin:
        return home_common_user(request)
    else:
        return home_admin_user(request)


def home_common_user(request):
    user = request.user
    form = ChooseCourseForm()
    cursos = CursoUsuario.objects.filter(user=user)
    context = {
        "user_id": user.pk,
        "form": form,
    }
    if cursos:
        for i in range(0, len(cursos)):
            curso = cursos[i]
            posicao = calcular_posicao(
                Cursos.objects.get(
                    curso=curso.get_curso(), faculdade=curso.get_faculdade()
                ),
                user.nota,
            )
            curso_atual = {
                f"curso{i+1}": {
                    "faculdade": curso.get_faculdade(),
                    "curso": curso.get_curso(),
                    "vagas": f"{curso.get_numero_vagas()} vagas",
                    "nota_posicao": posicao,
                },
            }
            context.update(curso_atual)

    return render(
        request,
        "common_user/home.html",
        context,
    )


@login_required
def process_course_choice(request, user_id):
    if request.method == "POST":
        form = ChooseCourseForm(request.POST)
        if form.is_valid():
            user = request.user
            cursos = CursoUsuario.objects.filter(user=user)
            curso = form.save(commit=False)
            curso.user = user
            if len(cursos) >= 2:
                curso_selecionado = int(request.POST["curso_alterado"])
                match curso_selecionado:
                    case 1:
                        cursos[0].curso = curso.curso
                        cursos[0].save()
                    case 2:
                        cursos[1].curso = curso.curso
                        cursos[1].save()
            else:
                curso.save()
            return redirect("home_page", user_id=user_id)
    else:
        response = HttpResponse()
        response.status_code = 405
        return response


def calcular_posicao(curso, nota):
    notas_gerais = {float(nota)}
    for curso in CursoUsuario.objects.filter(curso=curso):
        notas_gerais.add(curso.get_nota_user())
    notas_ordenadas = sorted(notas_gerais, reverse=True)
    return f"Nota: {nota}. Posição {notas_ordenadas.index(float(nota)) + 1} de {curso.get_numero_vagas()} vagas"


def home_admin_user(request):
    if request.method == "GET":
        form = CreateCourseForm()
        context = {"user_id": request.user.pk, "form": form}
        return render(request, "admin_user/home_admin.html", context)


def create_course(request):
    if request.method == "POST":
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save()
            context = {"user_id": request.user.pk}
            return render(request, "admin_user/succes_page.html", context)


def logout_user(request):
    logout(request)
    return redirect("login_page")
