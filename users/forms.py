from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import (
    AuthenticationForm,
    SetPasswordMixin,
    UserCreationForm,
)
from django.core.exceptions import ValidationError

from .models import MyUser


class FormSignup(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages["password_mismatch"] = (
            "A senha não é a mesma nos dois campos"
        )
        self.fields["nome"].widget.attrs.update(
            {
                "placeholder": "Digite seu nome",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )
        self.fields["email"].widget.attrs.update(
            {
                "placeholder": "Digite seu email",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )
        self.fields["cpf"].widget.attrs.update(
            {
                "placeholder": "Digite seu CPF",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )
        self.fields["nota"].widget.attrs.update(
            {
                "placeholder": "Digite sua nota no ENEM",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                "placeholder": "Crie sua senha",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
                "required": True,
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                "placeholder": "Confirme sua senha",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
                "required": True,
            }
        )

    class Meta:
        model = MyUser
        fields = ("nome", "email", "cpf", "nota", "password1", "password2")
        labels = {"cpf": "CPF", "password1": "Senha", "password2": "Confirme sua senha"}

        def clean_password2(self):
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError(
                    self.error_messages["password_mismatch"],
                    code="password_mismatch",
                )
            return password2

        def save(self, commit=True):
            user = super(FormSignup, self).save(commit=False)
            user.set_password(self.clean_password2())
            if commit:
                user.save()
            return user


class FormLogin(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(AuthenticationForm, self).__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {
                "placeholder": "Digite seu CPF",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )
        self.fields["password"].widget.attrs.update(
            {
                "placeholder": "Crie sua senha",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )

        self.request = request
        self.user_cache = None

        # Set the label for the "username" field.
        UserModel = MyUser
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        self.fields["username"].label = "CPF"


class FormChangePassword(SetPasswordMixin, forms.Form):

    cpf = forms.CharField(
        label="CPF",
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite seu CPF",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.new_password1, self.new_password2 = (
            SetPasswordMixin.create_password_fields(
                label1="Nova senha", label2="Confirme a nova senha"
            )
        )
        self.new_password1.widget.attrs.update(
            {
                "placeholder": "Nova senha",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )
        self.new_password2.widget.attrs.update(
            {
                "placeholder": "Confirme a nova senha",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )

    field_order = ["cpf", "password1", "password2"]

    # self.fields["cpf"] = forms.CharField(label="CPF", max_length=11)
    # self.fields["cpf"].widget.attrs.update(
    #     {
    #         "placeholder": "Digite seu CPF",
    #         "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
    #     }
    # )
    # self.fields["new_password1"].label = "Nova senha"
    # self.fields["new_password2"].label = "Confirme a nova senha"
    #

    def validate_passwords(
        self,
        password1_field_name="password1",
        password2_field_name="password2",
    ):
        password1 = password1_field_name.value()
        password2 = password2_field_name.value()

        print(f"pass1 {password1}")
        print(f"pass2 {password2}")

        if password1 and password2 and password1 != password2:
            error = ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
            # self.add_error(password2_field_name, error)

    def validate_password_for_user(self, user, password_field_name="password2"):
        password = password_field_name
        print(f"validate pass {password}")
        if password:
            try:
                password_validation.validate_password(password, user)
            except ValidationError as error:
                self.add_error(password_field_name, error)

    def set_password_and_save(self, user, password_field_name="password1", commit=True):
        print(password_field_name)
        user.set_password(password_field_name)
        if commit:
            user.save()
        return user

    def clean(self, user):
        self.validate_passwords(self.new_password1, self.new_password2)
        self.validate_password_for_user(user, "new_password2")
        # return super().clean()

    def save(self, user, commit=True):
        return self.set_password_and_save(user, "new_password1", commit=commit)
