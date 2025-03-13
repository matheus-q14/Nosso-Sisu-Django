from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render

from users.forms import FormChangePassword, FormLogin, FormSignup
from users.models import MyUser

# from .forms import FormChangePassword


def login_page(request):
    if request.method == "GET":
        form = FormLogin()
        return render(request, "login/login_page.html", {"form": form})
    elif request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            user = form.clean()
            user_db = MyUser.objects.get(cpf=user.get("username"))
            login(request, user)
            return redirect("home_page", user_id=user_db.pk)
        response = "CPF ou senha incorreto, tente novamente"
        form_login = FormLogin()
        return render(
            request, "login/login_page.html", {"response": response, "form": form_login}
        )


def redefinir_senha(request):
    if request.method == "GET":
        form = FormChangePassword()
        return render(request, "login/change_password.html", {"form": form})
    elif request.method == "POST":
        form = FormChangePassword(request.POST)
        if form.is_valid:
            user = MyUser.objects.get(cpf=form["cpf"].value())
            print(user)
            form.clean(user)
            form.save(user)
            return redirect("login_page")
        # return redirect("signup_page")
        # if form.is_valid() and :
        #     nova_senha = form["senha"].value()
        #     user = MyUser.objects.get(cpf=form["cpf"].value())
        #     user.senha = make_password(nova_senha)
        #     user.save()
        #     return redirect("login_page")


def cadastrar_usuario(request):
    if request.method == "GET":
        form = FormSignup()
        return render(request, "signup/signup_page.html", {"form": form})
    elif request.method == "POST":
        form = FormSignup(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")


def login_redirect(request):
    return redirect("login_page")
