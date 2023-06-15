from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('depresion/', views.tests, {'test_nombre': 'PHQ-9'}, name='depresion'),
    path('mdq/', views.tests, {'test_nombre': 'MDQ'}, name='mdq'),
    path('alcoholismo/', views.tests, {'test_nombre': 'AUDIT'}, name='alcoholismo'),
    path('dep-ado/', views.tests, {'test_nombre': 'DEP-ADO'}, name='drogas'),
    path('beck/', views.tests, {'test_nombre': 'BHS'}, name='beck'),
    path('edds/', views.tests, {'test_nombre': 'EDDS'}, name='edds'),
    path('ansiedad/', views.tests, {'test_nombre': 'Ansiedad'}, name='ansiedad'),
    path('estres/', views.tests, {'test_nombre': 'Estres'}, name='estres'),
    path('afectacion-academica/', views.tests, {'test_nombre': 'AfeccionAcademica'}, name='afecciónAcadémica'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('salir/', views.salir, name='salir'),
    path('registro/', views.registro, name='registro'),
]
