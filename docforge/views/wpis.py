#*-* coding: utf8 *-*
from pyramid.view import view_config
from docforge.views.common import startwith


class WpisView(object):
    def __init__(self, request):
        self.request = request
        self.db = self.request.db['wpisy']

    def _add(self, post):
        pola = startwith(post, "pole_")
        items = {}
        print pola
        for i in pola:
            val = post[i]
            i = i.split("_", 2)
            if i[1] == "number":
                val = float(val)
            print i[2], "ma typ", i[1], "i wartosc", val
            items[i[2]] = val
        items['_formatka'] = post['_formatka']
        self.db.insert(items)
        return {}


    @view_config(route_name='wpis_add', renderer='string')
    def add(self):
        self._add(self.request.POST)
        return {}
