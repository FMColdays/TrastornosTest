from django.shortcuts import render, redirect
from .models import Pregunta, Test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
# Create your views here.


@login_required
def inicio(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})


def depresion(request):
    # aqui va el test phq-9 xd
    test_PHQ = Test.objects.get(nombre='PHQ-9')  # Recuperar el test
    # Filtrar las preguntas solo para el test
    preguntas = Pregunta.objects.filter(test=test_PHQ)
    # Mandar las preguntas al test para que se recorran en un for
    return render(request, 'depresion.html', {'preguntas': preguntas})


def mdq(request):
    # aqui va el test mdq xd
    test_MDQ = Test.objects.get(nombre='MDQ')  # Recuperar el test
    # Filtrar las preguntas solo para el test
    preguntas = Pregunta.objects.filter(test=test_MDQ)
    # Mandar las preguntas al test para que se recorran en un for
    return render(request, 'mdq.html', {'preguntas': preguntas})


def drogas(request):
    # aqui va el test DEP-ADO xd
    DEP_ADO = Test.objects.get(nombre='DEP-ADO')  # Recuperar el test
    # Filtrar las preguntas solo para el test
    preguntas = Pregunta.objects.filter(test=DEP_ADO)
    # Mandar las preguntas al test para que se recorran en un for
    return render(request, 'drogas.html', {'preguntas': preguntas})


def beck(request):
    # aqui va el test DEP-ADO xd
    BHS = Test.objects.get(nombre='BHS')  # Recuperar el test
    # Filtrar las preguntas solo para el test
    preguntas = Pregunta.objects.filter(test=BHS)
    # Mandar las preguntas al test para que se recorran en un for
    return render(request, 'beck.html', {'preguntas': preguntas})


def edds(request):
    # aqui va el test DEP-ADO xd
    EDDS = Test.objects.get(nombre='EDDS')  # Recuperar el test
    # Filtrar las preguntas solo para el test
    preguntas = Pregunta.objects.filter(test=EDDS)
    # Mandar las preguntas al test para que se recorran en un for
    return render(request, 'edds.html', {'preguntas': preguntas})


def alcoholismo(request):
    # aqui va el audit xd
    test_audit = Test.objects.get(nombre='AUDIT')  # Recuperar el test AUDIT
    # Filtrar las preguntas solo para el test AUDIT
    preguntas = Pregunta.objects.filter(test=test_audit)
    return render(request, 'alcoholismo.html', {'preguntas': preguntas})


def salir(request):
    logout(request)
    return redirect('login')
