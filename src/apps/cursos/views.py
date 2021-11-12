from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from apps.cursos.forms import cursoForm, efectivoForm, estadisticaForm, inscripcionForm, tarjetaForm, transferenciaForm
from apps.usuarios.forms import estudianteForm
from apps.usuarios.models import Estudiante
from .models import PagoEfectivo, PagoTarjeta, PagoTransferencia, curso, Inscriptos,Pago
from apps.usuarios.models import Persona


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
    pago = False
   
    Curso = get_object_or_404(curso, pk=pk)
    listaIns = Inscriptos.objects.all()
    if(request.user.first_name.lower() == 'alumno'):
        inscripto = Inscriptos.objects.filter(pk=request.user.estudiante.id, curso= Curso.id)
        if(not inscripto):
            pago=True
            
        if(request.user.estudiante.id):
            for estudiante in listaIns:
                if(request.user.estudiante.id == estudiante.inscripto.id and Curso.id == estudiante.curso.id):
                    bandera = 1
                    break

    return render(request,
                  'cursos/datosCurso.html',
                  {'curso': Curso,'bandera': bandera,'pago':pago})

#----------------------------------------------------------------------------------------------------------------------------
def estadisticas(request):
    return render(request, 'cursos/estadisticas.html', {'cursos':curso.objects.all()})
    

def estadisticas_1(request):
    #if request.method == 'POST':
            Cursos = curso.objects.all()
            #Curso = get_object_or_404(curso,pk=request.POST['id_curso'])
            
            #cantinscriptos = []
            for data in Cursos:
                #cantinscriptos.append(len(Inscriptos.objects.filter(curso = data.id)))
                data.cant = len(Inscriptos.objects.filter(curso = data.id))
                 
            #print(cantinscriptos)
            return render(request,'cursos/estadisticascantinscriptos.html',{'cursos':Cursos})
            # nombre_curso = Curso.nombrecurso
            # Curso.delete()
            # messages.success(request, 'Se ha eliminado exitosamente el curso {}'.format(nombre_curso))
        # else:
            # messages.error(request, 'Debe indicar qué Programa se desea eliminar')

def estadisticas_2(request):
    Cursos = curso.objects.all()
    
    for data in Cursos:
        data.cant = len(Inscriptos.objects.filter(curso = data.id))
        data.cantP= len(PagoEfectivo.objects.filter(curso = data.id)) + len(PagoTarjeta.objects.filter(curso = data.id)) + len(PagoTransferencia.objects.filter(curso = data.id)) 
        data.cantD= data.cant - data.cantP
    
    return render(request,'cursos/estadisticascantpago.html',{'cursos':Cursos})    



def estadisticas_3(request):
    pass
#--------------------------------------------------------------------------------------------------------------------------------
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
@permission_required('cursos.add_pagoefectivo', raise_exception=True)
@permission_required('cursos.add_pagotarjeta', raise_exception=True)
@permission_required('cursos.add_pagotarjeta', raise_exception=True)
def pago(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    return render(request, 'cursos/seleccionpago.html',{'curso':Curso})

@permission_required('cursos.add_pagoefectivo', raise_exception=True)
def C_pagoEfectivo(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    idinscripto = request.user.estudiante.id
    inscripto = get_object_or_404(Estudiante, pk=idinscripto)
    if (request.method == 'POST'):
        efectivo_form = efectivoForm(request.POST)
        if efectivo_form.is_valid():
            nuevo_pagoEfectivo = efectivo_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_pagoEfectivo))
            return redirect(reverse('cursos:comprobante_pago', args={nuevo_pagoEfectivo.id}))
    else:
        efectivo_form = efectivoForm(initial={'curso': Curso.id,'importe':Curso.costo,'inscripto':inscripto.id})
    return render(request, 'cursos/pagoEfectivo.html', {'form': efectivo_form,'curso':Curso})


