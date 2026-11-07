from django.shortcuts import render, get_object_or_404
from Academica.models import Faculty, Department

# Create your views here.

## Facultades 

def listaFacultades(request):
    facultades = Faculty.objects.all()
    return render(request, 'facultades/listado_facultades.html',
                 {'facultades': facultades})

def detalleFacultad(request, id):
    facultad = get_object_or_404( Faculty,faculty_id=id)
    return render(request,'facultades/detalle_facultad.html',{'facultad': facultad}
    )

## Departamentos

def listaDepartamentos(request):
    departamentos = Department.objects.select_related('faculty')
    return render(request, 'departamentos/listado_departamentos.html',
                     {'departamentos': departamentos })


def detalleDepartamento(request, id):
    departamento = get_object_or_404(
        Department.objects.select_related('faculty'),
        department_id=id)

    return render( request,'departamentos/detalle_departamento.html',
        {'departamento': departamento}
    )