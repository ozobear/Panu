from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from . import views 

urlpatterns = [
	url(r'^registro/$', views.Registration.as_view(), name="registro"),
	url(r'^profile/$', views.ProfileView.as_view(), name="profile"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout, name="logout"),
]