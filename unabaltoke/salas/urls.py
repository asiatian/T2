from django.conf.urls import url
from django.urls import path,include
from salas import views

urlpatterns = [
   path('salas/',views.SalaView.as_view(),name='salas'),
   url(r'sala/create/$',views.SalaCreate.as_view(), name='sala_create'),
   path('accounts/',include('django.contrib.auth.urls')),

]
#urlpatterns = [
#	path('salas/', views.SalaView.get, name='salas' )
#

#]