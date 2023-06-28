from django import forms
from django.forms import ModelForm
from .models import *

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            'idAlbum',
            'title',
            'artista',
            'recomendacion',
            'genero',
            'analisis',
            'image'
        ]
        labels = {
            'idAlbum':'ID',
            'title':'Título',
            'artista':'Artista',
            'recomendacion':'Recomendacion',
            'genero':'Genero',
            'analisis':'Analisis',
            'image':'Imagen'
        }
        widgets = {
            'idAlbum':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'artista':forms.TextInput(attrs={'class':'form-control'}),
            'recomendacion':forms.Select(attrs={'class':'form-control'}),
            'genero':forms.Select(attrs={'class':'form-control'}),
            'analisis':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }
