from django.db import models

# Create your models here.

class Sala(models.Model):
	nombre = models.CharField(max_length=60)
	hora_inicio = models.IntegerField()
	hora_cierre = models.IntegerField()
	descripcion = models.CharField(max_length=300)
	salas = models.Manager()

	def __str__(self):
		return "{}".format(self.nombre)


