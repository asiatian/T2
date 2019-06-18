from django.shortcuts import render
from .models import DiaA,NumeroA
import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
# Create your views here.

class MostrarDiaA(TemplateView):
    def get(self,request,**kwargs):
        try:
            args = DiaA.dias.get(dia=datetime.datetime.now().date())
        except Exception as e:
            print(e)
            print(datetime.datetime.now().date())
            args = DiaA(dia=datetime.datetime.now().date(),numeros=null)
        #args = DiaA.dias.get(dia=datetime.datetime.now().date())
        argumento = args.numeros.last()
        if(argumento == None):
            cero = 0;
            return render(request,'horas.html',{"numero":cero})
        return render(request, 'horas.html',{"numero":args.numeros.last().id})

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
        return super(TomarHora,self).form_valid(form)
