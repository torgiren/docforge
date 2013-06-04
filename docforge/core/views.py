# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
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
		f.tresc = pickle.dumps(dane)
		f.nazwa = request.POST['nazwa']
		f.save()
		return render_to_response('formatka_list.html', {'post': dane})
	else:
		return render_to_response('formatka_add.html', RequestContext(request))

def formatka_list(request):
	f = Formatka.objects.all()
	return render_to_response('formatka_list.html', {'formatki': f})

def formatka_wpis(request, id):
	f = Formatka.objects.get(pk=id)
	pola = "<form>"
	for p in f.decode():
		typ = ""
		if p[1] == "tekst":
			typ = 'text'
		elif p[1] == 'data':
			typ = 'date'
		elif p[1] == 'numer':
			typ = 'number'
		pola += p[0]+": <input type='"+typ+"' name='"+ str(p[0]) + "'><br/>"
	pola += "<input type='submit' value='Zloz wniosek'>"
	pola += "</form>"
	return render_to_response('formatka_wpis.html', {'pola': pola})
