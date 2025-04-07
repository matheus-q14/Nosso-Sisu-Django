from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import FormSignup
from .models import MyUser


class MyUserAdmin(UserAdmin):
    add_form = FormSignup
    model = MyUser
    list_display = ("email", "is_staff", "is_active", "admin", "cpf", "nome", "nota")
    list_filter = ("email", "is_staff", "is_active", "admin", "cpf", "nome", "nota")
    fieldsets = (
        (None, {"fields": ("email", "admin", "password", "nome", "cpf")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "cpf",
                    "nome",
                    "nota",
                    "password1",
                    "password2",
                    "is_staff",
                    "admin",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email", "cpf", "nome")
    ordering = ("email", "cpf", "nome")


admin.site.register(MyUser, MyUserAdmin)
