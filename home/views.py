from django.shortcuts import render

from users.models import MyUser

# Create your views here.


def home_page(request, user_id):
    user = MyUser.objects.get(pk=user_id)
    if not user.admin:
        return home_common_user(request, user)
    else:
        return home_admin_user(request, user)


def home_common_user(request, user):
    return render(
        request,
        "common_user/home.html",
        {
            "user_id": 1,
            "faculdade": "Faculdade 1",
            "curso": "teste",
            "vagas": "testevagas",
            "nota_posicao": "Nota: 976.23",
            "faculdade2": "Faculdade 2",
            "curso2": "teste2",
            "vagas2": "testevagas2",
            "nota_posicao2": "Nota: 976.23",
        },
    )


def home_admin_user(request, user):
    pass
