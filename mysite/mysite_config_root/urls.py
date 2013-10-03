from app import views
from django.conf.urls import patterns, include, url
# enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signupadmin/', views.signup_admin),
    url(r'^signup_admin/', views.signup_admin),
    url(r'^admin/', include(admin.site.urls)),
)
