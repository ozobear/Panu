from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	phone = models.CharField(max_length=10, blank=True, null=True)
	age = models.IntegerField(blank=True, null=True)
	residence = models.TextField(blank=True, null=True)
	photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)


	class Meta:
		ordering = ('user',)

	def __str__(self):
		return 'Info del dueño {}'.format(self.user.username)