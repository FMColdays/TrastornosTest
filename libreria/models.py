from django.db import models

# Create your models here.

class Test(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_actualizacion = models.DateField(auto_now=True)

class Pregunta(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    pregunta = models.TextField()
    tipo_pregunta = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    ultima_actualizacion = models.DateField(auto_now=True)

class OpcionRespuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion = models.CharField(max_length=255)
    valor = models.IntegerField()

class Respuesta(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_respuesta = models.ForeignKey(OpcionRespuesta, on_delete=models.CASCADE)

