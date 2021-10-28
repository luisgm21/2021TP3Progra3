from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.usuarios.models import Estudiante
from .forms import profesorForm,estudianteForm
# Create your views here.

def login(request):
    return render(request, 'usuarios/login.html')


@csrf_exempt
def creacion_estudiante(request):
    if (request.method == 'POST'):
        estudiante_form = estudianteForm(request.POST)
        if estudiante_form.is_valid():
            nuevo_estudiante = estudiante_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_estudiante))
            return redirect(reverse('cursos:registroCursos'))
    else:
        estudiante_form = estudianteForm()    
    return render(request,'usuarios/inscripcion.html',{'form': estudiante_form})


@csrf_exempt
def edicion_curso(request, pk):
    estudiante = get_object_or_404(Estudiante, pk = pk)

    if (request.method == 'POST'):
        estudiante_form = estudianteForm(request.POST, request.FILES, instance=estudiante)
        if estudiante_form.is_valid():
            estudiante_form.save(commit=True)
            messages.success(request,
                             'Se ha editado correctamente el curso con el {}'.format(estudiante))
            return redirect(reverse('cursos:registroCursos'))
    else:
        estudiante_form = estudianteForm(instance=estudiante)    
    return render(request,'cursos/modificarCurso.html',{'form': estudiante_form})


def estudiante_delete(request):
    if request.method == 'POST':
        if 'id_estudiante' in request.POST:
            estudiante = get_object_or_404(Estudiante, pk=request.POST['id_estudiante'])
            nombre_estudiante = estudiante.nombreyapellido
            estudiante.delete()
            messages.success(request, 'Se ha eliminado exitosamente el curso {}'.format(nombre_estudiante))
        else:
            messages.error(request, 'Debe indicar qué Programa se desea eliminar')
    return redirect(reverse('usuarios:listaEstudiantes'))

@csrf_exempt
def creacion_profesor(request):
    if (request.method == 'POST'):
        profesor_form = profesorForm(request.POST)
        if profesor_form.is_valid():
            nuevo_profesor = profesor_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_profesor))
            return redirect(reverse('cursos:registroCursos'))
    else:
        profesor_form = profesorForm()    
    return render(request,'usuarios/inscripcion.html',{'form': profesor_form})