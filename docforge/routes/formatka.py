def formatki(config):
    config.add_route('formatki_list', '/list')
    config.add_route('formatki_add_form', '/add', request_method='GET')
    config.add_route('formatki_add_do', '/add', request_method='POST')
    config.add_route('formatki_fill_form', '/fill/{id}', request_method='GET')
    config.add_route('formatki_fill_do', '/fill/{id}', request_method='POST')
