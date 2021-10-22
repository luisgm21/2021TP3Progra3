from django.shortcuts import render, get_object_or_404, redirect
from .models import curso
# Create your views here.

def listaCursos(request):
    return render(request, 'cursos/tablaCursos.html',
    {'cursos': curso.objects.all()})
def tablaCursos(request):
    return render(request, 'cursos/tablaCursos.html')

def datosCurso(request):
    return render(request, 'cursos/datosCurso.html')   

def estadisticas(request):
    return render(request, 'cursos/estadisticas.html') 

def estadoCursos(request):
    return render(request, 'cursos/estadoCursos.html')   
def inscripcion(request):
    return render(request, 'cursos/inscripcion.html')   
def pago(request):
    return render(request, 'cursos/pago.html')   
