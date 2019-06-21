from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.AdminNoticias.models import ArticuloModelo

# Create your views here.

def Index(request):
    return render(request, 'vista/Index.html')
    
def Eventos(request):
    datos = ArticuloModelo.objects.filter(familia = 'E')
    return render(request, 'vista/Eventos.html', {'eventos':datos})

def Noticias(request):
    datos = ArticuloModelo.objects.filter(familia = 'N')
    return render(request, 'vista/Noticias.html', {'noticias':datos})

def Detalle(request, id):
    dato = ArticuloModelo.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'vista/Detalle.html', {'articulo':dato})
    else:
        return redirect(request, 'Index')
    return HttpResponse ("detalle")