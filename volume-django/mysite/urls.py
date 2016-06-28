"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(u'^restful/current/start/(?P<start>.+)/destination/(?P<destination>.+)$', 'trips.views.getNow'),
    url(r'^restful/current/monitor_status', 'trips.views.getSpeed'),
    url(r'^restful/current/overall','trips.views.getCurrent'),
    url(r'^restful/forecast/overall', 'trips.views.predictionAll'),
    url(r'^restful/forecast/(?P<time>[0-9]+)/start/(?P<start>.+)/destination/(?P<destination>.+)$', 'trips.views.prediction'),
    url(r'^restful/suggestion/direction/(?P<direction>.+)', 'trips.views.suggestion'),
    url(r'home/', 'trips.views.home'),
]
