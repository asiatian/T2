from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TallerDeportivo(models.Model):
    nombre=models.CharField(max_length=60)
    dia= models.IntegerField()
    hora= models.IntegerField()
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
    id= models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    dia = models.IntegerField(choices=DAY_CHOICES)
    bloque = models.IntegerField()
    reservas=models.Manager()

    def __str__(self):
        return "{}".format(self.nombre)
