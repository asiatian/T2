from django.conf.urls import url
from django.urls import path,include,re_path
from deportes import views

urlpatterns = [
    url(r'talleres/',views.TalleresView.as_view(),name='talleres'),
    url(r'taller/create/$',views.TallerCreate.as_view(success_url='/talleres/'),name="taller_create"),
    url(r'salaM/',views.HorasView.as_view()),
    url(r'sala/TomarHora/$',views.TomarHora.as_view(success_url='/salaM/'),name="tomar_hora"),
    url(r'sala/(?P<pk>\d+)/update/$',views.HoraUpdate.as_view(success_url='/salaM/'),name="reserva_update"),
    url(r'sala/(?P<pk>\d+)/delete/$',views.BorrarHora.as_view(success_url='/salaM/'),name="reserva_delete"),
    re_path(r'sala/(?P<pk>\d+)/', views.DetalleHoraView.as_view(),name="detalle"),
    #url(r'SalaM/TomarHora/(?[0-9]4)',views.TomarHora.as_view(success_url='/SalaM/'),name="tomar_hora"),
    #path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),

]
