from pyramid.view import view_config


@view_config(route_name='home', renderer='docforge:templates/index.jinja2')
def home(request):
    return {}
#@view_config(route_name='home', renderer='templates/mytemplate.pt')
#def my_view(request):
#    return {'project': 'docforge'}
