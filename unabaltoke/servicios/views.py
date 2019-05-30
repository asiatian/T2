from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Servicio, CrearPruebas
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,'index.html',context=None)

class HomeServiciosView(LoginRequiredMixin,TemplateView):
    def get(self,request,**kwargs):
        crearPruebas = CrearPruebas()
        return render(request, 'servicios.html',{'servicios': crearPruebas.obtenerServicios()})
