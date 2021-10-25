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

@csrf_exempt
def edicion_curso(request, pk):
    Curso = get_object_or_404(curso, pk = pk)

    if (request.method == 'POST'):
        curso_form = cursoForm(request.POST, request.FILES, instance=Curso)
        if curso_form.is_valid():
            curso_form.save(commit=True)
            messages.success(request,
                             'Se ha editado correctamente el curso con el {}'.format(Curso))
            return redirect(reverse('cursos:registroCursos'))
    else:
        curso_form = cursoForm(instance=Curso)    
    return render(request,'cursos/modificarCurso.html',{'form': curso_form})

def curso_delete(request):
    if request.method == 'POST':
        if 'id_curso' in request.POST:
            Curso = get_object_or_404(curso, pk=request.POST['id_curso'])
            nombre_curso = curso.nombrecurso
            Curso.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Programa {}'.format(nombre_curso))
        else:
            messages.error(request, 'Debe indicar qué Programa se desea eliminar')
    return redirect(reverse('cursos:registroCursos'))


def tablaCursos(request):
    return render(request, 'cursos/tablaCursos.html')

def datosCurso(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    return render(request,
                  'cursos/datosCurso.html',
                  {'curso': Curso})

def estadisticas(request):
    return render(request, 'cursos/estadisticas.html') 

def estadoCursos(request):
    return render(request, 'cursos/estadoCursos.html')   
def inscripcion(request):
    return render(request, 'cursos/inscripcion.html')   
def pago(request):
    return render(request, 'cursos/pago.html')   
