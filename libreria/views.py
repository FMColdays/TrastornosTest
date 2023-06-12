from django.shortcuts import render
from django.http import HttpResponse
from .models import Pregunta, Test
# Create your views here.


def inicio(request):
   return render(request, 'index.html')

def depresion(request):
   #aqui va el test phq-9 xd
   test_PHQ = Test.objects.get(nombre='PHQ-9')  # Recuperar el test 
   preguntas = Pregunta.objects.filter(test=test_PHQ)  # Filtrar las preguntas solo para el test
   return render(request, 'depresion.html', {'preguntas': preguntas}) # Mandar las preguntas al test para que se recorran en un for

def mdq(request):
   #aqui va el test mdq xd
   test_MDQ = Test.objects.get(nombre='MDQ')  # Recuperar el test 
   preguntas = Pregunta.objects.filter(test=test_MDQ)  # Filtrar las preguntas solo para el test
   return render(request, 'mdq.html', {'preguntas': preguntas}) # Mandar las preguntas al test para que se recorran en un for

def drogas(request):
   #aqui va el test DEP-ADO xd
   DEP_ADO = Test.objects.get(nombre='DEP-ADO')  # Recuperar el test 
   preguntas = Pregunta.objects.filter(test=DEP_ADO)  # Filtrar las preguntas solo para el test
   return render(request, 'drogas.html', {'preguntas': preguntas}) # Mandar las preguntas al test para que se recorran en un for

def beck(request):
   #aqui va el test DEP-ADO xd
   BHS = Test.objects.get(nombre='BHS')  # Recuperar el test 
   preguntas = Pregunta.objects.filter(test=BHS)  # Filtrar las preguntas solo para el test
   return render(request, 'beck.html', {'preguntas': preguntas}) # Mandar las preguntas al test para que se recorran en un for

def edds(request):
   #aqui va el test DEP-ADO xd
   EDDS = Test.objects.get(nombre='EDDS')  # Recuperar el test 
   preguntas = Pregunta.objects.filter(test=EDDS)  # Filtrar las preguntas solo para el test
   return render(request, 'edds.html', {'preguntas': preguntas}) # Mandar las preguntas al test para que se recorran en un for

def alcoholismo(request):
   #aqui va el audit xd
   test_audit = Test.objects.get(nombre='AUDIT')  # Recuperar el test AUDIT
   preguntas = Pregunta.objects.filter(test=test_audit)  # Filtrar las preguntas solo para el test AUDIT
   return render(request, 'alcoholismo.html', {'preguntas': preguntas})