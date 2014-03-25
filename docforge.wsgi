import site
vepath = '/home/torgiren/env/mgr2.6/lib/python2.6/site-packages'
site.addsitedir(vepath)
vepath = '/home/torgiren/docforge'
site.addsitedir(vepath)
from pyramid.paster import get_app, setup_logging
ini_path = '/home/torgiren/docforge/development.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
