from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TallerDeportivo(models.Model):
    DAY_CHOICES = (
        ('Lunes','Lunes'),
        ('Martes','Martes'),
        ('Miercoles','Miercoles'),
        ('Jueves','Jueves'),
        ('Viernes','Viernes'),
        ('Sabado','Sabado')
    )
    nombre=models.CharField(max_length=60)
    dia= models.CharField(max_length=10,choices=DAY_CHOICES)
    hora= models.TimeField()
    icono = models.ImageField(upload_to='icons/%Y/%m/%d/',max_length= 255,null=True,blank=True)

    talleres=models.Manager()
    def __str__(self):
        return "{}".format(self.nombre)

class ReservaMusculatura(models.Model):
    DAY_CHOICES = (
        (1,'Lunes'),
        (2,'Martes'),
        (3,'Miercoles'),
        (4,'Jueves'),
        (5,'Viernes'),
        (6,'Sabado')
    )
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    dia = models.IntegerField(choices=DAY_CHOICES)
    Fecha = models.DateField(null=True)
    bloque = models.TimeField()
    reservas=models.Manager()

    def __str__(self):
        return "{}".format(self.id)
