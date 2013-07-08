#*-* coding: utf8 *-*
from pyramid.view import view_config
from docforge.views.common import startwith
import bson

from docforge.errors import *

class FormatkiView(object):
    def __init__(self, request):
        self.request = request
        self.db = self.request.db['formatki']

    def _list(self):
        return self.db.find()

    def _add(self, name, zipped):
        obj = {}
        obj['_nazwa'] = name
        for z in zipped:
            obj[z[0]] = z[1]
        self.db.insert(obj)

    def _merge_field(self, post):
        """Wyciąga ze słownika post pola "nazwa_" oraz "typ",
        a następnie tworzy z nich listę krotek"""
        nazwy = startwith(post, "nazwa_")
        typy = startwith(post, "typ_")
        if len(nazwy) != len(typy):
            raise LengthMismachException
        nazwy.sort()
        typy.sort()
        nazwy = [post[i] for i in nazwy]
        typy = [post[i] for i in typy]
        return zip(nazwy, typy)

    def _get(self, id):
        return self.db.find_one({'_id': bson.ObjectId(id)})

    def _get_widget(self, id):
        print id
        print self.request.db['typy'].find_one({'_id': bson.ObjectId(id)})
        return self.request.db['typy'].find_one({'_id': bson.ObjectId(id)})['widget']

    @view_config(route_name='formatki_list', renderer='docforge:templates/list.jinja2')
    def list(self):
        items = [{'verbose': i['_nazwa'], 'href': self.request.route_path('formatki_fill_form', id=i['_id'])} for i in self._list()]
        return {'items': items, 'title': u'Lista dostępnych formularzy'}

    @view_config(route_name='formatki_add_form', renderer='docforge:templates/formatki_form.jinja2')
    def show_form(self):
        return {}

    @view_config(route_name='formatki_add_do', renderer='string')
    def add_form(self):
        if not self.request.POST.get('_nazwa'):
            raise NoFormNameFoundException
        zipped = self._merge_field(self.request.POST)
        self._add(self.request.POST['_nazwa'], zipped)
        return self.request.POST

    @view_config(route_name='formatki_fill_form', renderer='docforge:templates/formatki_fill.jinja2')
#    @view_config(route_name='formatki_fill_form', renderer='string')
    def fill_form(self):
        id=self.request.matchdict['id']
        obj = self._get(id)
        nazwa = obj['_nazwa']
        del(obj['_nazwa'])
        del(obj['_id'])
        items = [{'nazwa': i, 'widget': self._get_widget(j)} for (i,j) in obj.items()]
        return {'nazwa': nazwa, 'items': items}
