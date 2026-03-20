from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'prioridad', 'completada']
        widgets = {
            # ✅ ahora es DateTimeField -> usar datetime-local
            'fecha_vencimiento': forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'prioridad': forms.Select(attrs={'class': 'form-select'}),
            'completada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ✅ Para que al EDITAR se precargue bien en el input datetime-local
        if self.instance and self.instance.pk and self.instance.fecha_vencimiento:
            self.initial['fecha_vencimiento'] = self.instance.fecha_vencimiento.strftime("%Y-%m-%dT%H:%M")


class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user