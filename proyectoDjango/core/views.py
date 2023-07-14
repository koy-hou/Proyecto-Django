from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from crud.models import *
from crud.forms import *


# Create your views here.
def root(request):
    return redirect('/home/')

def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')

def fotodeldia(request):
    return render(request,'core/fotodeldia.html')

def contact(request):
    form = ContactoForm()
    context = {'form':form}
    if request.method == 'POST':
        form = ContactoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        else:
            return redirect(request.path)
    return render(request,'core/contact.html',context)

def album(request):
    generos = Genero.objects.all()
    context = {'albums': Album.objects.all(),'recomendacion': Recomendacion.objects.all(),'Generos':generos}
    return render(request,'core/album.html',context)

def album_recomendado(request, album_id):
    
    album = Album.objects.get(idAlbum=album_id)
    context = {'album':album}
    return render(request,'core/album-recomendado.html',context)

def artistafiltro(request):
    filter_field = request.GET.getlist('filter_field')

    generos = Genero.objects.all()
    cantidad_por_genero = {}
    
    albums = Album.objects.all()
    if filter_field:
        albums = albums.filter(genero__in=filter_field)

    context = {'albums':albums,
               'Generos':Genero.objects.all(),
               'cantidad':albums.count(),
               'cantidad_por_genero':cantidad_por_genero}
    return render(request,'core/album.html',context)