from django.db import models
from django.conf import settings

class Persona(models.Model):
	nombre = models.CharField(max_length=150)
	apellido = models.CharField(max_length=100)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=100)
	correo = models.EmailField()
	domicilio = models.TextField()
