from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import View
from .models import Sala
from .forms import postSala as salaForm
# Create your views here.
#
class SalaView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		print(Sala.salas.all())
		salitas = Sala.salas.all()
		if len(salitas)==0:
			return redirect('sala/create/')		
		else:
			return render(request, 'salas.html', {'salas': salitas})

#class SalaView(View):
#	def get(request):
#		return render(request, 'salas.html')



class SalaCreate(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		
		
		return render(request, 'sala_form.html')
	def post(self,request,**kwargs):
		print(request.POST)
		if request.method == 'POST':
			nueva_sala = salaForm(request.POST)
			if nueva_sala.is_valid():
				print("paso el post")
				sala = Sala()
				sala.nombre = nueva_sala["nombre"].value()
				sala.hora_inicio = nueva_sala["hora_inicio"].value()
				sala.hora_cierre = nueva_sala["hora_cierre"].value()
				sala.descripcion = nueva_sala["descripcion"].value()
				sala.save()
		return render(request, 'sala_form.html')


						