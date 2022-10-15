from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('buscador', views.buscador, name='buscador'),
    path('peliculas', views.peliculas, name='peliculas'),
    path('peliculas/crear', views.crear, name='crear'),
    path('peliculas/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('buscar/<str:aBuscar>', views.buscar, name='buscar'),
    path('<int:id>/',views.reseniaPelicula, name = 'resenia_Pelicula')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)