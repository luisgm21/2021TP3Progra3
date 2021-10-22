from django.shortcuts import render, get_object_or_404, redirect
from .models import curso
# Create your views here.

def listaCursos(request):
    return render(request, 'cursos/tablaCursos.html',
    {'cursos': curso.objects.all()})
