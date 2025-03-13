from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_redirect, name="login_redirect"),
    path("account/login/", views.login_page, name="login_page"),
    path("redefinir-senha/", views.redefinir_senha, name="redefinir_senha"),
    path("account/signup", views.cadastrar_usuario, name="cadastrar_usuario"),
]
