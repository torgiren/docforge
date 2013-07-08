from pyramid.view import view_config

class TypyView(object):
    def __init__(self, request):
        self.request = request


    def __list_names(self):
        elements = self.request.db['typy'].find({}, {'nazwa':1, 'widget':1})
        elements = [(str(i['widget']), i['nazwa']) for i in elements]
        return elements

    @view_config(route_name='typy', renderer='json')
    def list_names(self):
        return list(self.__list_names())
