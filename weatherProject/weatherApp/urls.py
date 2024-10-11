from django.urls import path
from .import views

#create your views here

urlpatterns = [
    path('', views.index),
]