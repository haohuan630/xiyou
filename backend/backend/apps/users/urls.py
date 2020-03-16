#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : sunny
# from django.urls import path
#
# from users import views
#
# urlpatterns = [
#     path(r'login', views.Login.as_view())
# ]

from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from users import views

urlpatterns = [
    url(r'^areas/$', views.AreasView.as_view(), name='areas-list'),
    url(r'^areas/(?P<pk>\d+)/$', views.SubAreasView.as_view(), name='areas-detail'),
]

# router = DefaultRouter()
# router.register('users', views.AreaViewSet, base_name='users')
# urlpatterns += router.urls
