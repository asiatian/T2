from django import forms
from .models import ReservaMusculatura

class MusculaturaForm(forms.Form):
    model= ReservaMusculatura
    CHOICES = (('1', 'Lunes'),('2', 'Martes'),('3', 'Miercoles'),('4', 'Jueves'),('5', 'Viernes'),('6', 'Sabado'))
    dias = forms.ChoiceField(choices=CHOICES)
