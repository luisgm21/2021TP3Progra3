from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from apps.cursos.forms import cursoForm, efectivoForm, tarjetaForm, transferenciaForm
from .models import curso,Inscriptos
# Create your views here.

@permission_required('view_curso',raise_exception=True)
def listaCursos(request):
    return render(request, 'cursos/tablaCursos.html',
    {'cursos': curso.objects.all()})

def listaInscriptos(request):
    return render(request,'cursos/tablaAlumnos.html',
    {'estudiantes': Inscriptos.objects.all() })
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

@permission_required('add_curso',raise_exception=True)
def creacion_curso(request):
    if (request.method == 'POST'):
        curso_form = cursoForm(request.POST)
        if curso_form.is_valid():
            nuevo_curso = curso_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_curso))
            return redirect(reverse('cursos:estadoCursos'))
    else:
        curso_form = cursoForm()    
    return render(request,'cursos/formcrearcurso.html',{'form': curso_form})

@permission_required('change_curso',raise_exception=True)
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


@permission_required('view_curso',raise_exception=True)
@permission_required('change_curso',raise_exception=True)
@permission_required('delete_curso',raise_exception=True)
def ventana_ecurso(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    return render(request,
                  'cursos/evaluacionCurso.html',
                  {'curso': Curso})


@permission_required('view_curso',raise_exception=True)
@permission_required('change_curso',raise_exception=True)
@permission_required('delete_curso',raise_exception=True)
def evaluar_curso(request):
    if request.method == 'POST':
        if 'id_curso' in request.POST:
            Curso = get_object_or_404(curso, pk=request.POST['id_curso'])
            nombre_curso = Curso.nombrecurso
            Curso.motivo = request.POST['motivo']
            Curso.estadocurso = request.POST['estadocurso']
            Curso.save()
            messages.success(request, 'Se ha eliminado exitosamente el curso {}'.format(nombre_curso))
        else:
            messages.error(request, 'Debe indicar qué Programa se desea eliminar')
    return redirect(reverse('cursos:registroCursos'))



@permission_required('delete_curso',raise_exception=True)
def curso_delete(request):
    if request.method == 'POST':
        if 'id_curso' in request.POST:
            Curso = get_object_or_404(curso, pk=request.POST['id_curso'])
            nombre_curso = Curso.nombrecurso
            Curso.delete()
            messages.success(request, 'Se ha eliminado exitosamente el curso {}'.format(nombre_curso))
        else:
            messages.error(request, 'Debe indicar qué Programa se desea eliminar')
    return redirect(reverse('cursos:registroCursos'))

#----------------------------------------------------------------------------#
@permission_required('view_curso',raise_exception=True)
def datosCurso(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    return render(request,
                  'cursos/datosCurso.html',
                  {'curso': Curso})

def estadisticas(request):
    return render(request, 'cursos/estadisticas.html') 

@permission_required('view_curso',raise_exception=True)
@permission_required('change_curso',raise_exception=True)
@permission_required('delete_curso',raise_exception=True)
def estadoCursos(request):
    return render(request, 'cursos/estadoCursos.html',{'cursos': curso.objects.all()}) 

  
def inscripcion(request):
    return render(request, 'cursos/inscripcion.html')   
def pago(request):
    return render(request, 'cursos/seleccionpago.html')   
#---------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------
@permission_required('add_pagoefectivo',raise_exception=True)
def C_pagoEfectivo(request):
    if (request.method == 'POST'):
        efectivo_form = efectivoForm(request.POST)
        if efectivo_form.is_valid():
            nuevo_pagoEfectivo = efectivo_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_pagoEfectivo))
            return redirect(reverse('cursos:registroCursos'))
    else:
        efectivo_form = efectivoForm()    
    return render(request,'cursos/pagoEfectivo.html',{'form': efectivo_form})
#---------------------------------------------------------------Tarjeta_-------------------------------------
@permission_required('add_pagotarjeta',raise_exception=True)
def C_pagoTarjeta(request):
    if (request.method == 'POST'):
        tarjeta_form = tarjetaForm(request.POST)
        if tarjeta_form.is_valid():
            nuevo_pagoTarjeta = tarjeta_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_pagoTarjeta))
            return redirect(reverse('cursos:registroCursos'))
    else:
        tarjeta_form = tarjetaForm()    
    return render(request,'cursos/pagoTarjeta.html',{'form': tarjeta_form})

#-----------------------------------------------------------Transferencia-------------------------------

@permission_required('add_pagotransferencia',raise_exception=True)
def C_pagoTransferencia(request):
    if (request.method == 'POST'):
        trans_form = transferenciaForm(request.POST)
        if trans_form.is_valid():
            nuevo_pagoTransferencia = trans_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_pagoTransferencia))
            return redirect(reverse('cursos:registroCursos'))
    else:
        trans_form = transferenciaForm()    
    return render(request,'cursos/pagoTarjeta.html',{'form': trans_form})        