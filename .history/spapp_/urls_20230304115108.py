from django.urls import path
from sapp_.vie import views

urlpattern = [
    path('', views.index, name = 'index')
]