from django import forms

from .models import CursoUsuario


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
