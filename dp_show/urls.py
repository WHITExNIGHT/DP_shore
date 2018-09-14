# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^center/([0-9]+)/$', views.center),
    # url(r'^test/$', views.test),
    # url(r'^test1/$', views.test1),
]
