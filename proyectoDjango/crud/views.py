# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from .models import *
from .forms import *


# Create your views here.
def root(request):
    return redirect('albums/')

def album_lista(request):
    context = {'albums': Album.objects.all()}
    return render(request,'crud/albums.html',context)

def album_nuevo(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            idAlbum = form.cleaned_data.get('idAlbum')
            title = form.cleaned_data.get('title')
            artista = form.cleaned_data.get('artista')
            recomendacion = form.cleaned_data.get('recomendacion')
            genero = form.cleaned_data.get('genero')
            analisis = form.cleaned_data.get('analisis')
            image = form.cleaned_data.get('image')
            obj = Album.objects.create(
                idAlbum = idAlbum,
                title = title,
                artista = artista,
                recomendacion = recomendacion,
                analisis = analisis,
                image = image
            )
            obj.save()
            return redirect(reverse('albums')+ '?OK')
        else:
            return redirect(reverse('albums')+ '?FAIL')
    else:
        form = AlbumForm
    return render(request,'crud/albums-nuevo.html',{'form':form})

def album_editar(request,album_id):
    try:
        album = Album.objects.get(idAlbum = album_id)
        form = AlbumForm(instance=album)

        if request.method == 'POST':
            form = AlbumForm(request.POST, request.FILES, instance=album)
            if form.is_valid():
                form.save()
                return redirect(reverse('albums') + '?UPDATED')
            else:
                return redirect(reverse('album-editar') + album_id) 

        context = {'form':form}
        return render(request,'crud/albums-editar.html',context)
    except:
        return redirect(reverse('albums') + '?NO_EXISTS')


def album_detalle(request, album_id):
    try:
        album = Album.objects.get(idAlbum=album_id)
        if album:
            context = {'album':album}
            return render(request,'crud/albums-detalles.html',context)
        else:
            return redirect(reverse('albums') + '?lala')
    except:
        return redirect(reverse('albums') + '?FAIL')
    
def album_eliminar(request,album_id):
    try:
        album = Album.objects.get(idAlbum=album_id)
        album.delete()
        return redirect(reverse('albums') + '?DELETED')
    except:
        return redirect(reverse('albums') + '?FAIL')