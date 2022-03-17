from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('check', views.check, name='check'),
]