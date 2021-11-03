from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    SEXO_OPCIONES = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otrxs','Otrxs')
    )
    dni = models.CharField(max_length=8,unique=True)
    nombreyapellido = models.CharField(max_length=100)
    fecha_nacimiento= models.DateTimeField()
    telefono= models.IntegerField()
    sexo= models.CharField(max_length=15,choices=SEXO_OPCIONES,null=False, blank=False)
    domicilio=models.CharField(max_length=256,null=False, blank=False)
    titulo=models.CharField(max_length=40,null=True)
    class Meta:
        abstract = True
class Estudiante(Persona):
    matricula= models.CharField(max_length=4,unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True,unique=True)

class Profesor(Persona):
    fechaIngresoTrabajar= models.DateField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True,unique=True)
    
    def __str__(self):
        return super().nombreyapellido

