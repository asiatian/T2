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
    numeros = models.ManyToManyField(NumeroA,blank=True,related_name="lista_numerosA")
    actual = models.ForeignKey(NumeroA,blank=True,null=True,on_delete=models.SET_NULL)
    dias = models.Manager()

class NumeroF(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante =  models.ForeignKey(User, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    numeros =  models.Manager()

class DiaF(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.DateField(null=True)
    numeros = models.ManyToManyField(NumeroF,blank=True,related_name="lista_numerosF")
    actual = models.ForeignKey(NumeroF,blank=True,null=True,on_delete=models.SET_NULL)
    dias = models.Manager()

class NumeroT(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante =  models.ForeignKey(User, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    numeros =  models.Manager()

class DiaT(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.DateField(null=True)
    numeros = models.ManyToManyField(NumeroT,blank=True,related_name="lista_numerosT")
    actual = models.ForeignKey(NumeroT,blank=True,null=True,on_delete=models.SET_NULL)
    dias = models.Manager()

#@receiver(post_save, sender=User)
def crearDiaA(sender, instance, created, **kwargs):
    if created:
        DiaA.objects.create(dia=instance)
