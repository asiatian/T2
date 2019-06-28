from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from servicioAcademico.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.IntegerField(default=0)
    sede = models.CharField(max_length=30, blank=True, default="Antonio Varas")
    tipo = models.CharField(max_length= 10,blank=True, default = "Pregrado")
    horatomadaA = models.ForeignKey(NumeroA, blank=True, null=True , on_delete=models.CASCADE)
    horatomadaF = models.ForeignKey(NumeroF, blank=True, null=True , on_delete=models.CASCADE)
    horatomadaT = models.ForeignKey(NumeroT, blank=True, null=True , on_delete=models.CASCADE)

    def guardarA(self,instance,**kwargs):
        nuevo = self
        nuevo.horatomadaA = instance
        profile = super(Profile, nuevo).save()
        self.user.save()
        return profile

    def guardarF(self,instance,**kwargs):
        nuevo = self
        nuevo.horatomadaF = instance
        profile = super(Profile, nuevo).save()
        self.user.save()
        return profile

    def guardarT(self,instance,**kwargs):
        nuevo = self
        nuevo.horatomadaT = instance
        profile = super(Profile, nuevo).save()
        self.user.save()
        return profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if kwargs.get('created', False):
         Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_user_profile,sender=User)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()
