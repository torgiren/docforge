from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import pickle

# Create your models here.


class Formatka(models.Model):
	author = models.ForeignKey(User)
	data = models.DateTimeField(auto_now_add=True)
	tresc = models.TextField()
	nazwa = models.CharField(max_length=255)

	def decode(self):
		return pickle.loads(str(self.tresc))

class FormatkaAdmin(admin.ModelAdmin):
	list_display = ('nazwa', 'author', 'decode', 'data')
	pass


class Wpis(models.Model):
	formatka = models.ForeignKey(Formatka)
	user = models.ForeignKey(User)
	data = models.DateTimeField(auto_now_add=True)
	tresc = models.TextField()
	ip = models.CharField(max_length=20)

admin.site.register(Formatka, FormatkaAdmin)
admin.site.register(Wpis)
