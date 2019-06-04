from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.update_profile, name='profile')
]
