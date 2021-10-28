from django import forms

from django.core.exceptions import ValidationError

from apps.usuarios.models import Profesor,Estudiante

class profesorForm(forms.ModelForm):
    
    class Meta:
        model = Profesor
        fields = ('dni','nombreyapellido','fecha_nacimiento','telefono','sexo','domicilio','titulo','fechaIngresoTrabajar')

class estudianteForm(forms.ModelForm):
    
    class Meta:
        model = Estudiante
        fields = ('dni','nombreyapellido','fecha_nacimiento','telefono','sexo','domicilio','titulo','matricula')
