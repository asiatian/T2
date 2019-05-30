from django.db import models

# Create your models here.
class TallerDeportivo(models.Model):
    nombre=models.CharField(max_length=60)
    dia= models.IntegerField()
    hora= models.IntegerField()
    talleres=models.Manager()

    def __str__(self):
        return "{}".format(self.nombre)
