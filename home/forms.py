from django import forms

from .models import Cursos, CursoUsuario


class ChooseCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["curso"].widget.attrs.update(
            {
                "class": "text-wrap text-black",
            }
        )
        self.fields["user"].widget.attrs.update({"class": "hidden"})

    class Meta:
        model = CursoUsuario
        fields = ["user", "curso"]
        labels = {"user": ""}


class CreateCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["faculdade"].widget.attrs.update(
            {
                "placeholder": "Digite o nome da faculdade no padrão: 'Faculdade - Sigla'",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )
        self.fields["curso"].widget.attrs.update(
            {
                "placeholder": "Digite o nome do curso",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )
        self.fields["numero_vagas"].widget.attrs.update(
            {
                "placeholder": "Digite o número de vagas do curso",
                "class": "border text-sm rounded-lg block w-full p-2.5 bg-gray-700 border-gray-600 placeholder-gray-400 text-white focus:ring-blue-500 focus:border-blue-500",
            }
        )

    class Meta:
        model = Cursos
        fields = ["faculdade", "curso", "numero_vagas"]
        labels = {
            "faculdade": "Faculdade",
            "curso": "Curso",
            "numero_vagas": "Número de vagas",
        }
