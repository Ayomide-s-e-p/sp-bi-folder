from django.urls import path
from from import views

urlpattern = [
    path('', views.index, name = 'index')
]