# ---------------------------------------------------------------Tarjeta_-------------------------------------
@permission_required('cursos.add_pagotarjeta', raise_exception=True)
def C_pagoTarjeta(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    idinscripto = request.user.estudiante.id
    inscripto = get_object_or_404(Estudiante, pk=idinscripto)
    if (request.method == 'POST'):
        tarjeta_form = tarjetaForm(request.POST)
        if tarjeta_form.is_valid():
            nuevo_pagoTarjeta = tarjeta_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_pagoTarjeta))
            return redirect(reverse('cursos:comprobante_pagoT', args={nuevo_pagoTarjeta.id}))
    else:
        tarjeta_form = tarjetaForm(initial={'curso': Curso.id,'importe':Curso.costo,'inscripto':inscripto.id})
    return render(request, 'cursos/pagoTarjeta.html', {'form': tarjeta_form,'curso':Curso})


# -----------------------------------------------------------Transferencia-------------------------------

@permission_required('cursos.add_pagotransferencia', raise_exception=True)
def C_pagoTransferencia(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    idinscripto = request.user.estudiante.id
    inscripto = get_object_or_404(Estudiante, pk=idinscripto)
    if (request.method == 'POST'):
        trans_form = transferenciaForm(request.POST)
        if trans_form.is_valid():
            nuevo_pagoTransferencia = trans_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_pagoTransferencia))
            return redirect(reverse('cursos:comprobante_pagoB', args={nuevo_pagoTransferencia.id}))
    else:
        trans_form = transferenciaForm(initial={'curso': Curso.id,'importe':Curso.costo,'inscripto':inscripto.id})
    return render(request, 'cursos/pagotransferencia.html', {'form': trans_form,'curso':Curso})


# --------------------------------------------------------------------------------------------------------#
@permission_required('cursos.add_inscriptos', raise_exception=True)
def inscripcion_curso(request, pk):
    Curso = get_object_or_404(curso, pk=pk)
    ideEstudiante = request.user.estudiante.id
    Alumno = get_object_or_404(Estudiante, pk=ideEstudiante)
    if (request.method == 'POST'):
        inscripcion_form = inscripcionForm(request.POST)
        if inscripcion_form.is_valid():
            nuevo_pagoEfectivo = inscripcion_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_pagoEfectivo))
            return redirect(reverse('cursos:registroCursos'))
    else:
        inscripcion_form = inscripcionForm(initial={'curso': Curso.id, 'inscripto': Alumno.id})
    return render(request, 'cursos/inscripcion.html', {'form': inscripcion_form})

@permission_required('cursos.view_inscriptos',raise_exception=True)
def listaInscriptos(request,pk):
    Curso = get_object_or_404(curso, pk=pk)
    return render(request, 'cursos/listaAlumnos.html',
                  {'alumnos': Inscriptos.objects.filter(curso = Curso) ,'curso': Curso})

@permission_required('cursos.change_inscriptos',raise_exception=True)
def evaluar_inscripto(request, pk):
    inscripto= get_object_or_404(Inscriptos, pk=pk)

    if (request.method == 'POST'):
        inscripto_form = inscripcionForm(request.POST, request.FILES, instance=inscripto)
        if inscripto_form.is_valid():
            inscripto_form.save(commit=True)
            messages.success(request,
                             'Se ha evaluado correctamente el Inscripto con el {}'.format(inscripto))
            return HttpResponseRedirect(reverse('cursos:listaAlumnos', args=(inscripto.curso.id,)))
    else:
        inscripto_form = inscripcionForm(instance=inscripto)
    return render(request, 'cursos/evaluarins.html', {'form': inscripto_form})

def comprobantePago(request, pk):
    comprobante = get_object_or_404(PagoEfectivo, pk=pk)
    return render(request,
                  'cursos/comprobantePago.html',
                  {'comprobante': comprobante})

def comprobantePagoT(request, pk):
    comprobante = get_object_or_404(PagoTarjeta, pk=pk)
    return render(request,
                  'cursos/comprobantePagoT.html',
                  {'comprobante': comprobante})

def comprobantePagoB(request, pk):
    comprobante = get_object_or_404(PagoTransferencia,pk=pk)
    return render(request,
                  'cursos/comprobantePagoB.html',
                  {'comprobante': comprobante})                  