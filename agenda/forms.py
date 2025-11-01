from django import forms
from .models import Espera

class EsperaForm(forms.ModelForm):
    class Meta:
        model = Espera
        fields = ['nome', 'servico', 'data', 'hora']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }
