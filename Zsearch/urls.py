from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'Auth.views.index'),
	(r'^user/', include('Auth.urls')),
)

