from django.shortcuts import render, redirect
from .models import Pregunta, Test, Instituto, Carrera, OpcionRespuesta, Respuesta
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
    tests = Test.objects.get(nombre=test_nombre)
    preguntas = Pregunta.objects.filter(test=tests)

    if request.method == 'POST':
        respuestas = []
        for key, value in request.POST.items():
            if key.startswith('pregunta'):
                respuesta = {
                    'pregunta_id': key,
                    'opcion_id': value
                }
                respuestas.append(respuesta)

        for respuesta in respuestas:
            pregunta_id = respuesta['pregunta_id'].replace('pregunta', '')
            opcion_id = respuesta['opcion_id']

            pregunta = Pregunta.objects.get(pk=pregunta_id)
            opcion = OpcionRespuesta.objects.get(pk=opcion_id)

            nueva_respuesta = Respuesta(
                user=request.user,
                test=tests,
                pregunta=pregunta,
                opcion_respuesta=opcion
            )
            nueva_respuesta.save()
        return redirect('inicio')
        

    return render(request, 'tests.html', {'preguntas': preguntas, 'color_fondo': color_fondo, 'test_nombre': test_nombre})

@login_required
def salir(request):
    logout(request)
    return redirect('/')
