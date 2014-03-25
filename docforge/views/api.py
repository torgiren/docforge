#*-* coding: utf8 *-*
from pyramid.view import view_config


class ApiView(object):
    def __init__(self, request):
        self.request = request
        self.db = self.request.db['formatki']

    @view_config(route_name='zapisz_template', renderer='string')
    def zapisz_template(self):
        wynik = {}
        dane = self.request.POST.mixed()
        wynik['nazwa'] = dane['nazwa']
        wynik['template'] = dane['template'].replace("&gt",  '>').replace("&lt",'<')
        wynik['pola'] = []
        for i in dane['pola[]']:
#            {j.split('=')[0]: j.split('=')[1] for j in i.split('&')}
            wynik['pola'].append({j.split('=')[0]: j.split('=')[1] for j in i.split('&')})
        print wynik
        print self.db
        print self.db.insert(wynik)
        for i in self.db.find():
            print i
        print "Koniec"
        return "Zapisuje"

