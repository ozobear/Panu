from django.db import models

class Persona(models.Model):
	nombre = models.CharField(max_length=150)
	apellido = models.CharField(max_length=100)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=100)
	correo = models.EmailField()
	domicilio = models.TextField()
 
	def __str__(self):
		return '{} {}'.format(self.nombre. self.apellido) 