from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

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
    elif(input == 6):
        return "Sabado"

class TalleresView(LoginRequiredMixin,TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'talleres.html',{'talleres': TallerDeportivo.talleres.all()})

class TallerCreate(LoginRequiredMixin,CreateView):
    model = TallerDeportivo
    template_name='./taller_form.html'
    fields='__all__'

class HorasView(LoginRequiredMixin,TemplateView):
    def get(self,request,**kwargs):
        current_user = request.user
        fixed = []
        args= ReservaMusculatura.reservas.all()
        for arg in args:
            #print(User.id)
            if(current_user==arg.estudiante):
                var = {"id":arg.id,"estudiante":arg.estudiante,"dia":dia(arg.dia),"bloque":arg.bloque}
                fixed.append(var)
        return render(request, 'salaM.html',{"reservas":fixed})


class DetalleHoraView(LoginRequiredMixin,TemplateView):
    def get(self,request, **kwargs):
        id=kwargs["pk"]
        arg = ReservaMusculatura.reservas.get(id=id)
        fixed = {"id":arg.id,"estudiante":arg.estudiante,"dia":dia(arg.dia),"fecha":arg.Fecha,"bloque":arg.bloque}
        return render(request, 'sala.html',{'reserva': fixed })


class TomarHora(LoginRequiredMixin,CreateView):
    model = ReservaMusculatura
    template_name = './salaM_form.html'
    fields = ['dia','Fecha','bloque']
    def form_valid(self,form):
        form.instance.estudiante = self.request.user
        return super(TomarHora,self).form_valid(form)


class BorrarHora(DeleteView):
    model = ReservaMusculatura
    template_name='./salaM_form.html'
    success_url = reverse_lazy('cursos')

class HoraUpdate(UpdateView):
    model = ReservaMusculatura
    template_name='./salaM_form.html'
    fields= ['dia','Fecha','bloque']
