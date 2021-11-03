from django import forms

from django.core.exceptions import ValidationError

from apps.cursos.models import PagoEfectivo, PagoTarjeta, PagoTransferencia, curso 

class cursoForm(forms.ModelForm):
    
    class Meta:
        model = curso
        fields = ("nombrecurso","objetivogeneral", "modalidad", "costo" ,"honorarios" ,"horascatedra","cantidadminalumnos","cantidadmaxalumnos","fechaini","fechafin","docentecargo")

    def clean(self):
        datos_validados = super().clean()
        fecha_inicio = datos_validados['fechaini']
        fecha_fin = datos_validados['fechafin']
        cantmaxalu = datos_validados['cantidadmaxalumnos']
        cantminalu = datos_validados['cantidadminalumnos']
        
        if fecha_fin and fecha_inicio > fecha_fin:
            raise ValidationError(
                {'fechaini': 'La fecha de inicio no puede ser posterior a la fecha fin'}
            )

        if cantmaxalu < cantminalu:
            raise ValidationError(
                {'cantidadminalumnos': 'La cantidad minima de alumnos no puede ser mayor a la cantidad maxima'}
            )
   

        return datos_validados

class efectivoForm(forms.ModelForm):
    
    class Meta:
        model = PagoEfectivo
        fields = ("formaPago","importe","descripcion","fecha","numRecibo","numeroTicket")

class tarjetaForm(forms.ModelForm):
    
    class Meta:
        model = PagoTarjeta
        fields = ("formaPago","importe","descripcion","fecha","numRecibo","titularTarjeta","numeroTarjeta","tipoTarjeta","codSeguridad","fechaCaducidad")



class transferenciaForm(forms.ModelForm):

    class Meta:
        model = PagoTransferencia
        fields = ("formaPago","importe","descripcion","fecha","numRecibo","CBU","alias","banco")        


