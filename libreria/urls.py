from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('depresion/', views.depresion, name='depresion'),
    path('alcoholismo/', views.alcoholismo, name='alcoholismo'),
    path('MDQ/', views.mdq, name='mdq'),
    path('DEP-ADO/', views.drogas, name='drogas'),
    
    
    
]
