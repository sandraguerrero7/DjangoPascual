from django.shortcuts import render
from Academica.models import Faculty

# Create your views here.

def listaFacultades(request):
    facultades = Faculty.objects.all()
    return render(request, 'facultades/listado_facultades.html',
                 {'facultades': facultades})