from app import views
from django.conf.urls import patterns, include, url
# enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^app/', views.index, name='index'),
    url(r'^signup/', views.signup, name='signup'),

    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
