from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/maps/$', views.add_map, name='add_map'),
    url(r'^maps/(?P<id>\d+)/$', views.building, name='building'),
    url(r'^maps/$', views.building, name='building'),
]