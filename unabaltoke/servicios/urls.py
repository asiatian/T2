from django.conf.urls import url
from django.urls import path,include
from servicios import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name='index'),
    url(r'servicios/',views.HomeServiciosView.as_view(),name='servicios'),
    #path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),

]
