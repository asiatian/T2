from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class NumeroA(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante =  models.ForeignKey(User, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    numeros =  models.Manager()

class DiaA(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.DateField(null=True)
    numeros = models.ManyToManyField(NumeroA,blank=True,related_name="lista_numeros")
    actual = models.ForeignKey(NumeroA,blank=True,null=True,on_delete=models.SET_NULL)
    dias = models.Manager()

@receiver(post_save, sender=User)
def crearDia(sender, instance, created, **kwargs):
    if created:
        DiaA.objects.create(dia=instance)
