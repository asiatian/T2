
from django import forms
from django.forms import ModelForm

from .models import ReservaMusculatura


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'

class ReservaForm(ModelForm):
    class Meta:
        model = ReservaMusculatura
        fields = ['dia', 'Fecha', 'bloque']
        widgets = {
            'Fecha': DateInput(),
            'bloque': TimeInput(),
        }
