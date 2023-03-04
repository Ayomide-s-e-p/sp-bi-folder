from django.urls import path
from sapp_.views import views

urlpattern = [
    path('', views.index, name = 'index')
]