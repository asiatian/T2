from django import forms
from .models import ReservaMusculatura

class musculosForm(forms.Form):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
