from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from apps.cursos.forms import cursoForm, efectivoForm, inscripcionForm, tarjetaForm, transferenciaForm
from apps.usuarios.forms import estudianteForm
from apps.usuarios.models import Estudiante
from .models import curso, Inscriptos


# Create your views here.

@permission_required('cursos.view_curso', raise_exception=True)
def listaCursos(request):
    return render(request, 'cursos/tablaCursos.html',
                  {'cursos': curso.objects.all()})

@permission_required('cursos.add_curso', raise_exception=True)
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
    return render(request, 'cursos/formcrearcurso.html', {'form': curso_form})


@permission_required('cursos.change_curso', raise_exception=True)
def edicion_curso(request, pk):
    Curso = get_object_or_404(curso, pk=pk)

    if (request.method == 'POST'):
        curso_form = cursoForm(request.POST, request.FILES, instance=Curso)
        if curso_form.is_valid():
            curso_form.save(commit=True)
            messages.success(request,
                             'Se ha editado correctamente el curso con el {}'.format(Curso))
            return redirect(reverse('cursos:registroCursos'))
    else:
        curso_form = cursoForm(instance=Curso)
    return render(request, 'cursos/modificarCurso.html', {'form': curso_form})


@permission_required('cursos.add_group', raise_exception=True)
@permission_required('cursos.view_curso', raise_exception=True)
@permission_required('cursos.change_curso', raise_exception=True)
@permission_required('cursos.delete_curso', raise_exception=True)
def ventana_ecurso(request, pk):
    Curso = get_object_or_404(curso, pk=pk)
    return render(request,
                  'cursos/evaluacionCurso.html',
                  {'curso': Curso})


@permission_required('cursos.add_group', raise_exception=True)
@permission_required('cursos.view_curso', raise_exception=True)
@permission_required('cursos.change_curso', raise_exception=True)
@permission_required('cursos.delete_curso', raise_exception=True)
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


@permission_required('cursos.delete_curso', raise_exception=True)
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


# ----------------------------------------------------------------------------#
@permission_required('cursos.view_curso', raise_exception=True)
def datosCurso(request, pk):
    bandera = 0;
    Curso = get_object_or_404(curso, pk=pk)
    listaIns = Inscriptos.objects.all()
    if(request.user.first_name == 'Alumno'):
        if(request.user.estudiante.id):
            for inscripto in listaIns:
                if(request.user.estudiante.id == inscripto.id):
                    bandera = 1
                    break

    return render(request,
                  'cursos/datosCurso.html',
                  {'curso': Curso,'bandera': bandera})


def estadisticas(request):
    return render(request, 'cursos/estadisticas.html')


@permission_required('cursos.view_curso', raise_exception=True)
@permission_required('cursos.change_curso', raise_exception=True)
@permission_required('cursos.delete_curso', raise_exception=True)
def estadoCursos(request):
    return render(request, 'cursos/estadoCursos.html', {'cursos': curso.objects.all()})
#------------------------------------------------------------------------------------------------------
@permission_required('cursos.add_inscriptos',raise_exception=True)
def inscripcion(request):
    return render(request, 'cursos/inscripcion.html')




# ---------------------------------------------------------------------------------------------#

def pago(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    return render(request, 'cursos/seleccionpago.html',{'curso':Curso})

@permission_required('cursos.add_pagoefectivo', raise_exception=True)
def C_pagoEfectivo(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    if (request.method == 'POST'):
        efectivo_form = efectivoForm(request.POST)
        if efectivo_form.is_valid():
            nuevo_pagoEfectivo = efectivo_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_pagoEfectivo))
            return redirect(reverse('cursos:registroCursos'))
    else:
        efectivo_form = efectivoForm(initial={'curso': Curso.id})
    return render(request, 'cursos/pagoEfectivo.html', {'form': efectivo_form})


# ---------------------------------------------------------------Tarjeta_-------------------------------------
@permission_required('cursos.add_pagotarjeta', raise_exception=True)
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
    return render(request, 'cursos/pagoTarjeta.html', {'form': tarjeta_form})


# -----------------------------------------------------------Transferencia-------------------------------

@permission_required('cursos.add_pagotransferencia', raise_exception=True)
def C_pagoTransferencia(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    ideEstudiante = request.user.estudiante.id
    Alumno = get_object_or_404(Estudiante, pk=ideEstudiante)
    if (request.method == 'POST'):
        trans_form = transferenciaForm(request.POST)
        if trans_form.is_valid():
            nuevo_pagoTransferencia = trans_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_pagoTransferencia))
            return redirect(reverse('cursos:registroCursos'))
    else:
        trans_form = transferenciaForm(initial={'curso': Curso.id, 'alumno': Alumno.id})
    return render(request, 'cursos/pagotransferencia.html', {'form': trans_form})


# --------------------------------------------------------------------------------------------------------#
@permission_required('cursos.add_inscriptos', raise_exception=True)
def inscripcion_curso(request, pk):
    Curso = get_object_or_404(curso, pk=pk)
    ideEstudiante = request.user.estudiante.id
    Alumno = get_object_or_404(Estudiante, pk=ideEstudiante)
    if (request.method == 'POST'):
        efectivo_form = inscripcionForm(request.POST)
        if efectivo_form.is_valid():
            nuevo_pagoEfectivo = efectivo_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_pagoEfectivo))
            return redirect(reverse('cursos:registroCursos'))
    else:
        efectivo_form = inscripcionForm(initial={'curso': Curso.id, 'inscripto': Alumno.id})
    return render(request, 'cursos/inscripcion.html', {'form': efectivo_form})

@permission_required('cursos.view_inscriptos',raise_exception=True)
def listaInscriptos(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    return render(request, 'cursos/listaAlumnos.html',
                  {'alumnos': Inscriptos.objects.all() ,'curso': Curso})

@permission_required('cursos.change_inscriptos',raise_exception=True)
def evaluar_inscripto(request, pk):
    inscripto= get_object_or_404(Inscriptos, pk=pk)

    if (request.method == 'POST'):
        curso_form = inscripcionForm(request.POST, request.FILES, instance=inscripto)
        if curso_form.is_valid():
            curso_form.save(commit=True)
            messages.success(request,
                             'Se ha evaluado correctamente el Inscripto con el {}'.format(inscripto))
            return HttpResponseRedirect(reverse('cursos:listaAlumnos', args=(inscripto.curso.id,)))
    else:
        curso_form = inscripcionForm(instance=inscripto)
    return render(request, 'cursos/evaluarins.html', {'form': curso_form})