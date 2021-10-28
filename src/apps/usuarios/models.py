from django.db import models
from django.db.models.base import Model

# Create your models here.
class Persona(models.Model):
    dni = models.CharField(max_length=8,unique=True)
    nombreyapellido = models.CharField(max_length=100)
    fecha_nacimiento= models.DateTimeField()
    telefono= models.IntegerField()
    sexo= models.CharField(max_length=15,null=False, blank=False)
    domicilio=models.CharField(max_length=256,null=False, blank=False)
    titulo=models.CharField(max_length=40,null=True)
    class Meta:
        abstract = True
class Usuario(models.Model):
    username = models.CharField(max_length=15, unique=True,null=False,blank=False)
    email= models.EmailField(unique=True)
    password= models.TextField(null=False, blank=False)

class Estudiante(Persona):
    matricula= models.CharField(max_length=4,unique=True)

class Profesor(Persona):
    fechaIngresoTrabajar= models.DateField(null=True)
    
    def __str__(self):
        return super().nombreyapellido

