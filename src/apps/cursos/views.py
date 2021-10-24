from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from apps.cursos.forms import cursoForm
from .models import curso
# Create your views here.

def listaCursos(request):
    return render(request, 'cursos/tablaCursos.html',
    {'cursos': curso.objects.all()})

# def creacion_curso(request):
#     nuevo_curso=curso()

#     if(request.method == 'POST'):
#         nuevo_curso.nombrecurso = request.POST.get('nombreCurso',None)
#         nuevo_curso.objetivogeneral = request.POST.get('objectivo',None)
#         nuevo_curso.modalidad = request.POST.get('modalidad',None)
#         nuevo_curso.costo = request.POST.get('costo',None)
#         nuevo_curso.horascatedra = request.POST.get('horasCatedra',None)
#         nuevo_curso.cantidadmaxalumnos = request.POST.get('cantMinimaAlum',None)
#         nuevo_curso.cantidadminalumnos = request.POST.get('cantMaximaAlum',None)
#         nuevo_curso.fechaini = request.POST.get('fechaInicio') 
#         nuevo_curso.fechafin = request.POST.get('fechaFin') if request.POST.get('fechaFin') else None 
#         try:
#             nuevo_curso.save()
#             messages.success(request,'se ha agregado correctamente el programa {}',format(nuevo_curso))
#         except Exception as e:
#             messages.error(request,'No se puedo agregar el programa {}',format(e)
#             )
#         return redirect(reverse)   
#     else:

@csrf_exempt
def creacion_curso(request):
    if (request.method == 'POST'):
        curso_form = cursoForm(request.POST)
        if curso_form.is_valid():
            nuevo_curso = curso_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_curso))
            return redirect(reverse('cursos:registroCursos'))
    else:
        curso_form = cursoForm()    
    return render(request,'cursos/formcrearcurso.html',{'form': curso_form})


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
