from django import forms 
from .models import Mascota

class MascotaForm(forms.ModelForm):
	class Meta:
		model = Mascota
		fields = [
			'nombre',
			'sexo',
			'edad',
			'fecha',
			'persona',
			'medicina',
		]
		labels = {
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad': 'Edad',
			'fecha': 'Fecha',
			'persona': 'Humano',
			'medicina': 'Medicina',
		}
		widgets = {
			'nombre': forms.TextInput(),
			'sexo': forms.TextInput(),
			'edad': forms.TextInput(),
			'fecha': forms.TextInput(),
			'persona': forms.Select(),
			'medicina': forms.CheckboxSelectMultiple(),
		}