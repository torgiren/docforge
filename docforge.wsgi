import site
vepath = '/home/torgiren/env/mgr/lib/python2.7/site-packages'
site.addsitedir(vepath)
from pyramid.paster import get_app, setup_logging
ini_path = '/home/torgiren/docforge/development.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
