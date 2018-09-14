# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    url(r'^logout/$', views.logout),
    url(r'^center_handle/$', views.center_handle),
    url(r'^center_handle2/$', views.center_handle2),
]
