from django import forms
from .models import ReservaMusculatura

class MusculaturaForm(forms.ModelForm):
    class Meta:
        models = ReservaMusculatura
        fields = ('estudiante','dia','Fecha','bloque')
