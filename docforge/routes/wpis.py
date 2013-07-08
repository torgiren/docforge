def wpis(config):
    config.add_route('wpis_add', '/add', request_method="POST")
    config.add_route('wpis_list', '/list')
    config.add_route('wpis_show', '/list/{id}')
