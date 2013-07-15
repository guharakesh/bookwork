from django.conf.urls import patterns, url

from homepage import views

urlpattersn = patterns('',
    url(r'^$', views.index, name='index')
)
