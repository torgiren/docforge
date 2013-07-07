from pyramid.config import Configurator
import pymongo


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    def add_db(request):
        db = config.registry.db['docforge']
        return db
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('formatki_list', '/formatki/list')
    config.add_route('formatki_add_form', '/formatki/add', request_method='GET')
    config.add_route('formatki_add_do', '/formatki/add', request_method='POST')
    config.add_route('typy', '/typy')
    config.registry.db = pymongo.Connection('localhost')
    config.add_request_method(add_db, 'db', reify=True)
    config.scan()
    return config.make_wsgi_app()
