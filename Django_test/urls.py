#coding=utf-8
#自己新建的，不是框架自己生存的

from django.urls import path
from django.conf.urls import url

from .views import index,GetTime

urlpatterns = [
    path('', index),
    path(r'^time/', GetTime),
]