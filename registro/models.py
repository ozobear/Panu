from django.db import models
from dueno.models import Persona

class Medicina(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return '{} '.format(self.nombre) 

class Mascota(models.Model):
	nombre = models.CharField(max_length=100)
	sexo = models.CharField(max_length=20)
	edad = models.IntegerField()
	fecha = models.DateField()
	persona = models.ForeignKey(Persona, blank=True, null=True, on_delete=models.CASCADE)
	medicina = models.ManyToManyField(Medicina)