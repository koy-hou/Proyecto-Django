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

def contact(request):
    return render(request,'core/contact.html')

def album(request):
    context = {'albums': Album.objects.all(),'recomendacion': Recomendacion.objects.all()}
    return render(request,'core/album.html',context)

def album_recomendado(request,album_id):
    try:
        album = Album.objects.get(idAlbum=album_id)
        if album:
            context = {'album':album}
            return render(request,'core/albums-recomendado.html',context)
        else:
            return redirect(reverse('album') + '?lala')
    except:
        return redirect(reverse('album') + '?FAIL')