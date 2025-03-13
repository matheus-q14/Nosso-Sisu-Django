from django import forms


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
