from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import listaCursos,datosCurso,estadisticas,estadoCursos,inscripcion,pago,creacion_curso

app_name='cursos'

urlpatterns=[
    #cursos views
    path('', listaCursos,name='registroCursos'),
    path('crear/',creacion_curso,name='creacion_curso'),
    path('<int:pk>/', datosCurso,name='cursoDetalle'),
    path('estadisticas/', estadisticas,name='estadisticas'),
    path('estadocursos/', estadoCursos,name='estadoCursos'),
    path('inscripcion/', inscripcion,name='inscrpcion'),
    path('pago/', pago,name='pago'),


] 