#*-* coding: utf8 *-*
from pyramid.view import view_config
from docforge.views.common import startwith

from docforge.errors import *

class FormatkiView(object):
    def __init__(self, request):
        self.request = request
        self.db = self.request.db['formatki']

    def _list(self):
        return db.find()

    def _add(self, name, zipped):
        obj = {}
        obj['nazwa'] = name
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
        return zip(nazwy, typy)

    @view_config(route_name='formatki_list', renderer='docforge:templates/list.jinja2')
    def list(self):
        return {'items': self._list()}

    @view_config(route_name='formatki_add_form', renderer='docforge:templates/formatki_form.jinja2')
    def show_form(self):
        return {}

    @view_config(route_name='formatki_add_do', renderer='string')
    def add_form(self):
        if not self.request.POST.haskey('nazwa'):
            raise NoFormNameFoundException
        zipped = self._merge_field(self.request.POST)
        self._add(self.request.POST['nazwa'], zipped)
        return self.request.POST
