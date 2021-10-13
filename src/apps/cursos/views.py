from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def tablaCursos(request):
    print(request)
    return render(request, 'cursos/tablaCursos.html')