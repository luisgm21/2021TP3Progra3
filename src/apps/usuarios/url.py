from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import login,creacion_estudiante

app_name='usuarios'

urlpatterns=[
    #cursos views
    path('', login , name='login'),
    path('crear/estudiante',creacion_estudiante,name='crear_estudiante')

] 