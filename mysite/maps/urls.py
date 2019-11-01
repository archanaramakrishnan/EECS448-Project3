from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/maps/$', views.add_map, name='add_map'),
]