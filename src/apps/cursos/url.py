from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import listaCursos
app_name='cursos'

urlpatterns=[
    #cursos views
   
    path('', listaCursos,name='registroCursos')
] 