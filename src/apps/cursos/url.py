from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import C_pagoEfectivo, C_pagoTarjeta, C_pagoTransferencia, comprobantePago, comprobantePagoB, comprobantePagoT, estadisticas_1, estadisticas_2, evaluar_curso, evaluar_inscripto, inscripcion_curso, listaCursos,datosCurso,estadisticas,estadoCursos,inscripcion, listaInscriptos,pago,creacion_curso,edicion_curso,curso_delete, ventana_ecurso

app_name='cursos'

urlpatterns=[
    #cursos views
    path('', listaCursos,name='registroCursos'),
    path('crear/',creacion_curso,name='creacion_curso'),
    path('<int:pk>/', datosCurso,name='cursoDetalle'),
    path('estadocursos/', estadoCursos,name='estadoCursos'),
    path('edicion/<int:pk>',edicion_curso,name='curso_edicion'),
    path('delete/', curso_delete, name='curso_delete'),
    path('evaluar/',evaluar_curso,name='evaluar'),
    path('evaluar/<int:pk>/',ventana_ecurso,name='curso_evaluar'),
    path('inscripcion/<int:pk>',inscripcion_curso,name='inscripcion'),
    path('lista/<int:pk>',listaInscriptos,name='listaAlumnos'),
    path('lista/inscripto/<int:pk>',evaluar_inscripto,name='alumno'),
    path('estadisticas/', estadisticas,name='estadisticas'),
    path('pago/<int:pk>', pago,name='pago'),
    path('pago/efectivo/<int:pk>', C_pagoEfectivo, name='pagoefectivo'),
    path('pago/tarjeta/<int:pk>', C_pagoTarjeta, name='pagotarjeta'),
    path('pago/transferencia/<int:pk>', C_pagoTransferencia, name='pagotransferencia'),
    path('pago/comprobante/<int:pk>', comprobantePago, name='comprobante_pago'),
    path('pago/comprobanteT/<int:pk>', comprobantePagoT, name='comprobante_pagoT'),
    path('pago/comprobanteB/<int:pk>', comprobantePagoB, name='comprobante_pagoB'),
    path('Estadisticas/A',estadisticas_1,name='Estadistica1'),
    path('Estadisticas/B',estadisticas_2,name='Estadistica2')
] 



 