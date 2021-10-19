from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import tablaCursos
app_name='cursos'

urlpatterns=[
    #cursos views
    path('', tablaCursos,name='registroCursos')
] 