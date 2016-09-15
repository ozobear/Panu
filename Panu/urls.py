from django.conf.urls import url, include 
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from social.apps.django_app import urls as socialUrls
from accounts import urls as accUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include(accUrls, namespace="accounts")),
    url(r'^registro/', include('registro.urls', namespace="registro")),
    url(r'^persona/', include('dueno.urls', namespace="dueño")),
    url('', include(socialUrls, namespace='social')),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),
]
