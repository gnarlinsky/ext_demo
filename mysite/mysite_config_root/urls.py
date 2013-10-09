from app import views
from django.conf.urls import patterns, include, url
# enable admin
from django.contrib import admin
from django.http import HttpResponseRedirect
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signupadmin/', views.signup_admin),
    url(r'^admin/$', lambda x: HttpResponseRedirect('/admin/app/customer')),
    url(r'^admin/', include(admin.site.urls)),
)
