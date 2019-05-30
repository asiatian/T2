from django.db import models

# Create your models here.
class Servicio:
    def __init__(self,area,nombre):
        self.nombre = nombre
        self.area= area

class CrearPruebas:
    def __init__(self):
        self.servicios=[]
        self.servicios.append(Servicio("Biblioteca","Boxes"))
        self.servicios.append(Servicio("Servicios Academicos","sacar numero"))
        self.servicios.append(Servicio("Gimnacio","Sala Musculatura"))

    def obtenerServicios(self):
        return self.servicios
