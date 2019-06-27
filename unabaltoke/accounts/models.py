from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from servicioAcademico.models import NumeroA

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.IntegerField(default=0)
    sede = models.CharField(max_length=30, blank=True, default="Antonio Varas")
    tipo = models.CharField(max_length= 10,blank=True, default = "Pregrado")
    horatomada = models.ForeignKey(NumeroA, blank=True, null=True , on_delete=models.CASCADE)

    def definirHoraServicio(self, instance,**kwargs):
        self.horatomada=instance
        self.horatomada.save()
        print(self.horatomada)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if kwargs.get('created', False):
         Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_user_profile,sender=User)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created,**kwargs):
    if created:
        instance.profile.save()
