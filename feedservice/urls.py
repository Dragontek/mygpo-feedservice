from django.conf.urls import patterns, url

from feedservice.webservice.views import ParseView, IndexView

urlpatterns = patterns('',
 url(r'^$',               IndexView.as_view(),     name='index'),
 url(r'^parse$',          ParseView.as_view(),     name='parse'),
)
