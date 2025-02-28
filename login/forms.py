from django import forms
from django.forms import (EmailInput, FloatField, ModelForm, PasswordInput,
                          TextInput)

from .models import Usuario


class FormSignup(ModelForm):
    class Meta:
        model = Usuario
        fields = ["nome", "email", "cpf", "nota", "senha"]
        labels = {"cpf": "CPF"}
        widgets = {
            "nome": TextInput(
                attrs={
                    "placeholder": "Digite seu nome",
                    "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
                }
            ),
            "email": EmailInput(
                attrs={
                    "placeholder": "Digite seu email",
                    "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
                }
            ),
            "cpf": TextInput(
                attrs={
                    "placeholder": "Digite seu CPF",
                    "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
                }
            ),
            "nota": TextInput(
                attrs={
                    "placeholder": "Digite sua nota no ENEM",
                    "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
                }
            ),
            "senha": PasswordInput(
                attrs={
                    "placeholder": "Crie sua senha",
                    "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
                    "required": True,
                }
            ),
        }


class FormLogin(forms.Form):
    CPF = forms.CharField(
        label="CPF",
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite seu CPF",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        ),
    )
    senha = forms.CharField(
        label="Senha",
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Crie sua senha",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        ),
    )


class FormChangePassword(forms.Form):
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
    senha = forms.CharField(
        label="Nova senha",
        max_length=30,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Nova senha",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        ),
    )
