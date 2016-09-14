from django.conf.urls import url, include
from .views import index_dueno

urlpatterns = [
    url(r'^index$', index_dueno)
]