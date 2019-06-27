from django.shortcuts import render
from .models import *
import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from accounts.models import Profile
from accounts.forms import ProfileFormHora
# Create your views here.

class MostrarDiaA(TemplateView):
    def get(self,request,**kwargs):
        try:
            argsA = DiaA.dias.get(dia=datetime.datetime.now().date())
            argsF = DiaF.dias.get(dia=datetime.datetime.now().date())
            argsT = DiaT.dias.get(dia=datetime.datetime.now().date())
        except Exception as e:
            if not NumeroA.numeros.all():
                NumeroA.numeros.all().delete()
            print(e)
            argsA = DiaA(dia=datetime.datetime.now().date())
            argsA.save()
            argsF = DiaF(dia=datetime.datetime.now().date())
            argsF.save()
            argsT = DiaT(dia=datetime.datetime.now().date())
            argsT.save()
        #args = DiaA.dias.get(dia=datetime.datetime.now().date())
        #try:
        #    argumentoA = argsA.numeros.last()
        #except Exception as e:
        #    argumentoA = 0
        #    argA = 0
        argumentoA = argsA.numeros.last()
        if(argumentoA != None):
            argumentoA = argsA.numeros.last().id
        else:
            argumentoA = 0
        argumentoF = argsF.numeros.last()
        if(argumentoF != None):
            argumentoF = argsF.numeros.last().id
        else:
            argumentoF = 0
        argumentoT = argsT.numeros.last()
        if(argumentoT != None):
            argumentoT = argsT.numeros.last().id
        else:
            argumentoT = 0
        args = {"A":argumentoA,"F":argumentoF,"T":argumentoT}
        return render(request, 'horas.html',{"numeros":args})

class TomarHora(LoginRequiredMixin,CreateView):
    model = NumeroA
    template_name = './tomar_horaA.html'
    fields = []

    def form_valid(self,form):
        form.instance.estudiante = self.request.user
        dia = DiaA.dias.get(dia=datetime.datetime.now().date())
        form.instance.save()
        dia.numeros.add(form.instance)
        dia.save()
        self.request.user.profile.guardar(form.instance)
        return super(TomarHora,self).form_valid(form)
