from django.db import models
from dueno.models import Persona

class Vacuna(models.Model):
	nombre = models.CharField(max_length=100)

class Mascota(models.Model):
	nombre = models.CharField(max_length=100)
	sexo = models.CharField(max_length=20)
	edad = models.IntegerField()
	fecha = models.DateTimeField()
	persona = models.ForeignKey(Persona, blank=True, null=True, on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna)

