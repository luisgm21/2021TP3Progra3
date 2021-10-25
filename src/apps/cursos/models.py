from datetime import date
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.mixins import FieldCacheMixin
from apps.usuarios.models import Profesor

# Create your models here.
class curso(models.Model):
    MODALIDAD_OPCIONES = (
        ('virtual', 'Virtual'),
        ('presencial', 'Presencial'),
        ('mixto','Mixto')
    )
    nombrecurso = models.CharField(max_length=100)
    objetivogeneral = models.TextField(max_length=5000)
    modalidad = models.CharField(max_length=10,choices=MODALIDAD_OPCIONES)
    costo = models.IntegerField()
    horascatedra = models.IntegerField()
    cantidadminalumnos= models.IntegerField()
    cantidadmaxalumnos=models.IntegerField()
    fechaini=models.DateTimeField(default= date.today)
    fechafin=models.DateTimeField()
    docentecargo= models.ManyToManyField(Profesor)
    estadocurso= models.CharField(max_length=20,default='En Curso')
    def __str__(self):
        return f"NombreCurso:{self.nombrecurso}"

class propuesta(models.Model):
    codcurso= models.OneToOneField(curso,on_delete=models.CASCADE)
    descripcion= models.TextField(max_length=5000)
    fecha= models.DateTimeField()
    estado = models.CharField(max_length=30)
    docente= models.OneToOneField(Profesor,on_delete=models.CASCADE)

#----------------------------------------------------------------------------------------    
class Pago(models.Model):
    PAGO_OPCIONES = (
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia','Transferencia')
    )
    FormaPago= models.CharField(choices=PAGO_OPCIONES, max_length=15)
    importe=models.IntegerField()
    descripcion=models.TextField(max_length=250)
    fecha=models.DateTimeField(default= date.today)
    class Meta:
        abstract = True
    
class PagoEfectivo(Pago):
    numeroRecibo=models.IntegerField()

class PagoTarjeta(Pago):
    PAGO_TARJETA_OPCIONES= (
        ('Debito', 'Debito'),
        ('Credito', 'Credito')    
    )
    titularTarjeta=models.CharField(max_length=50)
    numeroTarjeta=models.CharField(max_length=16)
    TipoTarjeta=models.CharField(choices=PAGO_TARJETA_OPCIONES,max_length=10)
    codSeguridad=models.CharField(max_length=3)

class PagoTransferencia(Pago):
    CBU=models.CharField(max_length=22)
    alias=models.CharField(max_length=25)
    banco=models.CharField(max_length=50)

#-----------------------------------------------------------------------------


