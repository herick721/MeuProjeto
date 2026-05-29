from django.contrib import admin
from django.urls import path
from CarsApp import views

app_name = "CarsApp"

urlpatterns = [
    path("", views.searchf, name="home"),
    path("detalhes/<int:carro_id>/", views.detalhes, name="detalhes"),
]
