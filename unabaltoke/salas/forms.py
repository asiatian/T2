from django import forms
from .models import Sala

class postSala(forms.ModelForm):
	class Meta: 
		model = Sala
		fields = ['nombre', 'hora_inicio', 'hora_cierre', 'descripcion']