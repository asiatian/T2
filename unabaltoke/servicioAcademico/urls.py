from django.conf.urls import url
from django.urls import path,include,re_path
from servicioAcademico import views

urlpatterns = [
    url(r'serviciosAcademicos/',views.MostrarDiaA.as_view(),name='servicios'),
    url(r'servicioAcademico/TomaA/',views.TomarHoraA.as_view(success_url='/serviciosAcademicos/'),name='TomaA'),
    url(r'servicioAcademico/TomaF/',views.TomarHoraF.as_view(success_url='/serviciosAcademicos/'),name='TomaF'),
    url(r'servicioAcademico/TomaT/',views.TomarHoraT.as_view(success_url='/serviciosAcademicos/'),name='TomaT'),
]
