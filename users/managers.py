from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where cpf is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, cpf, nota, nome, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not cpf:
            raise ValueError(_("O CPF precisa ser digitado"))
        email = self.normalize_email(email)
        user = self.model(cpf=cpf, nota=nota, nome=nome, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, cpf, nota, nome, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(cpf, nota, nome, email, password, **extra_fields)
