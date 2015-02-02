#from django.conf.urls import patterns, include, url
from django.conf.urls import *
#from dns_api.view import hello, date_time
import search

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dns_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
	url(r'^api/search$', search.validation),
	url(r'^ui/', include('ui.urls')),
#	(r'^ui$', ui.views.user_template),
#	(r'^ui/search$', ui.views.search_template),
#	(r'^admin/', include(admin.site.urls)),
)
