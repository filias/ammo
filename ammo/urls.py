from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'base.views.home', name='home'),
    #url(r'^ammo/', include('ammo.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls')),
)
