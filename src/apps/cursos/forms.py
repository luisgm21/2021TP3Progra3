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
        if fecha_fin and fecha_inicio > fecha_fin:
            raise ValidationError(
                {'fecha_inicio': 'La fecha de inicio no puede ser posterior a la fecha fin'}
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


