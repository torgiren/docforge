#*-* coding: utf8 *-*
from pyramid.view import view_config
from docforge.views.common import startwith
from docforge.views.formatki import FormatkiView
from bson import objectid


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

    def _list(self, id=None, sort=None, rev=None):
        if id:
            warunek = {'_formatka': id}
        else:
            warunek = None
        print "Warunek: ", warunek
        objs = list(self.db.find(warunek, {'_formatka': 0, '_id': 0}))
        if sort:
            objs.sort(cmp=lambda x,y: cmp(x[sort], y[sort]))
        if rev:
            objs.reverse()
        print objs
#        del(objs['_formatka'])
#        del(objs['_id'])
        return objs

    @view_config(route_name='wpis_add', renderer='string')
    def add(self):
        self._add(self.request.POST)
        return {}

    @view_config(route_name='wpis_list', renderer='docforge:templates/list.jinja2')
    def list(self):
        tmp = FormatkiView(self.request)
        items = [{'verbose': unicode(i['_nazwa']), 'href': self.request.route_path('wpis_show', id=i['_id'])} for i in tmp._list()]
        return {'items': items, 'title': u'Dostępne formularze'}

#    @view_config(route_name='wpis_show', renderer='string')
    @view_config(route_name='wpis_show', renderer='docforge:templates/wpis_list.jinja2')
    def show(self):
        id = self.request.matchdict.get('id', None)
        if 'sort' in self.request.GET:
            sort = self.request.GET['sort']
        else:
            sort = None
        if 'rev' in self.request.GET:
            rev = self.request.GET['rev']
            act = None
        else:
            rev = None
            act = sort
        print "sort: ", sort
        print id
        items = [i.items() for i in self._list(id, sort=sort, rev=rev)]
        return {'items': items, 'act': act}

