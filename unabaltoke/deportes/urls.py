from django.conf.urls import url
from django.urls import path,include
from deportes import views

urlpatterns = [
    url(r'talleres/',views.TalleresView.as_view(),name='talleres'),
    url(r'taller/create/$',views.TallerCreate.as_view(success_url='/talleres/'),name="taller_create"),
    #path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),

]
