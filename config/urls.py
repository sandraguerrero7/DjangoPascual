from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Academica.views import listaFacultades, listaDepartamentos, detalleDepartamento, detalleFacultad


urlpatterns = [
    path('admin/', admin.site.urls),
    path('facultades/', listaFacultades,  name='listado_facultades'),
    path('facultades/detalle/<str:id>/', detalleFacultad, name='detalleFacultad'),
    path('departamentos/', listaDepartamentos,  name='listado_dptos'),
    path('departamentos/detalle/<str:id>/', detalleDepartamento, name='detalleDepartamento')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
