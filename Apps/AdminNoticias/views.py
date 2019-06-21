from django.shortcuts import render, redirect
from django.http import HttpResponse

from Apps.AdminNoticias.forms import ArticuloForm
from Apps.AdminNoticias.models import ArticuloModelo

# Create your views here.

def noticias_listar(request):
    datos = ArticuloModelo.objects.all()
    contexto = {'lista': datos}
    return render(request, 'noticias/Listar.html', contexto)
    # return HttpResponse("Listar")

def noticias_crear(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('noticias_listar')
    else:
        form=ArticuloForm()
    return render(request, "noticias/Crear.html", {'articulo':form})

def noticias_editar(request, id): 
    articulo = ArticuloModelo.objects.get(id=id)
    if request.method == "POST":
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('noticias_listar')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, "noticias/Editar.html",{'articulo':form})

def noticias_borrar(request, id):
    articulo = ArticuloModelo.objects.get(id=id)
    if request.method == "POST":
        articulo.delete()
        return redirect('noticias_listar')
    else:
        return render(request, 'noticias/Borrar.html', {'articulo': articulo})
   