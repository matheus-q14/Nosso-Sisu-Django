from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import redirect, render

from .forms import FormChangePassword, FormLogin, FormSignup
from .models import Usuario

# Create your views here.


def login_page(request):
    if request.method == "GET":
        form = FormLogin()
        return render(request, "login/login_page.html", {"form": form})
    elif request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            cpf = form["CPF"].value()
            senha_input = form["senha"].value()
            senha_db = Usuario.objects.get(cpf=cpf).senha
            if check_password(senha_input, senha_db):
                print("Correto")
                return render(request, "home")
            else:
                response = "Senha ou CPF incorreto, tente novamente"
                return render(
                    request,
                    "login/login_page.html",
                    {"response": response, "form": form},
                )


def redefinir_senha(request):
    if request.method == "GET":
        form = FormChangePassword()
        return render(request, "login/change_password.html", {"form": form})
    elif request.method == "POST":
        form = FormChangePassword(request.POST)
        if form.is_valid() and Usuario.objects.get(cpf=form['cpf'].value()):
            nova_senha = form['senha'].value()
            user = Usuario.objects.get(cpf=form['cpf'].value())
            user.senha = make_password(nova_senha)
            user.save()
            return redirect('login_page')


def cadastrar_usuario(request):
    if request.method == "GET":
        form = FormSignup()
        return render(request, "signup/signup_page.html", {"form": form})
    elif request.method == "POST":
        form = FormSignup(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.senha = make_password(formulario.senha)
            formulario = form.save()
            return redirect("login_page")
