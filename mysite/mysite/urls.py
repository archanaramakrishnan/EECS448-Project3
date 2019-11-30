"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from myapp import views as v
from maps import views as map_v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    url(r'^$', v.index),
    url(r'^add/maps', map_v.add_map),
    url(r'^maps/(?P<id>\d+)/$', map_v.distance_output),
    url(r'^advice.html', v.advice),
     url(r'^view_advice.html', v.view_advice, name='post_list'),
     url(r'^post_new.html', v.post_new, name='post_new'),
     url(r'^time.html', v.time, name = "time"),
    url(r'^ratings_landing_page.html', v.ratings_landing_page),
    url(r'^rating_form.html', v.rating_form),
    url(r'^ratings_view_class.html', v.ratings_view_class),
    path('', v.rating_form),
]

urlpatterns += staticfiles_urlpatterns()
