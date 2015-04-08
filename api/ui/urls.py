from django.conf.urls import *
#from dns_api.view import hello, date_time
import views


urlpatterns = patterns(
'',
    # Examples:
    # url(r'^$', 'dns_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
#	(r'^ui$', views.user_template),
	#(r'^home/$', views.search_template),
	(r'^$', views.search_template),
	(r'^search/$', views.search_data),
	(r'^update/$', views.update_data),
	(r'^callapi/$', views.callapi)
#	(r'^admin/', include(admin.site.urls)),
)
