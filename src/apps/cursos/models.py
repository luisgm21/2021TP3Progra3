from datetime import date, time
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.mixins import FieldCacheMixin
from apps.usuarios.models import Estudiante, Profesor

# Create your models here.
class curso(models.Model):
    MODALIDAD_OPCIONES = (
        ('virtual', 'Virtual'),
        ('presencial', 'Presencial'),
        ('mixto','Mixto')
    )
    ESTADO_OPCIONES = (
        ('en_revision','En Revision'),
        ('aprobado','Aprobado'),
        ('desaprobado','Desaprobado')
    )
    nombrecurso = models.CharField(max_length=100)
    objetivogeneral = models.TextField(max_length=5000)
    modalidad = models.CharField(max_length=10,choices=MODALIDAD_OPCIONES)
    costo = models.IntegerField()
    horascatedra = models.IntegerField()
    honorarios = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    cantidadminalumnos = models.IntegerField()
    cantidadmaxalumnos = models.IntegerField()
    fechaini = models.DateField()
    fechafin = models.DateField()
    docentecargo = models.ManyToManyField(Profesor)
    estadocurso = models.CharField(max_length=20,default='En Revision', choices=ESTADO_OPCIONES)
    motivo = models.TextField(max_length=1000,default='Sin Motivo')
    def __str__(self):
        return f"NombreCurso:{self.nombrecurso}"

#----------------------------------------------------------------------------------------    
class Pago(models.Model):
    # PAGO_OPCIONES = (
    #     ('Efectivo', 'Efectivo'),
    #     ('Tarjeta', 'Tarjeta'),
    #     ('Transferencia','Transferencia')
    # )
    formaPago = models.CharField( max_length=15)
    importe = models.DecimalField(max_digits=7,decimal_places=2)
    descripcion = models.TextField(max_length=250)
    fecha = models.DateTimeField(default= date.today)
    numRecibo = models.IntegerField(null=True,blank=True)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE,null=True,blank=True)
    inscripto = models.ForeignKey(Estudiante, on_delete=models.CASCADE,null=True,blank=True)
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
    titularTarjeta = models.CharField(max_length=50)
    numeroTarjeta = models.CharField(max_length=16)
    tipoTarjeta = models.CharField(choices=PAGO_TARJETA_OPCIONES,max_length=10)
    codSeguridad = models.CharField(max_length=3)
    fechaCaducidad = models.DateField()
    formaPago = models.CharField(default='PagoTarjeta',max_length=100)

class PagoTransferencia(Pago):
    CBU = models.CharField(max_length=22)
    alias = models.CharField(max_length=25)
    banco = models.CharField(max_length=50)
    formaPago = models.CharField(default='PagoTransferencia',max_length=100)

#-----------------------------------------------------------------------------

class Inscriptos(models.Model):
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    inscripto = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nota1 = models.IntegerField(null=True,blank=True,default = 0)
    nota2 = models.IntegerField(null=True,blank=True,default = 0)
    nota3 = models.IntegerField(null=True,blank=True,default = 0)
    asistencia = models.CharField(max_length=4, default='100%')

#Lo agregamos para una posible funcionalidad pero no la usamos
class Estadistica(models.Model):
    curso = models.ForeignKey(curso,on_delete=models.CASCADE)