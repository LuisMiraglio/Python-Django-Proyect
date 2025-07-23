from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'prioridad', 'completada']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
            'prioridad': forms.Select(attrs={'class': 'form-select'}),
            'completada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
