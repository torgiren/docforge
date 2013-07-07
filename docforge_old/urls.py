from django.conf.urls import patterns, include, url
import core.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', core.views.index),
	url(r'formatka/dodaj$', core.views.formatka_add),
	url(r'formatka/list$', core.views.formatka_list),
	url(r'formatka/wpis/(?P<id>\d+)$', core.views.formatka_wpis),
    # Examples:
    # url(r'^$', 'docforge.views.home', name='home'),
    # url(r'^docforge/', include('docforge.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
