from datetime import date, time
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.mixins import FieldCacheMixin
from apps.usuarios.models import Estudiante, Profesor
from django.utils import timezone
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
    honorarios=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
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
    # PAGO_OPCIONES = (
    #     ('Efectivo', 'Efectivo'),
    #     ('Tarjeta', 'Tarjeta'),
    #     ('Transferencia','Transferencia')
    # )
    formaPago= models.CharField( max_length=15)
    importe=models.DecimalField(max_digits=7,decimal_places=2)
    descripcion=models.TextField(max_length=250)
    fecha=models.DateTimeField(default= date.today)
    numRecibo=models.IntegerField(null=True,blank=True)
    class Meta:
        abstract = True
    
class PagoEfectivo(Pago):
    formaPago= models.CharField(default='Efectivo',max_length=100)
    numeroTicket=models.IntegerField(null=True,blank=True)

class PagoTarjeta(Pago):
    PAGO_TARJETA_OPCIONES= (
        ('Debito', 'Debito'),
        ('Credito', 'Credito')    
    )
    titularTarjeta=models.CharField(max_length=50)
    numeroTarjeta=models.CharField(max_length=16)
    tipoTarjeta=models.CharField(choices=PAGO_TARJETA_OPCIONES,max_length=10)
    codSeguridad=models.CharField(max_length=3)
    fechaCaducidad=models.DateField(default=date.today)
    formaPago= models.CharField(default='PagoTarjeta',max_length=100)

class PagoTransferencia(Pago):
    CBU=models.CharField(max_length=22)
    alias=models.CharField(max_length=25)
    banco=models.CharField(max_length=50)
    formaPago= models.CharField(default='PagoTransferencia',max_length=100)

#-----------------------------------------------------------------------------

class Inscriptos(models.Model):
    curso=models.ForeignKey(curso, on_delete=models.CASCADE)
    incriptos= models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nota1=models.IntegerField(null=True)
    nota2=models.IntegerField(null=True)
    nota3=models.IntegerField(null=True)
    asistencia= models.CharField(max_length=4)

