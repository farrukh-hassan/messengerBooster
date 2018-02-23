from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', views.username, name='username'),
    url(r'^$', views.index, name='index'),
]
