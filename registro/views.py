from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MascotaForm
from .models import Mascota 

def index(request):
	return render(request, 'index.html')

def mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('registro:index')
	else:
		form = MascotaForm()

	return render(request, 'mascota_form.html', {'form':form}) 

def mascota_list(request):
	mascota = Mascota.objects.all()
	contexto = {'mascotas':mascota}
	return render(request, 'mascota_list.html', contexto)
