from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import C_pagoEfectivo, C_pagoTarjeta, C_pagoTransferencia, evaluar_curso, listaCursos,datosCurso,estadisticas,estadoCursos,inscripcion,pago,creacion_curso,edicion_curso,curso_delete, ventana_ecurso

app_name='cursos'

urlpatterns=[
    #cursos views
    path('', listaCursos,name='registroCursos'),
    path('crear/',creacion_curso,name='creacion_curso'),
    path('<int:pk>/', datosCurso,name='cursoDetalle'),
    path('estadisticas/', estadisticas,name='estadisticas'),
    path('estadocursos/', estadoCursos,name='estadoCursos'),
    path('inscripcion/', inscripcion,name='inscripcion'),
    path('pago/', pago,name='pago'),
    path('edicion/<int:pk>',edicion_curso,name='curso_edicion'),
    path('delete/', curso_delete, name='curso_delete'),
    path('pago/efectivo', C_pagoEfectivo, name='pagoefectivo'),
    path('pago/tarjeta', C_pagoTarjeta, name='pagotarjeta'),
    path('pago/transferencia', C_pagoTransferencia, name='pagotransferencia'),
    path('evaluar/',evaluar_curso,name='evaluar'),
    path('evaluar/<int:pk>/',ventana_ecurso,name='curso_evaluar')

] 