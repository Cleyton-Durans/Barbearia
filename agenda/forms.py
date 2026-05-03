from django import forms
from .models import Espera

class EsperaForm(forms.ModelForm):
    class Meta:
        model = Espera
        fields = ['nome', 'servico']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'servico': forms.Select(attrs={'class': 'form-control'}),   
        }
