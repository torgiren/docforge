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
    config.add_route('home', '/')
    config.include('docforge.routes.formatka.formatki', route_prefix='/formatki')
    config.include('docforge.routes.ajax.ajax', route_prefix='/ajax')
    config.registry.db = pymongo.Connection('localhost')
    config.add_request_method(add_db, 'db', reify=True)
    config.scan()
    return config.make_wsgi_app()
