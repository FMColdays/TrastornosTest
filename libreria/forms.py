from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('correo', 'carrera', 'edad', 'instituto', 'sexo', 'semestre')
