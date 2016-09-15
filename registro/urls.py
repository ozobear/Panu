from django.conf.urls import url, include
from .views import index, mascota_view, mascota_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', mascota_view, name='mascota_crear'),
    url(r'^lista$', mascota_list, name='mascota_listar'),
]