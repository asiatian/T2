from django.shortcuts import render
from django.views.generic import TemplateView
from .models import TallerDeportivo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

# Create your views here.

class TalleresView(LoginRequiredMixin,TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'talleres.html',{'talleres': TallerDeportivo.talleres.all()})

class TallerCreate(CreateView):
    model = TallerDeportivo
    template_name='./taller_form.html'
    fields='__all__'
