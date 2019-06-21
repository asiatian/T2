from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Servicio, CrearPruebas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from accounts.models import Profile
# Create your views here.

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        if(request.user.is_anonymous != True):
            try:
                profile = request.user.profile
            except Profile.DoesNotExist:
                profile = Profile(user=request.user)
                profile.save()
        return render(request,'index.html',context=None)

class HomeServiciosView(LoginRequiredMixin,TemplateView):
    def get(self,request,**kwargs):
        crearPruebas = CrearPruebas()
        return render(request, 'servicios.html',{'servicios': crearPruebas.obtenerServicios()})
