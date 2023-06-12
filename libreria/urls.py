from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('depresion/', views.depresion, name='depresion'),
    path('alcoholismo/', views.alcoholismo, name='alcoholismo'),
    path('MDQ/', views.mdq, name='mdq'),
    path('DEP-ADO/', views.drogas, name='drogas'),
    path('BECK/', views.beck, name='beck'),
    path('EDDS/', views.edds, name='edds'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', views.salir, name='salir'),
    path('registro/', views.registro, name='registro'),
]
