from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    correo = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    instituto = models.CharField(max_length=100)
    edad = models.CharField(max_length=100)
    sexo = models.IntegerField()
    semestre = models.CharField(max_length=100)

    # Agrega cualquier otro campo adicional que desees

    def __str__(self):
        return self.user.username


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_respuesta = models.ForeignKey(
        OpcionRespuesta, on_delete=models.CASCADE)


class Instituto(models.Model):
    nombre = models.CharField(max_length=100)


class Carrera(models.Model):
    nombre = models.CharField(max_length=100)


class Calificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
