from datetime import date
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.mixins import FieldCacheMixin
from apps.usuarios.models import Profesor

# Create your models here.
class curso(models.Model):
    nombrecurso = models.CharField(max_length=100)
    objetivogeneral = models.TextField(max_length=5000)
    modalidad = models.CharField(max_length=10)
    costo = models.IntegerField()
    horascatedra = models.IntegerField()
    cantidadminalumnos= models.IntegerField()
    cantidadmaxalumnos=models.IntegerField()
    fechaini=models.DateTimeField(default= date.today)
    fechafin=models.DateTimeField()
    docentecargo= models.ManyToManyField(Profesor)
    estadocurso= models.CharField(max_length=20,default='En Curso')

class propuesta(models.Model):
    codcurso= models.OneToOneField(curso,on_delete=models.CASCADE)
    descripcion= models.TextField(max_length=5000)
    fecha= models.DateTimeField()
    estado = models.CharField(max_length=30)
    docente= models.OneToOneField(Profesor,on_delete=models.CASCADE)
    
    
