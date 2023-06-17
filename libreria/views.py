from django.shortcuts import render, redirect
from .models import Pregunta, Test, Instituto, Carrera
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UsuarioForm
from django.contrib.auth import logout, login
import random
# Create your views here.

COLORES = ['#9AFAC2', '#FAF499', '#FA8E7D',
           '#FAA8EF', '#CCD3FA', '#C3F9F9', '#9FFA9B']


@login_required
def inicio(request):
    return render(request, 'index.html')


def registro(request):
    carreras = Carrera.objects.all()
    institutos = Instituto.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        perfil_form = UsuarioForm(request.POST)
        if form.is_valid() and perfil_form.is_valid():
            user = form.save()
            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()
            login(request, user)
            return redirect('inicio')
    else: 
        form = UserCreationForm()
        perfil_form = UsuarioForm()
    
    return render(request, 'registration/registro.html', {'form': form, 'perfil_form': perfil_form, 'institutos': institutos, 'carreras': carreras})
    
    


@login_required
def tests(request, test_nombre):
    color_fondo = random.choice(COLORES)
    tests = Test.objects.filter(nombre=test_nombre)
    preguntas = Pregunta.objects.filter(test__in=tests)
    return render(request, 'tests.html', {'preguntas': preguntas, 'color_fondo': color_fondo, 'test_nombre': test_nombre})



@login_required
def salir(request):
    logout(request)
    return redirect('/')
