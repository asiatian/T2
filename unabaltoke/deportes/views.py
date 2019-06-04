from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from .models import TallerDeportivo, ReservaMusculatura

# Create your views here.

def dia(input):
    if(input == 1):
        return "Lunes"
    elif(input == 2):
        return "Martes"
    elif(input == 3):
        return "Miercoles"
    elif(input == 4):
        return "Jueves"
    elif(input == 5):
        return "Viernes"

class TalleresView(LoginRequiredMixin,TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'talleres.html',{'talleres': TallerDeportivo.talleres.all()})

class TallerCreate(LoginRequiredMixin,CreateView):
    model = TallerDeportivo
    template_name='./taller_form.html'
    fields='__all__'

class HorasView(LoginRequiredMixin,TemplateView):
    def get(self,request,**kwargs):
        fixed = []
        args= {'reservas': ReservaMusculatura.reservas.all()}
        #for arg in args:
        #    var = [arg.nombre,dia(arg.dia),arg.hora]
        #    fixed.append(var)
        return render(request, 'salaM.html',args)

class TomarHora(CreateView):
    model = ReservaMusculatura
    template_name='./salaM_form.html'
    fields='__all__'

class BorrarHora(DeleteView):
    model = ReservaMusculatura
    template_name='./curso_form.html'
    success_url = reverse_lazy('cursos')
