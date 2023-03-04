from django.urls import path
from sapp_ import views

urlpattern = [
    path('', views.index, name = 'index')
]