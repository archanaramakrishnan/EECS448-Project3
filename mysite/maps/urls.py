from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/maps/$', views.add_map, name='add_map'),
    url(r'^maps/(?P<id>\d+)/$', views.distance_output, name='distance_output'),
]