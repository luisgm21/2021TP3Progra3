from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.usuarios.models import Estudiante, Profesor
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
                             'Se ha agregado correctamente el estudiante {}'.format(nuevo_estudiante))
            return redirect(reverse('usuarios:registro_usuario_estudiante'))
    else:
        estudiante_form = estudianteForm()    
    return render(request,'usuarios/crearestudiante.html',{'form': estudiante_form})


@csrf_exempt
def edicion_alumno(request, pk):
    estudiante = get_object_or_404(Estudiante, pk = pk)

    if (request.method == 'POST'):
        estudiante_form = estudianteForm(request.POST, request.FILES, instance=estudiante)
        if estudiante_form.is_valid():
            estudiante_form.save(commit=True)
            messages.success(request,
                             'Se ha editado correctamente el estudiante con el {}'.format(estudiante))
            return redirect(reverse('usuarios:registro_usuario_estudiante'))
    else:
        estudiante_form = estudianteForm(instance=estudiante)    
    return render(request,'usuarios/modificarestudiante.html',{'form': estudiante_form})


def estudiante_delete(request):
    if request.method == 'POST':
        if 'id_alumno' in request.POST:
            estudiante = get_object_or_404(Estudiante, pk=request.POST['id_alumno'])
            nombre_estudiante = estudiante.nombreyapellido
            estudiante.delete()
            messages.success(request, 'Se ha eliminado exitosamente el estudiante {}'.format(nombre_estudiante))
        else:
            messages.error(request, 'Debe indicar qué estudiante se desea eliminar')
    return redirect(reverse('usuarios:registro_usuario_estudiante'))

def listaEstudiantes(request):
    return render(request,'usuarios/listaAlumnos.html',
    {'alumnos': Estudiante.objects.all()})

def datosAlumno(request,pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request,
                  'usuarios/alumnodetalle.html',
                  {'alumno': estudiante})

#--------------------------------------------------------------------------------------------------------------------------
@csrf_exempt
def creacion_profesor(request):
    if (request.method == 'POST'):
        profesor_form = profesorForm(request.POST)
        if profesor_form.is_valid():
            nuevo_profesor = profesor_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el profesor {}'.format(nuevo_profesor))
            return redirect(reverse('usuarios:registro_usuario_profesor'))
    else:
        profesor_form = profesorForm()    
    return render(request,'usuarios/crearprofesor.html',{'form': profesor_form})

@csrf_exempt
def edicion_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk = pk)

    if (request.method == 'POST'):
        profesor_form = profesorForm(request.POST, request.FILES, instance=profesor)
        if profesor_form.is_valid():
            profesor_form.save(commit=True)
            messages.success(request,
                             'Se ha editado correctamente el profesor con el {}'.format(profesor))
            return redirect(reverse('usuarios:registro_usuario_profesor'))
    else:
        profesor_form = profesorForm(instance=profesor)    
    return render(request,'usuarios/modificarprofesor.html',{'form': profesor_form})


def profesor_delete(request):
    if request.method == 'POST':
        if 'id_profesor' in request.POST:
            profesor = get_object_or_404(Profesor, pk=request.POST['id_profesor'])
            nombre_profesor = profesor.nombreyapellido
            profesor.delete()
            messages.success(request, 'Se ha eliminado exitosamente el profesor {}'.format(nombre_profesor))
        else:
            messages.error(request, 'Debe indicar qué profesor se desea eliminar')
    return redirect(reverse('usuarios:registro_usuario_profesor'))

def listaProfesores(request):
    return render(request,'usuarios/listaProfesor.html',
    {'profesores': Profesor.objects.all()})

def datosProfesor(request,pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request,
                  'usuarios/profesordetalle.html',
                  {'profesor': profesor})

#----------------------------------------------------------------------------------------------------

