from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('depresion/', views.depresion, name='depresion'),
    path('alcoholismo/', views.alcoholismo, name='alcoholismo'),
    path('mdq/', views.mdq, name='mdq'),
    path('dep-ado/', views.drogas, name='drogas'),
    path('beck/', views.beck, name='beck'),
    path('edds/', views.edds, name='edds'),
    path('ansiedad/', views.ansiedad, name='ansiedad'),
     path('afectacion-academica/', views.afecciónAcadémica, name='afecciónAcadémica'),
    path('estres/', views.estres, name='estres'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', views.salir, name='salir'),
    path('registro/', views.registro, name='registro'),
]
