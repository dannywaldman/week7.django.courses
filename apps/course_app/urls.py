from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^/courses$', views.index, name = 'courses'),
    url(r'^/(?P<id>\d+)/destroy$', views.destroy, name = 'destroy'),
    url(r'^/(?P<id>\d+)/show$', views.show, name = 'show'),
    url(r'^/(?P<id>\d+)/comment$', views.comment, name = 'comment')
]
