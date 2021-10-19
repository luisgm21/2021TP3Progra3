from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import tablaCursos,datosCurso,estadisticas,estadoCursos,inscripcion,pago

app_name='cursos'

urlpatterns=[
    #cursos views
    path('', tablaCursos,name='registroCursos'),
    path('<int:pk>/', datosCurso,name='cursoDetalle'),
    path('estadisticas/', estadisticas,name='estadisticas'),
    path('estadocursos/', estadoCursos,name='estadoCursos'),
    path('inscripcion/', inscripcion,name='inscrpcion'),
    path('pago/', pago,name='pago'),


] 