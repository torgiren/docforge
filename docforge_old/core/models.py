from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import pickle

# Create your models here.
class Typ(models.Model):
	nazwa = models.CharField(max_length=255)
	widget = models.CharField(max_length=255)

	def __str__(self):
		return self.nazwa


class Formatka(models.Model):
	author = models.ForeignKey(User)
	data = models.DateTimeField(auto_now_add=True)
	nazwa = models.CharField(max_length=255)

	def __str__(self):
		return self.nazwa

class Pole(models.Model):
	nazwa = models.CharField(max_length=255)
	typ = models.ForeignKey(Typ)
	formatka = models.ForeignKey(Formatka)

	def __str__(self):
		return self.nazwa

class Wniosek(models.Model):
	wnioskodawca = models.ForeignKey(User)
	formatka = models.ForeignKey(Formatka)

class Wpis(models.Model):
	pole = models.ForeignKey(Pole)
	tekst_short = models.CharField(max_length=255, blank=True, null=True)
	liczba = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	tekst_long = models.TextField(blank=True, null=True)
	wniosek = models.ForeignKey(Wniosek)


admin.site.register(Formatka)
admin.site.register(Wpis)
admin.site.register(Pole)
admin.site.register(Typ)
admin.site.register(Wniosek)
