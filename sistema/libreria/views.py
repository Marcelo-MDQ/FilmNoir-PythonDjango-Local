from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pelicula
from .forms import PeliculaForm

# Create your views here.
def inicio(request):
    peliculas = []
    queryset = request.GET.get("buscar")
    if queryset:
        peliculas = (Pelicula.objects.filter(nombre__icontains=queryset).all() | Pelicula.objects.filter(director__icontains=queryset).all()).order_by('nombre','anio')
    return render(request, 'paginas/inicio.html', {'peliculas': peliculas})

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def buscador(request):
    return render(request, 'paginas/buscador.html')

def peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})

def crear(request):
    formulario = PeliculaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('peliculas')
    return render(request, 'peliculas/crear.html', {'formulario': formulario})

def editar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    formulario = PeliculaForm(request.POST or None, request.FILES or None, instance=pelicula)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('peliculas')
    return render(request, 'peliculas/editar.html', {'formulario': formulario})

def buscar(request, aBuscar):
    peliculas = Pelicula.objects.filter(nombre__icontains=aBuscar).all().order_by('nombre','anio')
    return render(request, 'peliculas/mostrar.html', {'peliculas': peliculas})

def eliminar(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('peliculas')

def reseniaPelicula(request, id):
    peliculas = Pelicula.objects.get(id=id)
    return render(request, 'peliculas/reseniaPelicula.html', {'peliculas': peliculas})
