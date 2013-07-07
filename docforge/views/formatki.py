#*-* coding: utf8 *-*
from pyramid.view import view_config
from docforge.views.common import startwith

from docforge.errors import *

class FormatkiView(object):
    def __init__(self, request):
        self.request = request

    def __list(self):
        db = self.request.db['formatki']
        return db.find()

    def __add(self):
        pass

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
        return {'items': self.__list()}

    @view_config(route_name='formatki_add_form', renderer='docforge:templates/formatki_form.jinja2')
    def show_form(self):
        return {}

    @view_config(route_name='formatki_add_do', renderer='string')
    def add_form(self):
        db = self.request.db['formatki']
        #TODO Check for POST
        print self.request.POST

        return self.request.POST
