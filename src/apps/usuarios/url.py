from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern

from .views import creacion_profesor, datosAlumno, datosProfesor, edicion_alumno, edicion_profesor, estudiante_delete, listaEstudiantes, listaProfesores, login,creacion_estudiante, profesor_delete

app_name='usuarios'

urlpatterns=[
    #cursos views
    path('', login , name='login'),
    path('crear/estudiante',creacion_estudiante,name='crear_estudiante'),
    path('listar/estudiante',listaEstudiantes,name="registro_usuario_estudiante"),
    path('estudiante/<int:pk>/', datosAlumno ,name='alumnoDetalle'),
    path('edicion/estudiante/<int:pk>',edicion_alumno,name='alumno_edicion'),
    path('delete/estudiante',estudiante_delete, name='alumno_delete'),
    path('crear/profesor',creacion_profesor,name='crear_profesor'),
    path('listar/profesor',listaProfesores,name="registro_usuario_profesor"),
    path('profesor/<int:pk>/', datosProfesor ,name='profesorDetalle'),
    path('edicion/profesor/<int:pk>',edicion_profesor,name='profesor_edicion'),
    path('delete/profesor',profesor_delete, name='profesor_delete'),
] 