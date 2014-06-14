from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import accounts
from accounts import urls

import main
from main import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PickUp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(accounts.urls)),
    url(r'^', include(main.urls)),
)

from django.conf import settings
urlpatterns += patterns('', (r'^static/(.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT }), ) 