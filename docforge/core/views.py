# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import transaction
from models import *
import pickle

def index(request):
	return render_to_response('index.html')

def formatka_add(request):
	if request.method == "POST":
		f = Formatka()
		f.author = request.user
		n = [(i, request.POST[i]) for i in request.POST if "nazwa_" in i]
		t = [(i, request.POST[i]) for i in request.POST if "typ_" in i]
		n.sort()
		t.sort()
		n = [i[1] for i in n]
		t = [i[1] for i in t]
		dane = zip(n,t)
		f.nazwa = request.POST['nazwa']
		f.save()
		for d in dane:
			tmp = Pole()
			tmp.nazwa = d[0]
			tmp.typ = Typ.objects.get(nazwa=d[1])
			tmp.formatka = f
			tmp.save()
		return render_to_response('formatka_list.html', {'post': dane})
	else:
		return render_to_response('formatka_add.html', RequestContext(request))

def formatka_list(request):
	f = Formatka.objects.all()
	return render_to_response('formatka_list.html', {'formatki': f})

@transaction.commit_on_success
def formatka_wpis(request, id):
	if request.method == "POST":
		wniosek = Wniosek()
		wniosek.formatka = Formatka.objects.get(id=int(request.POST['formatka']))
		wniosek.wnioskodawca = request.user
		wniosek.save()
		pola = Pole.objects.filter(formatka=int(request.POST['formatka']))
		for i,j in request.POST.items():
			tmp = pola.filter(nazwa=i)
			if tmp:
				tmp = tmp[0]
				w = Wpis()
				w.pole = tmp
				w.wniosek = wniosek
				w.tekst_short = j
				w.save()
		return render_to_response('index.html')
	else:
		f = Formatka.objects.get(pk=id)
		pola = Pole.objects.filter(formatka=f)	
		wynik = "<input type='hidden' name='formatka' value='" + str(f.id) +"'>"
		for p in pola:
			wynik += p.nazwa+": <input type='"+p.typ.widget+"' name='"+ str(p.nazwa) + "'><br/>"
		return render_to_response('formatka_wpis.html', {'pola': wynik}, RequestContext(request))
