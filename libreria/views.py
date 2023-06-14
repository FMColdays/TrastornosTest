from django.shortcuts import render, redirect
from .models import Pregunta, Test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UsuarioForm
from django.contrib.auth import logout, login
# Create your views here.


@login_required
def inicio(request):
    return render(request, 'index.html')


def registro(request):
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
    return render(request, 'registration/registro.html', {'form': form, 'perfil_form': perfil_form})


@login_required
def depresion(request):
    # aqui va el test phq-9 xd
    test_PHQ = Test.objects.get(nombre='PHQ-9')  # Recuperar el test
    # Filtrar las preguntas solo para el test
    preguntas = Pregunta.objects.filter(test=test_PHQ)
    # Mandar las preguntas al test para que se recorran en un for
    return render(request, 'depresion.html', {'preguntas': preguntas})

@login_required
def mdq(request):
    # aqui va el test mdq xd
    test_MDQ = Test.objects.get(nombre='MDQ')  # Recuperar el test
    # Filtrar las preguntas solo para el test
    preguntas = Pregunta.objects.filter(test=test_MDQ)
    # Mandar las preguntas al test para que se recorran en un for
    return render(request, 'mdq.html', {'preguntas': preguntas})

@login_required
def drogas(request):
    # aqui va el test DEP-ADO xd
    DEP_ADO = Test.objects.get(nombre='DEP-ADO')  # Recuperar el test
    # Filtrar las preguntas solo para el test
    preguntas = Pregunta.objects.filter(test=DEP_ADO)
    # Mandar las preguntas al test para que se recorran en un for
    return render(request, 'drogas.html', {'preguntas': preguntas})

@login_required
def beck(request):
    # aqui va el test DEP-ADO xd
    BHS = Test.objects.get(nombre='BHS')  # Recuperar el test
    # Filtrar las preguntas solo para el test
    preguntas = Pregunta.objects.filter(test=BHS)
    # Mandar las preguntas al test para que se recorran en un for
    return render(request, 'beck.html', {'preguntas': preguntas})

@login_required
def edds(request):
    # aqui va el test DEP-ADO xd
    EDDS = Test.objects.get(nombre='EDDS')  # Recuperar el test
    # Filtrar las preguntas solo para el test
    preguntas = Pregunta.objects.filter(test=EDDS)
    # Mandar las preguntas al test para que se recorran en un for
    return render(request, 'edds.html', {'preguntas': preguntas})

@login_required
def alcoholismo(request):
    # aqui va el audit xd
    test_audit = Test.objects.get(nombre='AUDIT')  # Recuperar el test AUDIT
    # Filtrar las preguntas solo para el test AUDIT
    preguntas = Pregunta.objects.filter(test=test_audit)
    return render(request, 'alcoholismo.html', {'preguntas': preguntas})

@login_required
def salir(request):
    logout(request)
    return redirect('/')
