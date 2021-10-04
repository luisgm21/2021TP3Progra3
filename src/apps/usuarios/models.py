from django.db import models

# Create your models here.
class Persona(models.Model):
    dni = models.IntegerField(unique=True)
    nombreyapellido = models.CharField(max_length=100)
    fecha_nacimiento= models.DateTimeField()
    telefono= models.IntegerField()
    sexo= models.CharField(max_length=15,null=False, blank=False)
    domicilio=models.CharField(max_length=256,null=False, blank=False)
class Usuario(models.Model):
    username = models.CharField(max_length=15, unique=True,null=False,blank=False)
    email= models.EmailField(unique=True)
    password= models.TextField(null=False, blank=False)

